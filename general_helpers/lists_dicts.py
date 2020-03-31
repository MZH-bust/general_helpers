import re
from general_helpers import datatypes


def sort_alphanumeric(list_of_strings: list) -> list:
    """Sortiert eine Liste alphanumerisch sinnvoll.

    Examples
    --------
    >>> sort_alphanumeric(["1", "10", "2", "foo_10", "foo_8"])
    ['1', '2', '10', 'foo_8', 'foo_10']

    Parameters
    ----------
    list_of_strings : list
        Eine Liste von Strings, die alphanumerisch sortiert werden soll.

    Returns
    -------
    list
        Alphanumerische Sortierung der Liste, die an die Funktion übergeben wurde.

    Raises
    ------
    TypeError
        Falls der Input Type keine Liste von Strings ist.

    """

    if not datatypes.is_list_of_strings(list_of_strings):
        raise TypeError

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(list_of_strings, key=alphanum_key)
