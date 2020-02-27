from typing import Generic, TypeVar
from unittest import TestCase, main
from runtime.util.typing.decorator import TypeHintsReqNotMetError, runtimechecked

__author__ = "Bilal El Uneis"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com"


class RunTimeCheckedDecoratorTests(TestCase):

    """(1) Tests to validate proper location usage of @"""
    def test_valid_when_used_with_function(self) -> None:
        try:
            @runtimechecked
            def func() -> bool:
                return True
        except TypeError:
            self.fail()

    def test_not_valid_when_used_with_class(self) -> None:
        with self.assertRaises(TypeError):
            @runtimechecked
            class Aclass:
                ...

    def test_valid_when_used_with_class_method(self) -> None:
        try:
            class ClassWithMethods:
                @runtimechecked
                def name(self, new_name: str) -> None:
                    ...
        except TypeError:
            self.fail()

    def test_valid_when_used_with_class_property(self) -> None:
        try:
            class ClassWithProp:
                def __init__(self) -> None:
                    self.__count: int = 0

                @property
                def count(self) -> int:
                    return self.__count

                @count.setter
                @runtimechecked
                def count(self, new_count: int) -> None:
                    self.__count = new_count
        except TypeError:
            self.fail()

    def test_function_is_type_hinted(self) -> None:

        # raises TypeHintsReqNotMetError, because param c=0.0 is not hinted
        with self.assertRaises(TypeHintsReqNotMetError):
            @runtimechecked
            def m1(a: int, b: str, c=0.0) -> bool:
                return True

        # raises TypeHintsReqNotMetError because, function return is not hinted
        with self.assertRaises(TypeHintsReqNotMetError):
            @runtimechecked
            def m2(a: int, b: str):
                return True

        try:
            @runtimechecked
            def m3(a: bool) -> bool:
                return a
        except TypeHintsReqNotMetError:
            self.fail()

    """(2) Tests of @ enforcing types when decorated function is called"""
    def test_function_called_with_correct_types(self) -> None:

        type_ = TypeVar('type_')

        class G(Generic[type_]):
            def __init__(self, value: type_):
                self.__value = value

        @runtimechecked
        def func(i: int, s: str, g: G[int], b: bool = False) -> float:
            return float(i)

        try:
            func(1, "duh", G[int](2))
        except TypeError:
            self.fail()

    def test_function_called_with_incorrect_types(self) -> None:

        type_ = TypeVar('type_')

        class G(Generic[type_]):
            def __init__(self, value: type_):
                self.__value = value

        @runtimechecked
        def func(i: int, s: str, g: G[int], b: bool = False) -> float:
            return float(i)

        with self.assertRaises(TypeError):
            func(1, "duh", G[float](2.0))


if __name__ == '__main__':
    main()
