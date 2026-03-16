import collections.abc


def append_if_not_none(obj: any, value: any, key: str = None) -> any:
    if value is None:
        return obj

    if key is None and isinstance(obj, list):
        obj.append(value)

    if key is not None and isinstance(obj, dict):
        if key not in obj:
            obj[key] = []
        obj[key].append(value)

    return obj


def always_a_list(obj: any) -> list:
    """
    returns a list no matter what is in the input.
    if the argument is a list already it gets returned verbatim
    but if it is not, it is wrapped into a list
    """
    if isinstance(obj, list):
        return obj
    elif isinstance(obj, collections.abc.Iterable) and not isinstance(obj, (str, bytes)):
        return list(obj)
    else:
        return [obj]


def default_if_none(obj: any, default: any) -> any:
    if obj is None:
        return default
    return obj


def first_or_default(lst: any, default: any = None) -> any:
    if lst is None:
        return default
    if isinstance(lst, collections.abc.Iterable) and not isinstance(lst, (str, bytes)):
        for item in lst:
            return item
        return default
    return None


def get_if_exists(obj: any, key: str | None, default: any = None) -> any:
    if obj is None or key is None:
        return default

    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        else:
            return default

    attr = getattr(obj, key, default)
    return attr


def list_is_optional(obj: any) -> any:
    """
    returns a dictionary if a dictionary or a list with just one item is provided
    returns None if None is given, or an empty list
    returns a list otherwise
    """
    if isinstance(obj, list):
        if len(obj) == 0:
            return None
        elif len(obj) == 1:
            return obj[0]
    return obj


def list_without_nones(lst: list) -> list:
    return [e for e in lst if e is not None]


def none_if_empty(obj: any) -> any:
    if isinstance(obj, list) and len(obj) == 0:
        return None
    if isinstance(obj, dict) and not obj:
        return None
    return obj


def set_if_not_none(obj: any, value: any, key: str = None) -> any:
    if value is None:
        return obj

    if key is None and isinstance(obj, list):
        obj.append(value)

    if key is not None and isinstance(obj, dict):
        obj[key] = value

    return obj
