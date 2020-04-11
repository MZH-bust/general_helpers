import pytest
from genutil import sharepoint_helper


class TestSpFieldText:
    @pytest.mark.parametrize(
        "test_parameter,expected",
        [
            pytest.param("20;#Lastname1, Firstname1;#91;#Lastname2, Firstname2;#184;#Lastname3, Firstname3",
                         ("Lastname1, Firstname1; Lastname2, Firstname2; Lastname3, Firstname3",
                          ["20", "91", "184"],
                          ["Lastname1, Firstname1", "Lastname2, Firstname2", "Lastname3, Firstname3"]),
                         id="Test for Multi User"),
            pytest.param("61;#Lastname, Firstname",
                         ("Lastname, Firstname",
                          ["61"],
                          ["Lastname, Firstname"]),
                         id="Test for Single User with identifier"),
            pytest.param("Lastname, Firstname",
                         ("Lastname, Firstname",
                          [""],
                          ["Lastname, Firstname"]),
                         id="Test for Single User without identifier"),

        ],
    )
    def test_sort_alphanumeric(self, test_parameter, expected):
        assert sharepoint_helper.SpFieldText(test_parameter).cleanse_text() == expected[0]
        assert sharepoint_helper.SpFieldText(test_parameter).get_identifier_list() == expected[1]
        assert sharepoint_helper.SpFieldText(test_parameter).get_value_list() == expected[2]
        assert sharepoint_helper.SpFieldText(test_parameter).identifier_value_list_transponed == [tuple(expected[1]),
                                                                                                  tuple(expected[2])]