from general_helpers import lists_dicts


def test_sort_alphanumeric():
    assert lists_dicts.sort_alphanumeric(["B", "01", "99", "0", "A"]) == ["0", "01", "99", "A",
                                                                              "B"], "Sollte anders sein"
