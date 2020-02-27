__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Feb 2020"
__email__ = "bilaleluneis@gmail.com, foundwonder@gmail.com"

from typing import Set, Type
from unittest import TestSuite, TestLoader, TextTestRunner, TestCase
from typing_extensions import Final

from runtime.util.meta.tests.frozen_tests import FrozenClassTests
from runtime.util.typing.tests.runtimechecked_tests import RunTimeCheckedDecoratorTests

TestCaseType: Type[TestCase] = Type[TestCase]
TestCaseSet: Set[TestCaseType] = Set[TestCaseType]
TESTS: Final[TestCaseSet] = {FrozenClassTests,
                             RunTimeCheckedDecoratorTests}


def init_test_suite() -> TestSuite:
    loader = TestLoader()
    suite = TestSuite()
    for test in TESTS:
        suite.addTests(loader.loadTestsFromTestCase(test))
    return suite


if __name__ == '__main__':
    runner = TextTestRunner(verbosity=3)
    tests = init_test_suite()
    runner.run(tests)
