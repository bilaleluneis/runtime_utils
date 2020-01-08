from runtime.util.typing.decorator import runtimechecked
from .classes import GenericType
from typing import Tuple

__author__ = "Bilal El Uneis"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com"


@runtimechecked
def func_1() -> None:
    """ function with no parameters and returns nothing"""
    return


@runtimechecked
def simple_func(name: str = "no", some_generic: GenericType[int] = GenericType[int](1)) -> Tuple[str, int]:
    return name, some_generic.value
