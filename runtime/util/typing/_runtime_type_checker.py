from typing import NamedTuple, List, Type, Any

__author__ = "Bilal El Uneis"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com"

_RuntimeCheckResult = NamedTuple('_RuntimeCheckResult', details=List[str], passed=bool)
_ParameterInfo = NamedTuple('_ParameterInfo', name=str, expected_type=Type[Any], actual_value=Any)


def _check_types(param_info_list: List[_ParameterInfo]) -> _RuntimeCheckResult:
    error_details: List[str] = []
    checks_passed: bool = True
    for param_info in param_info_list:
        pass
    return _RuntimeCheckResult(details=error_details, passed=checks_passed)
