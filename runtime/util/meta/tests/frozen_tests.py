from unittest import TestCase, main
from runtime.util.meta.decorator import frozen  # type: ignore
from typing import Generic, TypeVar

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


class FrozenClassTests(TestCase):

    def setUp(self) -> None:
        self._can_add_attribs: CanAddAttribs = CanAddAttribs()
        self._cant_add_attribs: CantAddAttribs = CantAddAttribs()
        self._generic_cant_add_attribs: GenericCantAddAttribs[str] = GenericCantAddAttribs[str]()

    def test_non_frozen_behaviour(self) -> None:
        self._can_add_attribs.a = 'A'
        self.assertEqual(self._can_add_attribs.a, 'A')

    def test_frozen_behaviour(self) -> None:
        self._cant_add_attribs.a = 'A'
        self.assertEqual(self._cant_add_attribs.a, 'A')
        with self.assertRaises(AttributeError):
            self._cant_add_attribs.b = 'B'

    def test_frozen_generic_behaviour(self) -> None:
        self._generic_cant_add_attribs.a = 'A'
        self.assertEqual(self._generic_cant_add_attribs.a, 'A')
        with self.assertRaises(AttributeError):
            self._generic_cant_add_attribs.b = 'B'


if __name__ == '__main__':
    main()
