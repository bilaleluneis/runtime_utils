from inspect import isfunction, Signature, Parameter, BoundArguments
from typing import NamedTuple, Type, Any, Callable, TypeVar, Set, Iterable
from typing_inspect import get_generic_type

__author__ = "Bilal El Uneis"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com"

_A = TypeVar('_A')  # short for Any Type
_FuncType = Callable[..., Any]
_F = TypeVar('_F', bound=_FuncType)
_RuntimeCheckResult = NamedTuple('_RuntimeCheckResult', details=Iterable[str], passed=bool)
_ParameterInfo = NamedTuple('_ParameterInfo', name=str, expected_type=Type[Any], actual_value=Any)
_TypeHintChecks = NamedTuple('_TypeHintChecks', errors=Set[str], passed=bool)
_non_hinted_params: Set[str] = {'self', 'cls'}


def _is_function_type(decorated_object: Any) -> bool:
    """ written this way for easier debugging"""
    is_function: bool = isfunction(decorated_object)
    return is_function


def _verify_uses_type_hints(func_signature: Signature) -> _TypeHintChecks:
    errors: Set[str] = set()
    if func_signature.return_annotation == Signature.empty:
        errors.add("return type is not defined!")
    params = func_signature.parameters
    for key in params:
        param: Parameter = params[key]
        if param.annotation == Parameter.empty and param.name not in _non_hinted_params:
            errors.add(f"{param.name} is not type hinted!")
    return _TypeHintChecks(errors, len(errors) == 0)


def _check_types(func_arguments: BoundArguments) -> _RuntimeCheckResult:
    error_details: Set[str] = set()
    checks_passed: bool = True
    func_sig: Signature = func_arguments.signature
    func_params = func_sig.parameters
    for func_param_key in func_params:
        func_param: Parameter = func_params[func_param_key]
        param_type: Type[_A] = func_param.annotation
        param_actual_value = func_arguments.arguments[func_param_key]
        value_type: Type[_A] = get_generic_type(param_actual_value)
        if value_type != param_type:
            checks_passed = False
            error = f" ERROR: param {func_param_key} expected {param_type} got {value_type} instead!"
            error_details.add(error)
    return _RuntimeCheckResult(details=error_details, passed=checks_passed)
