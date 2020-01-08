from typing import Callable, Any, TypeVar, cast, get_type_hints, Tuple, Type, List
from functools import wraps
from runtime.util.typing._runtime_type_checker import _check_types, _ParameterInfo

__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com, foundwonder@gmail.com"

FuncType = Callable[..., Any]
F = TypeVar('F', bound=FuncType)


def runtimechecked(function: F) -> F:
    # if not isfunction(function) and not ismethod(function) and not is_callable_type(function):
    #     raise TypeError(f"runtimechecked(function: F): {function} is not a Function or Method !")

    @wraps(function)
    def perform_type_checks(*args: Any, **kwargs: Any) -> F:
        params_value = [param_value for param_value in args]
        type_hints_1 = get_type_hints(function)
        if len(params_value):
            type_hints = get_type_hints(function)
            type_hints.pop('return', None)  # remove the return type from hints for now
            type_hints_list = cast(List[Tuple[str, Type[Any]]], list(type_hints.items()))
            params_info = [_ParameterInfo(name=func_sig[0], expected_type=func_sig[1], actual_value=value)
                           for func_sig, value in zip(type_hints_list, params_value)]
            result = _check_types(params_info)
            if not result.passed:
                raise TypeError([f"TYPE ERROR: {error}\n" for error in result.details])
        return cast(F, function(*args, **kwargs))

    return cast(F, perform_type_checks)
