import pytest


def generic_function(test_function, test_parameter, test_cases, expected):
    for test_type, value in test_cases.items():
        if test_type == "type":
            assert isinstance(test_function(*test_parameter), value) == expected
        elif test_type == "result":
            assert (test_function(*test_parameter) == value) is expected
        elif test_type == "error":
            with pytest.raises(value):
                test_function(*test_parameter)
        else:
            raise ValueError(f"Unbekannter Testfall {test_type}")
