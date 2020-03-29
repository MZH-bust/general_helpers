import pytest
from general_helpers import datatypes


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param(["this", "is", "a", "list", "of", "strings"], True, id="Param1 - List of Strings"),
        pytest.param("no list, but string", False, id="Param2 - String only"),
        pytest.param(["this", "is", "a", 9], False, id="Param3 - List contains int"),
        pytest.param(10, False, id="Param4 - only int"),
    ],
)
def test_is_list_of_strings(input, expected):
    assert datatypes.is_list_of_strings(input) == expected

