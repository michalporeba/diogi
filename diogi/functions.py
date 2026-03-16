from typing import Any, TypeVar, Iterable
import collections.abc

T = TypeVar('T')
D = TypeVar('D')


def append_if_not_none(obj: T, value: Any, key: str | None = None) -> T:
    if value is None:
        return obj

    if key is None and isinstance(obj, list):
        obj.append(value)

    if key is not None and isinstance(obj, dict):
        if key not in obj:
            obj[key] = []
        obj[key].append(value)

    return obj


def always_a_list(obj: Any) -> list[Any]:
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


def default_if_none(obj: T | None, default: T) -> T:
    if obj is None:
        return default
    return obj


def first_or_default(lst: Iterable[T] | Any, default: D = None) -> T | D | None:
    if lst is None:
        return default
    if isinstance(lst, collections.abc.Iterable) and not isinstance(lst, (str, bytes)):
        for item in lst:
            return item
        return default
    return None


def get_if_exists(obj: Any, key: str | None, default: T = None) -> Any | T:
    if obj is None or key is None:
        return default

    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        else:
            return default

    attr = getattr(obj, key, default)
    return attr


def list_is_optional(obj: list[T] | Any) -> T | list[T] | Any | None:
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


def list_without_nones(lst: Iterable[T | None]) -> list[T]:
    return [e for e in lst if e is not None]


def none_if_empty(obj: T) -> T | None:
    if isinstance(obj, list) and len(obj) == 0:
        return None
    if isinstance(obj, dict) and not obj:
        return None
    return obj


def set_if_not_none(obj: T, value: Any, key: str | None = None) -> T:
    if value is None:
        return obj

    if key is None and isinstance(obj, list):
        obj.append(value)

    if key is not None and isinstance(obj, dict):
        obj[key] = value

    return obj
