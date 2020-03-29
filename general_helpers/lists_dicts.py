import re
from general_helpers import datatypes


def sort_alphanumeric(data):
    """
    Sortiert eine Liste alphanumerisch sinnvoll.
    sort_alphanumeric(["1", "10", "2", "foo_10", "foo_8"]) ) -> ['1', '2', '10', 'foo_8', 'foo_10']
    :param data: Liste
    :return: sortierte Liste
    """
    if not datatypes.is_list_of_strings(data):
        raise TypeError

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


if __name__ == "__main__":
    test = sort_alphanumeric(["1", "10", "2", "foo_10", "foo_8"])
    test2 = sort_alphanumeric("foo_8")

