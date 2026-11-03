"""Exercise release guards with actual Git histories, without registry access."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parent


class ReleaseValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="sdk-release-")
        self.addCleanup(self.temp.cleanup)
        self.cwd = Path(self.temp.name)
        self.env = {
            **os.environ,
            "GIT_AUTHOR_NAME": "Release test",
            "GIT_AUTHOR_EMAIL": "test@example.com",
            "GIT_COMMITTER_NAME": "Release test",
            "GIT_COMMITTER_EMAIL": "test@example.com",
        }
        self.git("init", "--initial-branch=main")
        self.git("commit", "--allow-empty", "-m", "Approved release")
        self.approved = self.git("rev-parse", "HEAD")
        self.git("update-ref", "refs/remotes/origin/main", self.approved)
        (self.cwd / "pyproject.toml").write_text('[tool.poetry]\nversion = "3.0.0"\n')
        self.env.update(GITHUB_REF="refs/tags/v3.0.0", GITHUB_REF_NAME="v3.0.0", GITHUB_SHA=self.approved)

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.cwd, env=self.env, check=True, capture_output=True, text=True).stdout.strip()

    def guard(self):
        return subprocess.run(["bash", str(SCRIPTS / "verify-release-commit.sh")], cwd=self.cwd, env=self.env, capture_output=True, text=True)

    def test_approved_commit_and_ancestor_are_allowed(self):
        self.assertEqual(self.guard().returncode, 0)
        self.git("commit", "--allow-empty", "-m", "Newer approved commit")
        self.git("update-ref", "refs/remotes/origin/main", self.git("rev-parse", "HEAD"))
        self.git("checkout", "--detach", self.approved)
        self.assertEqual(self.guard().returncode, 0)

    def test_annotated_tag_is_resolved_to_commit(self):
        self.git("tag", "-a", "v3.0.0", "-m", "Release")
        self.env["GITHUB_SHA"] = self.git("rev-parse", "v3.0.0")
        self.assertEqual(self.guard().returncode, 0)

    def test_unmerged_commit_is_rejected(self):
        self.git("checkout", "-b", "unapproved")
        self.git("commit", "--allow-empty", "-m", "Unreviewed change")
        self.env["GITHUB_SHA"] = self.git("rev-parse", "HEAD")
        result = self.guard()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must already be merged", result.stdout)

    def test_wrong_checkout_is_rejected(self):
        self.git("commit", "--allow-empty", "-m", "Different checkout")
        result = self.guard()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("does not match", result.stdout)

    def test_missing_main_or_event_commit_is_rejected(self):
        self.git("update-ref", "-d", "refs/remotes/origin/main")
        self.assertNotEqual(self.guard().returncode, 0)
        del self.env["GITHUB_SHA"]
        self.assertNotEqual(self.guard().returncode, 0)

    def test_package_version_and_ref(self):
        for tag in ("3.0.0", "v3.0.0"):
            self.env.update(GITHUB_REF=f"refs/tags/{tag}", GITHUB_REF_NAME=tag)
            result = subprocess.run([sys.executable, str(SCRIPTS / "validate-release.py")], cwd=self.cwd, env=self.env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        for ref, tag in (("refs/heads/main", "main"), ("refs/heads/refs/tags/v3.0.0", "refs/tags/v3.0.0"), ("refs/tags/v3.0.1", "v3.0.1"), ("refs/tags/vv3.0.0", "vv3.0.0"), ("refs/tags/v3.0.0", "3.0.0"), ("", "")):
            with self.subTest(ref=ref, tag=tag):
                self.env.update(GITHUB_REF=ref, GITHUB_REF_NAME=tag)
                if not ref.startswith("refs/tags/"):
                    self.assertNotEqual(self.guard().returncode, 0)
                result = subprocess.run([sys.executable, str(SCRIPTS / "validate-release.py")], cwd=self.cwd, env=self.env, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
