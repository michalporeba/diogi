from collections.abc import Callable, Iterable
from typing import Any, TypeVar

import diogi.functions as f

T = TypeVar("T")


def always_a_list(func: Callable[..., Any]) -> Callable[..., list[Any]]:
    def wrapper(*args, **kwargs):
        return f.always_a_list(func(*args, **kwargs))

    return wrapper


def first_or_default(
    default: T,
) -> Callable[[Callable[..., Any]], Callable[..., T | Any | None]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., T | Any | None]:
        def wrapper(*args, **kwargs):
            return f.first_or_default(func(*args, **kwargs), default)

        return wrapper

    return decorator


def list_is_optional(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        return f.list_is_optional(func(*args, **kwargs))

    return wrapper


def list_without_nones(
    func: Callable[..., Iterable[T | None]],
) -> Callable[..., list[T]]:
    def wrapper(*args, **kwargs):
        return f.list_without_nones(func(*args, **kwargs))

    return wrapper
