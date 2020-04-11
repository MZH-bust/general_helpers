import pytest
from genutil import lists_dicts


class TestSortAlphanumeric:
    @pytest.mark.parametrize(
        "test_parameter,expected",
        [
            pytest.param(["1", "10", "2", "foo_10", "foo_8"], ['1', '2', '10', 'foo_8', 'foo_10'], id="Param1"),
            pytest.param(["Lonely String in List"], ["Lonely String in List"], id="Param2"),
        ],
    )
    def test_sort_alphanumeric(self, test_parameter, expected):
        assert lists_dicts.sort_alphanumeric(test_parameter) == expected

    def test_type_error(self):
        with pytest.raises(TypeError):
            lists_dicts.sort_alphanumeric([9])


