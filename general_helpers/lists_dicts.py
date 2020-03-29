import re


def sort_alphanumeric(data):
    """
    Sortiert eine Liste alphanumerisch sinnvoll.
    sorted_aphanumeric(["1", "10", "2", "foo_10", "foo_8"]) ) -> ['1', '2', '10', 'foo_8', 'foo_10']
    :param data: Liste
    :return: sortierte Liste
    """
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)