from runtime.util.typing.decorator import runtimechecked
from typing import Generic, Callable, Any, TypeVar

__author__ = "Bilal El Uneis"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com"


@runtimechecked
class AClass:
    ...


@runtimechecked
class CallableType(Callable[..., Any]):
    ...


class ClassWithMethods:

    @property
    def name(self) -> str:
        return "ClassWithMethods"

    @runtimechecked
    @name.setter
    def name(self, new_name: str) -> None:
        pass

    @runtimechecked
    def set_name(self, new_name: str) -> None:
        self.name = new_name


_Type = TypeVar('_Type')


class GenericType(Generic[_Type]):
    def __init__(self, value_: _Type):
        self.__value: _Type = value_

    @property
    def value(self) -> _Type:
        return self.__value
