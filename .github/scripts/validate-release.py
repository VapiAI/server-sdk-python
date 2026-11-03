"""Validate release refs before running package build code (Python 3.11+)."""

import os
from pathlib import Path
import sys
import tomllib


def main() -> None:
    tag = os.environ.get("GITHUB_REF_NAME", "")
    if not tag or os.environ.get("GITHUB_REF", "") != f"refs/tags/{tag}":
        sys.exit("Release requires a tag ref matching GITHUB_REF_NAME.")
    with Path("pyproject.toml").open("rb") as source:
        version = tomllib.load(source)["tool"]["poetry"]["version"]
    if tag not in (version, f"v{version}"):
        sys.exit(f"Release tag {tag} does not match package version {version}.")


if __name__ == "__main__":
    main()
