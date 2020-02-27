from inspect import signature, Signature, BoundArguments
from typing import Any, cast
from functools import wraps
from runtime.util.typing._runtime_type_checker import _F, _TypeHintChecks, _RuntimeCheckResult
from runtime.util.typing._runtime_type_checker import _verify_uses_type_hints, _is_function_type
from runtime.util.typing._runtime_type_checker import _check_types


__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Jan 2020"
__email__ = "bilaleluneis@gmail.com, foundwonder@gmail.com"


class TypeHintsReqNotMetError(Exception):
    ...


def runtimechecked(function: _F) -> _F:
    if not _is_function_type(function):
        raise TypeError("@runtimechecked can only be used with function types")
    func_signature: Signature = signature(function)
    type_hint_result: _TypeHintChecks = _verify_uses_type_hints(func_signature)
    if not type_hint_result.passed:
        raise TypeHintsReqNotMetError(str([f"{error}\n" for error in type_hint_result.errors]))

    @wraps(function)
    def __perform_type_checks(*args: Any, **kwargs: Any) -> _F:
        arguments: BoundArguments = func_signature.bind(*args, **kwargs)
        arguments.apply_defaults()
        result: _RuntimeCheckResult = _check_types(arguments)
        if not result.passed:
            raise TypeError(str(result.details))
        return cast(_F, function(*args, **kwargs))

    return cast(_F, __perform_type_checks)
