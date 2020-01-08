from typing import Generic, TypeVar
from runtime.util.meta.decorator import frozen

__author__ = "Bilal El Uneis"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com"

TestType = TypeVar("TestType")


class CanAddAttribs:
    ...


@frozen
class CantAddAttribs:
    def __init__(self) -> None:
        self.__a: str = ''

    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, new_value: str) -> None:
        self.__a = new_value


@frozen
class GenericCantAddAttribs(Generic[TestType]):
    def __init__(self) -> None:
        self.__a: str = ''

    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, new_value: str) -> None:
        self.__a = new_value
