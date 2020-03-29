def is_list_of_strings(obj):
    if isinstance(obj, list):
        return all(isinstance(s, str) for s in obj)
    return False
