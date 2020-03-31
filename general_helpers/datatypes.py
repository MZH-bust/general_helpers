def is_list_of_strings(obj: any) -> bool:
    """Gibt zurück, ob es sich bei einer übergebenen Variable um eine Liste von Strings handelt.

    Examples
    --------
    >>> is_list_of_strings(["String1", "String2", "String3"])
    True
    >>> is_list_of_strings("String_only")
    False
    >>> is_list_of_strings([5, "not_only_string", "String2", "String3"])
    False

    Notes
    -----
    Ein einzelner String ist keine Liste von Strings.
    Entsprechend lautet der Rückgabewert hier ebenfalls False

    Parameters
    ----------
    obj : any
        Beliebiger Datentyp zur Überprüfung

    Returns
    -------
    bool
        True, falls es sich um eine Liste von Strings handelt, andernfalls False
    """

    if isinstance(obj, list):
        return all(isinstance(s, str) for s in obj)
    return False
