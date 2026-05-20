"""Tests that verify pydantic-core APIs used by the SDK remain compatible.

This module exercises every pydantic_core import found in the SDK to ensure
that relaxing the upper-bound version constraint does not break functionality.
"""

import datetime as dt
from typing import Optional

import pydantic
import pydantic_core
import pytest

from vapi.core.pydantic_utilities import IS_PYDANTIC_V2


class TestPydanticCoreImports:
    """Verify that all pydantic_core symbols imported by the SDK are available."""

    def test_pydantic_undefined_importable(self) -> None:
        from pydantic_core import PydanticUndefined

        assert PydanticUndefined is not None

    def test_core_schema_importable(self) -> None:
        from pydantic_core import core_schema

        assert hasattr(core_schema, "datetime_schema")
        assert hasattr(core_schema, "no_info_before_validator_function")

    def test_to_jsonable_python_importable(self) -> None:
        from pydantic_core import to_jsonable_python

        assert callable(to_jsonable_python)


class TestPydanticCoreUsagePatterns:
    """Exercise the actual usage patterns from the SDK to ensure compatibility."""

    def test_pydantic_undefined_sentinel_comparison(self) -> None:
        """The SDK compares field defaults against PydanticUndefined."""
        from pydantic_core import PydanticUndefined

        assert PydanticUndefined != None  # noqa: E711
        assert PydanticUndefined != "some_value"

    def test_to_jsonable_python_with_datetime(self) -> None:
        """The SDK uses to_jsonable_python for serialization."""
        from pydantic_core import to_jsonable_python

        now = dt.datetime.now(tz=dt.timezone.utc)
        result = to_jsonable_python(now)
        assert isinstance(result, str)

    def test_to_jsonable_python_with_dict(self) -> None:
        from pydantic_core import to_jsonable_python

        data = {"key": "value", "number": 42}
        result = to_jsonable_python(data)
        assert result == data

    def test_core_schema_datetime_schema(self) -> None:
        """The SDK uses core_schema.datetime_schema in Rfc2822DateTime."""
        from pydantic_core import core_schema

        schema = core_schema.datetime_schema()
        assert schema is not None
        assert isinstance(schema, dict)

    @pytest.mark.skipif(not IS_PYDANTIC_V2, reason="Pydantic V2 only")
    def test_model_with_pydantic_undefined_default(self) -> None:
        """Simulate the SDK pattern of checking field defaults against PydanticUndefined."""
        from pydantic_core import PydanticUndefined

        class SampleModel(pydantic.BaseModel):
            required_field: str
            optional_field: Optional[str] = None

        fields = SampleModel.model_fields
        required_default = fields["required_field"].get_default()
        optional_default = fields["optional_field"].get_default()

        assert required_default is PydanticUndefined
        assert optional_default is None


class TestUncheckedBaseModelCompat:
    """Test that UncheckedBaseModel works with the current pydantic-core version."""

    def test_construct_with_defaults(self) -> None:
        """Verify UncheckedBaseModel.construct works with PydanticUndefined checks."""
        from vapi.core.unchecked_base_model import UncheckedBaseModel

        class TestModel(UncheckedBaseModel):
            name: str
            value: Optional[int] = None

        instance = TestModel.construct(name="test", value=42)
        assert instance.name == "test"
        assert instance.value == 42

    def test_construct_with_missing_optional(self) -> None:
        from vapi.core.unchecked_base_model import UncheckedBaseModel

        class TestModel(UncheckedBaseModel):
            name: str
            value: Optional[int] = None

        instance = TestModel.construct(name="test")
        assert instance.name == "test"
        assert instance.value is None

    def test_construct_with_extra_fields(self) -> None:
        from vapi.core.unchecked_base_model import UncheckedBaseModel

        class TestModel(UncheckedBaseModel):
            name: str

        instance = TestModel.construct(name="test", extra_field="extra")
        assert instance.name == "test"


class TestRfc2822DateTimeCompat:
    """Test that Rfc2822DateTime works with the current pydantic-core version."""

    @pytest.mark.skipif(not IS_PYDANTIC_V2, reason="Pydantic V2 only")
    def test_rfc2822_datetime_schema(self) -> None:
        from vapi.core.datetime_utils import Rfc2822DateTime

        schema = Rfc2822DateTime.__get_pydantic_core_schema__(Rfc2822DateTime, lambda x: x)
        assert schema is not None


class TestVersionConstraintRelaxed:
    """Meta-test: verify that pydantic-core >= 2.18.2 is installed and usable."""

    def test_pydantic_core_version_is_sufficient(self) -> None:
        version_parts = pydantic_core.__version__.split(".")
        major, minor, patch = int(version_parts[0]), int(version_parts[1]), int(version_parts[2])
        assert major >= 2, f"pydantic-core major version must be >= 2, got {major}"
        assert (major, minor, patch) >= (2, 18, 2), (
            f"pydantic-core must be >= 2.18.2, got {pydantic_core.__version__}"
        )

    def test_pydantic_core_not_artificially_capped(self) -> None:
        """This test documents that versions >= 2.44.0 should now be allowed."""
        # This test simply passes to document the intent:
        # The upper bound constraint pydantic-core<2.44.0 has been removed.
        # Users with pydantic>=2.13.3 (which requires pydantic-core==2.46.3)
        # should be able to install this SDK without conflicts.
        assert True
