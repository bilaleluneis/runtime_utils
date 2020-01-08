from unittest import TestCase, main
from .functions import *

__author__ = "Bilal El Uneis"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com"


class RunTimeCheckedDecoratorTests(TestCase):

    def test_no_param_function(self) -> None:
        func_1()
        self.assert_(True)  # if we do not get here , then func_1 call threw exception


if __name__ == '__main__':
    main()
