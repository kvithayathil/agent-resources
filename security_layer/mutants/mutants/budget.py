from security_layer.models import BudgetLimits, BudgetState

_DEFAULT_COST_PER_1K_TOKENS: dict[str, float] = {
    "default": 0.03,
    "gpt-4": 0.03,
    "gpt-4o": 0.005,
    "gpt-3.5-turbo": 0.002,
    "claude-3-opus": 0.015,
    "claude-3-sonnet": 0.003,
}
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    args = [orig, mutants, call_args, call_kwargs, self_arg]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__mutmut_trampoline__mutmut_orig, x__mutmut_trampoline__mutmut_mutants, args, kwargs, None)


def x__mutmut_trampoline__mutmut_orig(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_1(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = None # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_2(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['XXMUTANT_UNDER_TESTXX'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_3(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['mutant_under_test'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_4(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test != 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_5(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'XXfailXX': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_6(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'FAIL': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_7(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException(None)       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_8(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('XXFailed programmaticallyXX')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_9(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_10(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('FAILED PROGRAMMATICALLY')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_11(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test != 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_12(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'XXstatsXX': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_13(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'STATS': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_14(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(None) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_15(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' - orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_16(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ - '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_17(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + 'XX.XX' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_18(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = None # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_19(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(**call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_20(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, ) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_21(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = None # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_22(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ - '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_23(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' - orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_24(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ - '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_25(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + 'XX.XX' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_26(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + 'XX__mutmut_XX' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_27(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__MUTMUT_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_28(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_29(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(None): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_30(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = None # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_31(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(**call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_32(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, ) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_33(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = None # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_34(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition(None)[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_35(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.partition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_36(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('XX.XX')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_37(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[+1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_38(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-2] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_39(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_40(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = None # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_41(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](None, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_42(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_43(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_44(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, ) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_45(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = None # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_46(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](**call_kwargs) # type: ignore
    return result # type: ignore


def x__mutmut_trampoline__mutmut_47(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, ) # type: ignore
    return result # type: ignore

x__mutmut_trampoline__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__mutmut_trampoline__mutmut_1': x__mutmut_trampoline__mutmut_1, 
    'x__mutmut_trampoline__mutmut_2': x__mutmut_trampoline__mutmut_2, 
    'x__mutmut_trampoline__mutmut_3': x__mutmut_trampoline__mutmut_3, 
    'x__mutmut_trampoline__mutmut_4': x__mutmut_trampoline__mutmut_4, 
    'x__mutmut_trampoline__mutmut_5': x__mutmut_trampoline__mutmut_5, 
    'x__mutmut_trampoline__mutmut_6': x__mutmut_trampoline__mutmut_6, 
    'x__mutmut_trampoline__mutmut_7': x__mutmut_trampoline__mutmut_7, 
    'x__mutmut_trampoline__mutmut_8': x__mutmut_trampoline__mutmut_8, 
    'x__mutmut_trampoline__mutmut_9': x__mutmut_trampoline__mutmut_9, 
    'x__mutmut_trampoline__mutmut_10': x__mutmut_trampoline__mutmut_10, 
    'x__mutmut_trampoline__mutmut_11': x__mutmut_trampoline__mutmut_11, 
    'x__mutmut_trampoline__mutmut_12': x__mutmut_trampoline__mutmut_12, 
    'x__mutmut_trampoline__mutmut_13': x__mutmut_trampoline__mutmut_13, 
    'x__mutmut_trampoline__mutmut_14': x__mutmut_trampoline__mutmut_14, 
    'x__mutmut_trampoline__mutmut_15': x__mutmut_trampoline__mutmut_15, 
    'x__mutmut_trampoline__mutmut_16': x__mutmut_trampoline__mutmut_16, 
    'x__mutmut_trampoline__mutmut_17': x__mutmut_trampoline__mutmut_17, 
    'x__mutmut_trampoline__mutmut_18': x__mutmut_trampoline__mutmut_18, 
    'x__mutmut_trampoline__mutmut_19': x__mutmut_trampoline__mutmut_19, 
    'x__mutmut_trampoline__mutmut_20': x__mutmut_trampoline__mutmut_20, 
    'x__mutmut_trampoline__mutmut_21': x__mutmut_trampoline__mutmut_21, 
    'x__mutmut_trampoline__mutmut_22': x__mutmut_trampoline__mutmut_22, 
    'x__mutmut_trampoline__mutmut_23': x__mutmut_trampoline__mutmut_23, 
    'x__mutmut_trampoline__mutmut_24': x__mutmut_trampoline__mutmut_24, 
    'x__mutmut_trampoline__mutmut_25': x__mutmut_trampoline__mutmut_25, 
    'x__mutmut_trampoline__mutmut_26': x__mutmut_trampoline__mutmut_26, 
    'x__mutmut_trampoline__mutmut_27': x__mutmut_trampoline__mutmut_27, 
    'x__mutmut_trampoline__mutmut_28': x__mutmut_trampoline__mutmut_28, 
    'x__mutmut_trampoline__mutmut_29': x__mutmut_trampoline__mutmut_29, 
    'x__mutmut_trampoline__mutmut_30': x__mutmut_trampoline__mutmut_30, 
    'x__mutmut_trampoline__mutmut_31': x__mutmut_trampoline__mutmut_31, 
    'x__mutmut_trampoline__mutmut_32': x__mutmut_trampoline__mutmut_32, 
    'x__mutmut_trampoline__mutmut_33': x__mutmut_trampoline__mutmut_33, 
    'x__mutmut_trampoline__mutmut_34': x__mutmut_trampoline__mutmut_34, 
    'x__mutmut_trampoline__mutmut_35': x__mutmut_trampoline__mutmut_35, 
    'x__mutmut_trampoline__mutmut_36': x__mutmut_trampoline__mutmut_36, 
    'x__mutmut_trampoline__mutmut_37': x__mutmut_trampoline__mutmut_37, 
    'x__mutmut_trampoline__mutmut_38': x__mutmut_trampoline__mutmut_38, 
    'x__mutmut_trampoline__mutmut_39': x__mutmut_trampoline__mutmut_39, 
    'x__mutmut_trampoline__mutmut_40': x__mutmut_trampoline__mutmut_40, 
    'x__mutmut_trampoline__mutmut_41': x__mutmut_trampoline__mutmut_41, 
    'x__mutmut_trampoline__mutmut_42': x__mutmut_trampoline__mutmut_42, 
    'x__mutmut_trampoline__mutmut_43': x__mutmut_trampoline__mutmut_43, 
    'x__mutmut_trampoline__mutmut_44': x__mutmut_trampoline__mutmut_44, 
    'x__mutmut_trampoline__mutmut_45': x__mutmut_trampoline__mutmut_45, 
    'x__mutmut_trampoline__mutmut_46': x__mutmut_trampoline__mutmut_46, 
    'x__mutmut_trampoline__mutmut_47': x__mutmut_trampoline__mutmut_47
}
x__mutmut_trampoline__mutmut_orig.__name__ = 'x__mutmut_trampoline'


def check_budget(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, args, kwargs, None)


def x_check_budget__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, args, kwargs, None)


def x_check_budget__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, args, kwargs, None)


def x_check_budget__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, args, kwargs, None)


def x_check_budget__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_check_budget__mutmut_mutants, args, kwargs, None)


def x_check_budget__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, None, args, kwargs, None)


def x_check_budget__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, None, kwargs, None)


def x_check_budget__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, args, None, None)


def x_check_budget__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_mutants, args, kwargs, None)


def x_check_budget__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, args, kwargs, None)


def x_check_budget__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, kwargs, None)


def x_check_budget__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, args, None)


def x_check_budget__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_budget__mutmut_orig, x_check_budget__mutmut_mutants, args, kwargs, )

x_check_budget__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_budget__mutmut_1': x_check_budget__mutmut_1, 
    'x_check_budget__mutmut_2': x_check_budget__mutmut_2, 
    'x_check_budget__mutmut_3': x_check_budget__mutmut_3, 
    'x_check_budget__mutmut_4': x_check_budget__mutmut_4, 
    'x_check_budget__mutmut_5': x_check_budget__mutmut_5, 
    'x_check_budget__mutmut_6': x_check_budget__mutmut_6, 
    'x_check_budget__mutmut_7': x_check_budget__mutmut_7, 
    'x_check_budget__mutmut_8': x_check_budget__mutmut_8, 
    'x_check_budget__mutmut_9': x_check_budget__mutmut_9, 
    'x_check_budget__mutmut_10': x_check_budget__mutmut_10, 
    'x_check_budget__mutmut_11': x_check_budget__mutmut_11
}
x_check_budget__mutmut_orig.__name__ = 'x_check_budget'


def x_check_budget__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_orig__mutmut_orig, x_x_check_budget__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_orig__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_orig__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_orig__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_orig__mutmut_1': x_x_check_budget__mutmut_orig__mutmut_1, 
    'x_x_check_budget__mutmut_orig__mutmut_2': x_x_check_budget__mutmut_orig__mutmut_2, 
    'x_x_check_budget__mutmut_orig__mutmut_3': x_x_check_budget__mutmut_orig__mutmut_3, 
    'x_x_check_budget__mutmut_orig__mutmut_4': x_x_check_budget__mutmut_orig__mutmut_4, 
    'x_x_check_budget__mutmut_orig__mutmut_5': x_x_check_budget__mutmut_orig__mutmut_5, 
    'x_x_check_budget__mutmut_orig__mutmut_6': x_x_check_budget__mutmut_orig__mutmut_6, 
    'x_x_check_budget__mutmut_orig__mutmut_7': x_x_check_budget__mutmut_orig__mutmut_7, 
    'x_x_check_budget__mutmut_orig__mutmut_8': x_x_check_budget__mutmut_orig__mutmut_8, 
    'x_x_check_budget__mutmut_orig__mutmut_9': x_x_check_budget__mutmut_orig__mutmut_9, 
    'x_x_check_budget__mutmut_orig__mutmut_10': x_x_check_budget__mutmut_orig__mutmut_10, 
    'x_x_check_budget__mutmut_orig__mutmut_11': x_x_check_budget__mutmut_orig__mutmut_11, 
    'x_x_check_budget__mutmut_orig__mutmut_12': x_x_check_budget__mutmut_orig__mutmut_12, 
    'x_x_check_budget__mutmut_orig__mutmut_13': x_x_check_budget__mutmut_orig__mutmut_13, 
    'x_x_check_budget__mutmut_orig__mutmut_14': x_x_check_budget__mutmut_orig__mutmut_14, 
    'x_x_check_budget__mutmut_orig__mutmut_15': x_x_check_budget__mutmut_orig__mutmut_15, 
    'x_x_check_budget__mutmut_orig__mutmut_16': x_x_check_budget__mutmut_orig__mutmut_16, 
    'x_x_check_budget__mutmut_orig__mutmut_17': x_x_check_budget__mutmut_orig__mutmut_17, 
    'x_x_check_budget__mutmut_orig__mutmut_18': x_x_check_budget__mutmut_orig__mutmut_18, 
    'x_x_check_budget__mutmut_orig__mutmut_19': x_x_check_budget__mutmut_orig__mutmut_19, 
    'x_x_check_budget__mutmut_orig__mutmut_20': x_x_check_budget__mutmut_orig__mutmut_20, 
    'x_x_check_budget__mutmut_orig__mutmut_21': x_x_check_budget__mutmut_orig__mutmut_21, 
    'x_x_check_budget__mutmut_orig__mutmut_22': x_x_check_budget__mutmut_orig__mutmut_22
}
x_x_check_budget__mutmut_orig__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_orig'


def x_check_budget__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_1__mutmut_orig, x_x_check_budget__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_1__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_1__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_1__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_1__mutmut_1': x_x_check_budget__mutmut_1__mutmut_1, 
    'x_x_check_budget__mutmut_1__mutmut_2': x_x_check_budget__mutmut_1__mutmut_2, 
    'x_x_check_budget__mutmut_1__mutmut_3': x_x_check_budget__mutmut_1__mutmut_3, 
    'x_x_check_budget__mutmut_1__mutmut_4': x_x_check_budget__mutmut_1__mutmut_4, 
    'x_x_check_budget__mutmut_1__mutmut_5': x_x_check_budget__mutmut_1__mutmut_5, 
    'x_x_check_budget__mutmut_1__mutmut_6': x_x_check_budget__mutmut_1__mutmut_6, 
    'x_x_check_budget__mutmut_1__mutmut_7': x_x_check_budget__mutmut_1__mutmut_7, 
    'x_x_check_budget__mutmut_1__mutmut_8': x_x_check_budget__mutmut_1__mutmut_8, 
    'x_x_check_budget__mutmut_1__mutmut_9': x_x_check_budget__mutmut_1__mutmut_9, 
    'x_x_check_budget__mutmut_1__mutmut_10': x_x_check_budget__mutmut_1__mutmut_10, 
    'x_x_check_budget__mutmut_1__mutmut_11': x_x_check_budget__mutmut_1__mutmut_11, 
    'x_x_check_budget__mutmut_1__mutmut_12': x_x_check_budget__mutmut_1__mutmut_12, 
    'x_x_check_budget__mutmut_1__mutmut_13': x_x_check_budget__mutmut_1__mutmut_13, 
    'x_x_check_budget__mutmut_1__mutmut_14': x_x_check_budget__mutmut_1__mutmut_14, 
    'x_x_check_budget__mutmut_1__mutmut_15': x_x_check_budget__mutmut_1__mutmut_15, 
    'x_x_check_budget__mutmut_1__mutmut_16': x_x_check_budget__mutmut_1__mutmut_16, 
    'x_x_check_budget__mutmut_1__mutmut_17': x_x_check_budget__mutmut_1__mutmut_17, 
    'x_x_check_budget__mutmut_1__mutmut_18': x_x_check_budget__mutmut_1__mutmut_18, 
    'x_x_check_budget__mutmut_1__mutmut_19': x_x_check_budget__mutmut_1__mutmut_19, 
    'x_x_check_budget__mutmut_1__mutmut_20': x_x_check_budget__mutmut_1__mutmut_20, 
    'x_x_check_budget__mutmut_1__mutmut_21': x_x_check_budget__mutmut_1__mutmut_21, 
    'x_x_check_budget__mutmut_1__mutmut_22': x_x_check_budget__mutmut_1__mutmut_22
}
x_x_check_budget__mutmut_1__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_1'


def x_check_budget__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_2__mutmut_orig, x_x_check_budget__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_2__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_2__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_2__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_2__mutmut_1': x_x_check_budget__mutmut_2__mutmut_1, 
    'x_x_check_budget__mutmut_2__mutmut_2': x_x_check_budget__mutmut_2__mutmut_2, 
    'x_x_check_budget__mutmut_2__mutmut_3': x_x_check_budget__mutmut_2__mutmut_3, 
    'x_x_check_budget__mutmut_2__mutmut_4': x_x_check_budget__mutmut_2__mutmut_4, 
    'x_x_check_budget__mutmut_2__mutmut_5': x_x_check_budget__mutmut_2__mutmut_5, 
    'x_x_check_budget__mutmut_2__mutmut_6': x_x_check_budget__mutmut_2__mutmut_6, 
    'x_x_check_budget__mutmut_2__mutmut_7': x_x_check_budget__mutmut_2__mutmut_7, 
    'x_x_check_budget__mutmut_2__mutmut_8': x_x_check_budget__mutmut_2__mutmut_8, 
    'x_x_check_budget__mutmut_2__mutmut_9': x_x_check_budget__mutmut_2__mutmut_9, 
    'x_x_check_budget__mutmut_2__mutmut_10': x_x_check_budget__mutmut_2__mutmut_10, 
    'x_x_check_budget__mutmut_2__mutmut_11': x_x_check_budget__mutmut_2__mutmut_11, 
    'x_x_check_budget__mutmut_2__mutmut_12': x_x_check_budget__mutmut_2__mutmut_12, 
    'x_x_check_budget__mutmut_2__mutmut_13': x_x_check_budget__mutmut_2__mutmut_13, 
    'x_x_check_budget__mutmut_2__mutmut_14': x_x_check_budget__mutmut_2__mutmut_14, 
    'x_x_check_budget__mutmut_2__mutmut_15': x_x_check_budget__mutmut_2__mutmut_15, 
    'x_x_check_budget__mutmut_2__mutmut_16': x_x_check_budget__mutmut_2__mutmut_16, 
    'x_x_check_budget__mutmut_2__mutmut_17': x_x_check_budget__mutmut_2__mutmut_17, 
    'x_x_check_budget__mutmut_2__mutmut_18': x_x_check_budget__mutmut_2__mutmut_18, 
    'x_x_check_budget__mutmut_2__mutmut_19': x_x_check_budget__mutmut_2__mutmut_19, 
    'x_x_check_budget__mutmut_2__mutmut_20': x_x_check_budget__mutmut_2__mutmut_20, 
    'x_x_check_budget__mutmut_2__mutmut_21': x_x_check_budget__mutmut_2__mutmut_21, 
    'x_x_check_budget__mutmut_2__mutmut_22': x_x_check_budget__mutmut_2__mutmut_22
}
x_x_check_budget__mutmut_2__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_2'


def x_check_budget__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_3__mutmut_orig, x_x_check_budget__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_3__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXXXToken budget exceededXXXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "xxtoken budget exceededxx"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXTOKEN BUDGET EXCEEDEDXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_3__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_3__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_3__mutmut_1': x_x_check_budget__mutmut_3__mutmut_1, 
    'x_x_check_budget__mutmut_3__mutmut_2': x_x_check_budget__mutmut_3__mutmut_2, 
    'x_x_check_budget__mutmut_3__mutmut_3': x_x_check_budget__mutmut_3__mutmut_3, 
    'x_x_check_budget__mutmut_3__mutmut_4': x_x_check_budget__mutmut_3__mutmut_4, 
    'x_x_check_budget__mutmut_3__mutmut_5': x_x_check_budget__mutmut_3__mutmut_5, 
    'x_x_check_budget__mutmut_3__mutmut_6': x_x_check_budget__mutmut_3__mutmut_6, 
    'x_x_check_budget__mutmut_3__mutmut_7': x_x_check_budget__mutmut_3__mutmut_7, 
    'x_x_check_budget__mutmut_3__mutmut_8': x_x_check_budget__mutmut_3__mutmut_8, 
    'x_x_check_budget__mutmut_3__mutmut_9': x_x_check_budget__mutmut_3__mutmut_9, 
    'x_x_check_budget__mutmut_3__mutmut_10': x_x_check_budget__mutmut_3__mutmut_10, 
    'x_x_check_budget__mutmut_3__mutmut_11': x_x_check_budget__mutmut_3__mutmut_11, 
    'x_x_check_budget__mutmut_3__mutmut_12': x_x_check_budget__mutmut_3__mutmut_12, 
    'x_x_check_budget__mutmut_3__mutmut_13': x_x_check_budget__mutmut_3__mutmut_13, 
    'x_x_check_budget__mutmut_3__mutmut_14': x_x_check_budget__mutmut_3__mutmut_14, 
    'x_x_check_budget__mutmut_3__mutmut_15': x_x_check_budget__mutmut_3__mutmut_15, 
    'x_x_check_budget__mutmut_3__mutmut_16': x_x_check_budget__mutmut_3__mutmut_16, 
    'x_x_check_budget__mutmut_3__mutmut_17': x_x_check_budget__mutmut_3__mutmut_17, 
    'x_x_check_budget__mutmut_3__mutmut_18': x_x_check_budget__mutmut_3__mutmut_18, 
    'x_x_check_budget__mutmut_3__mutmut_19': x_x_check_budget__mutmut_3__mutmut_19, 
    'x_x_check_budget__mutmut_3__mutmut_20': x_x_check_budget__mutmut_3__mutmut_20, 
    'x_x_check_budget__mutmut_3__mutmut_21': x_x_check_budget__mutmut_3__mutmut_21, 
    'x_x_check_budget__mutmut_3__mutmut_22': x_x_check_budget__mutmut_3__mutmut_22
}
x_x_check_budget__mutmut_3__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_3'


def x_check_budget__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_4__mutmut_orig, x_x_check_budget__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_4__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXtoken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_4__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_4__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_4__mutmut_1': x_x_check_budget__mutmut_4__mutmut_1, 
    'x_x_check_budget__mutmut_4__mutmut_2': x_x_check_budget__mutmut_4__mutmut_2, 
    'x_x_check_budget__mutmut_4__mutmut_3': x_x_check_budget__mutmut_4__mutmut_3, 
    'x_x_check_budget__mutmut_4__mutmut_4': x_x_check_budget__mutmut_4__mutmut_4, 
    'x_x_check_budget__mutmut_4__mutmut_5': x_x_check_budget__mutmut_4__mutmut_5, 
    'x_x_check_budget__mutmut_4__mutmut_6': x_x_check_budget__mutmut_4__mutmut_6, 
    'x_x_check_budget__mutmut_4__mutmut_7': x_x_check_budget__mutmut_4__mutmut_7, 
    'x_x_check_budget__mutmut_4__mutmut_8': x_x_check_budget__mutmut_4__mutmut_8, 
    'x_x_check_budget__mutmut_4__mutmut_9': x_x_check_budget__mutmut_4__mutmut_9, 
    'x_x_check_budget__mutmut_4__mutmut_10': x_x_check_budget__mutmut_4__mutmut_10, 
    'x_x_check_budget__mutmut_4__mutmut_11': x_x_check_budget__mutmut_4__mutmut_11, 
    'x_x_check_budget__mutmut_4__mutmut_12': x_x_check_budget__mutmut_4__mutmut_12, 
    'x_x_check_budget__mutmut_4__mutmut_13': x_x_check_budget__mutmut_4__mutmut_13, 
    'x_x_check_budget__mutmut_4__mutmut_14': x_x_check_budget__mutmut_4__mutmut_14, 
    'x_x_check_budget__mutmut_4__mutmut_15': x_x_check_budget__mutmut_4__mutmut_15, 
    'x_x_check_budget__mutmut_4__mutmut_16': x_x_check_budget__mutmut_4__mutmut_16, 
    'x_x_check_budget__mutmut_4__mutmut_17': x_x_check_budget__mutmut_4__mutmut_17, 
    'x_x_check_budget__mutmut_4__mutmut_18': x_x_check_budget__mutmut_4__mutmut_18, 
    'x_x_check_budget__mutmut_4__mutmut_19': x_x_check_budget__mutmut_4__mutmut_19, 
    'x_x_check_budget__mutmut_4__mutmut_20': x_x_check_budget__mutmut_4__mutmut_20, 
    'x_x_check_budget__mutmut_4__mutmut_21': x_x_check_budget__mutmut_4__mutmut_21
}
x_x_check_budget__mutmut_4__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_4'


def x_check_budget__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_5__mutmut_orig, x_x_check_budget__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_5__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXTOKEN BUDGET EXCEEDEDXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_5__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_5__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_5__mutmut_1': x_x_check_budget__mutmut_5__mutmut_1, 
    'x_x_check_budget__mutmut_5__mutmut_2': x_x_check_budget__mutmut_5__mutmut_2, 
    'x_x_check_budget__mutmut_5__mutmut_3': x_x_check_budget__mutmut_5__mutmut_3, 
    'x_x_check_budget__mutmut_5__mutmut_4': x_x_check_budget__mutmut_5__mutmut_4, 
    'x_x_check_budget__mutmut_5__mutmut_5': x_x_check_budget__mutmut_5__mutmut_5, 
    'x_x_check_budget__mutmut_5__mutmut_6': x_x_check_budget__mutmut_5__mutmut_6, 
    'x_x_check_budget__mutmut_5__mutmut_7': x_x_check_budget__mutmut_5__mutmut_7, 
    'x_x_check_budget__mutmut_5__mutmut_8': x_x_check_budget__mutmut_5__mutmut_8, 
    'x_x_check_budget__mutmut_5__mutmut_9': x_x_check_budget__mutmut_5__mutmut_9, 
    'x_x_check_budget__mutmut_5__mutmut_10': x_x_check_budget__mutmut_5__mutmut_10, 
    'x_x_check_budget__mutmut_5__mutmut_11': x_x_check_budget__mutmut_5__mutmut_11, 
    'x_x_check_budget__mutmut_5__mutmut_12': x_x_check_budget__mutmut_5__mutmut_12, 
    'x_x_check_budget__mutmut_5__mutmut_13': x_x_check_budget__mutmut_5__mutmut_13, 
    'x_x_check_budget__mutmut_5__mutmut_14': x_x_check_budget__mutmut_5__mutmut_14, 
    'x_x_check_budget__mutmut_5__mutmut_15': x_x_check_budget__mutmut_5__mutmut_15, 
    'x_x_check_budget__mutmut_5__mutmut_16': x_x_check_budget__mutmut_5__mutmut_16, 
    'x_x_check_budget__mutmut_5__mutmut_17': x_x_check_budget__mutmut_5__mutmut_17, 
    'x_x_check_budget__mutmut_5__mutmut_18': x_x_check_budget__mutmut_5__mutmut_18, 
    'x_x_check_budget__mutmut_5__mutmut_19': x_x_check_budget__mutmut_5__mutmut_19, 
    'x_x_check_budget__mutmut_5__mutmut_20': x_x_check_budget__mutmut_5__mutmut_20, 
    'x_x_check_budget__mutmut_5__mutmut_21': x_x_check_budget__mutmut_5__mutmut_21
}
x_x_check_budget__mutmut_5__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_5'


def x_check_budget__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_6__mutmut_orig, x_x_check_budget__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_6__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_6__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_6__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_6__mutmut_1': x_x_check_budget__mutmut_6__mutmut_1, 
    'x_x_check_budget__mutmut_6__mutmut_2': x_x_check_budget__mutmut_6__mutmut_2, 
    'x_x_check_budget__mutmut_6__mutmut_3': x_x_check_budget__mutmut_6__mutmut_3, 
    'x_x_check_budget__mutmut_6__mutmut_4': x_x_check_budget__mutmut_6__mutmut_4, 
    'x_x_check_budget__mutmut_6__mutmut_5': x_x_check_budget__mutmut_6__mutmut_5, 
    'x_x_check_budget__mutmut_6__mutmut_6': x_x_check_budget__mutmut_6__mutmut_6, 
    'x_x_check_budget__mutmut_6__mutmut_7': x_x_check_budget__mutmut_6__mutmut_7, 
    'x_x_check_budget__mutmut_6__mutmut_8': x_x_check_budget__mutmut_6__mutmut_8, 
    'x_x_check_budget__mutmut_6__mutmut_9': x_x_check_budget__mutmut_6__mutmut_9, 
    'x_x_check_budget__mutmut_6__mutmut_10': x_x_check_budget__mutmut_6__mutmut_10, 
    'x_x_check_budget__mutmut_6__mutmut_11': x_x_check_budget__mutmut_6__mutmut_11, 
    'x_x_check_budget__mutmut_6__mutmut_12': x_x_check_budget__mutmut_6__mutmut_12, 
    'x_x_check_budget__mutmut_6__mutmut_13': x_x_check_budget__mutmut_6__mutmut_13, 
    'x_x_check_budget__mutmut_6__mutmut_14': x_x_check_budget__mutmut_6__mutmut_14, 
    'x_x_check_budget__mutmut_6__mutmut_15': x_x_check_budget__mutmut_6__mutmut_15, 
    'x_x_check_budget__mutmut_6__mutmut_16': x_x_check_budget__mutmut_6__mutmut_16, 
    'x_x_check_budget__mutmut_6__mutmut_17': x_x_check_budget__mutmut_6__mutmut_17, 
    'x_x_check_budget__mutmut_6__mutmut_18': x_x_check_budget__mutmut_6__mutmut_18, 
    'x_x_check_budget__mutmut_6__mutmut_19': x_x_check_budget__mutmut_6__mutmut_19, 
    'x_x_check_budget__mutmut_6__mutmut_20': x_x_check_budget__mutmut_6__mutmut_20, 
    'x_x_check_budget__mutmut_6__mutmut_21': x_x_check_budget__mutmut_6__mutmut_21, 
    'x_x_check_budget__mutmut_6__mutmut_22': x_x_check_budget__mutmut_6__mutmut_22
}
x_x_check_budget__mutmut_6__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_6'


def x_check_budget__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_7__mutmut_orig, x_x_check_budget__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_7__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_7__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_7__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_7__mutmut_1': x_x_check_budget__mutmut_7__mutmut_1, 
    'x_x_check_budget__mutmut_7__mutmut_2': x_x_check_budget__mutmut_7__mutmut_2, 
    'x_x_check_budget__mutmut_7__mutmut_3': x_x_check_budget__mutmut_7__mutmut_3, 
    'x_x_check_budget__mutmut_7__mutmut_4': x_x_check_budget__mutmut_7__mutmut_4, 
    'x_x_check_budget__mutmut_7__mutmut_5': x_x_check_budget__mutmut_7__mutmut_5, 
    'x_x_check_budget__mutmut_7__mutmut_6': x_x_check_budget__mutmut_7__mutmut_6, 
    'x_x_check_budget__mutmut_7__mutmut_7': x_x_check_budget__mutmut_7__mutmut_7, 
    'x_x_check_budget__mutmut_7__mutmut_8': x_x_check_budget__mutmut_7__mutmut_8, 
    'x_x_check_budget__mutmut_7__mutmut_9': x_x_check_budget__mutmut_7__mutmut_9, 
    'x_x_check_budget__mutmut_7__mutmut_10': x_x_check_budget__mutmut_7__mutmut_10, 
    'x_x_check_budget__mutmut_7__mutmut_11': x_x_check_budget__mutmut_7__mutmut_11, 
    'x_x_check_budget__mutmut_7__mutmut_12': x_x_check_budget__mutmut_7__mutmut_12, 
    'x_x_check_budget__mutmut_7__mutmut_13': x_x_check_budget__mutmut_7__mutmut_13, 
    'x_x_check_budget__mutmut_7__mutmut_14': x_x_check_budget__mutmut_7__mutmut_14, 
    'x_x_check_budget__mutmut_7__mutmut_15': x_x_check_budget__mutmut_7__mutmut_15, 
    'x_x_check_budget__mutmut_7__mutmut_16': x_x_check_budget__mutmut_7__mutmut_16, 
    'x_x_check_budget__mutmut_7__mutmut_17': x_x_check_budget__mutmut_7__mutmut_17, 
    'x_x_check_budget__mutmut_7__mutmut_18': x_x_check_budget__mutmut_7__mutmut_18, 
    'x_x_check_budget__mutmut_7__mutmut_19': x_x_check_budget__mutmut_7__mutmut_19, 
    'x_x_check_budget__mutmut_7__mutmut_20': x_x_check_budget__mutmut_7__mutmut_20, 
    'x_x_check_budget__mutmut_7__mutmut_21': x_x_check_budget__mutmut_7__mutmut_21, 
    'x_x_check_budget__mutmut_7__mutmut_22': x_x_check_budget__mutmut_7__mutmut_22
}
x_x_check_budget__mutmut_7__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_7'


def x_check_budget__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_8__mutmut_orig, x_x_check_budget__mutmut_8__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_8__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXXXTool calls per turn exceededXXXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "xxtool calls per turn exceededxx"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTOOL CALLS PER TURN EXCEEDEDXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_8__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_8__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_8__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_8__mutmut_1': x_x_check_budget__mutmut_8__mutmut_1, 
    'x_x_check_budget__mutmut_8__mutmut_2': x_x_check_budget__mutmut_8__mutmut_2, 
    'x_x_check_budget__mutmut_8__mutmut_3': x_x_check_budget__mutmut_8__mutmut_3, 
    'x_x_check_budget__mutmut_8__mutmut_4': x_x_check_budget__mutmut_8__mutmut_4, 
    'x_x_check_budget__mutmut_8__mutmut_5': x_x_check_budget__mutmut_8__mutmut_5, 
    'x_x_check_budget__mutmut_8__mutmut_6': x_x_check_budget__mutmut_8__mutmut_6, 
    'x_x_check_budget__mutmut_8__mutmut_7': x_x_check_budget__mutmut_8__mutmut_7, 
    'x_x_check_budget__mutmut_8__mutmut_8': x_x_check_budget__mutmut_8__mutmut_8, 
    'x_x_check_budget__mutmut_8__mutmut_9': x_x_check_budget__mutmut_8__mutmut_9, 
    'x_x_check_budget__mutmut_8__mutmut_10': x_x_check_budget__mutmut_8__mutmut_10, 
    'x_x_check_budget__mutmut_8__mutmut_11': x_x_check_budget__mutmut_8__mutmut_11, 
    'x_x_check_budget__mutmut_8__mutmut_12': x_x_check_budget__mutmut_8__mutmut_12, 
    'x_x_check_budget__mutmut_8__mutmut_13': x_x_check_budget__mutmut_8__mutmut_13, 
    'x_x_check_budget__mutmut_8__mutmut_14': x_x_check_budget__mutmut_8__mutmut_14, 
    'x_x_check_budget__mutmut_8__mutmut_15': x_x_check_budget__mutmut_8__mutmut_15, 
    'x_x_check_budget__mutmut_8__mutmut_16': x_x_check_budget__mutmut_8__mutmut_16, 
    'x_x_check_budget__mutmut_8__mutmut_17': x_x_check_budget__mutmut_8__mutmut_17, 
    'x_x_check_budget__mutmut_8__mutmut_18': x_x_check_budget__mutmut_8__mutmut_18, 
    'x_x_check_budget__mutmut_8__mutmut_19': x_x_check_budget__mutmut_8__mutmut_19, 
    'x_x_check_budget__mutmut_8__mutmut_20': x_x_check_budget__mutmut_8__mutmut_20, 
    'x_x_check_budget__mutmut_8__mutmut_21': x_x_check_budget__mutmut_8__mutmut_21, 
    'x_x_check_budget__mutmut_8__mutmut_22': x_x_check_budget__mutmut_8__mutmut_22
}
x_x_check_budget__mutmut_8__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_8'


def x_check_budget__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_9__mutmut_orig, x_x_check_budget__mutmut_9__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_9__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXtool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_9__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_9__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_9__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_9__mutmut_1': x_x_check_budget__mutmut_9__mutmut_1, 
    'x_x_check_budget__mutmut_9__mutmut_2': x_x_check_budget__mutmut_9__mutmut_2, 
    'x_x_check_budget__mutmut_9__mutmut_3': x_x_check_budget__mutmut_9__mutmut_3, 
    'x_x_check_budget__mutmut_9__mutmut_4': x_x_check_budget__mutmut_9__mutmut_4, 
    'x_x_check_budget__mutmut_9__mutmut_5': x_x_check_budget__mutmut_9__mutmut_5, 
    'x_x_check_budget__mutmut_9__mutmut_6': x_x_check_budget__mutmut_9__mutmut_6, 
    'x_x_check_budget__mutmut_9__mutmut_7': x_x_check_budget__mutmut_9__mutmut_7, 
    'x_x_check_budget__mutmut_9__mutmut_8': x_x_check_budget__mutmut_9__mutmut_8, 
    'x_x_check_budget__mutmut_9__mutmut_9': x_x_check_budget__mutmut_9__mutmut_9, 
    'x_x_check_budget__mutmut_9__mutmut_10': x_x_check_budget__mutmut_9__mutmut_10, 
    'x_x_check_budget__mutmut_9__mutmut_11': x_x_check_budget__mutmut_9__mutmut_11, 
    'x_x_check_budget__mutmut_9__mutmut_12': x_x_check_budget__mutmut_9__mutmut_12, 
    'x_x_check_budget__mutmut_9__mutmut_13': x_x_check_budget__mutmut_9__mutmut_13, 
    'x_x_check_budget__mutmut_9__mutmut_14': x_x_check_budget__mutmut_9__mutmut_14, 
    'x_x_check_budget__mutmut_9__mutmut_15': x_x_check_budget__mutmut_9__mutmut_15, 
    'x_x_check_budget__mutmut_9__mutmut_16': x_x_check_budget__mutmut_9__mutmut_16, 
    'x_x_check_budget__mutmut_9__mutmut_17': x_x_check_budget__mutmut_9__mutmut_17, 
    'x_x_check_budget__mutmut_9__mutmut_18': x_x_check_budget__mutmut_9__mutmut_18, 
    'x_x_check_budget__mutmut_9__mutmut_19': x_x_check_budget__mutmut_9__mutmut_19, 
    'x_x_check_budget__mutmut_9__mutmut_20': x_x_check_budget__mutmut_9__mutmut_20, 
    'x_x_check_budget__mutmut_9__mutmut_21': x_x_check_budget__mutmut_9__mutmut_21
}
x_x_check_budget__mutmut_9__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_9'


def x_check_budget__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_10__mutmut_orig, x_x_check_budget__mutmut_10__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_10__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTOOL CALLS PER TURN EXCEEDEDXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_10__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_10__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_10__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_10__mutmut_1': x_x_check_budget__mutmut_10__mutmut_1, 
    'x_x_check_budget__mutmut_10__mutmut_2': x_x_check_budget__mutmut_10__mutmut_2, 
    'x_x_check_budget__mutmut_10__mutmut_3': x_x_check_budget__mutmut_10__mutmut_3, 
    'x_x_check_budget__mutmut_10__mutmut_4': x_x_check_budget__mutmut_10__mutmut_4, 
    'x_x_check_budget__mutmut_10__mutmut_5': x_x_check_budget__mutmut_10__mutmut_5, 
    'x_x_check_budget__mutmut_10__mutmut_6': x_x_check_budget__mutmut_10__mutmut_6, 
    'x_x_check_budget__mutmut_10__mutmut_7': x_x_check_budget__mutmut_10__mutmut_7, 
    'x_x_check_budget__mutmut_10__mutmut_8': x_x_check_budget__mutmut_10__mutmut_8, 
    'x_x_check_budget__mutmut_10__mutmut_9': x_x_check_budget__mutmut_10__mutmut_9, 
    'x_x_check_budget__mutmut_10__mutmut_10': x_x_check_budget__mutmut_10__mutmut_10, 
    'x_x_check_budget__mutmut_10__mutmut_11': x_x_check_budget__mutmut_10__mutmut_11, 
    'x_x_check_budget__mutmut_10__mutmut_12': x_x_check_budget__mutmut_10__mutmut_12, 
    'x_x_check_budget__mutmut_10__mutmut_13': x_x_check_budget__mutmut_10__mutmut_13, 
    'x_x_check_budget__mutmut_10__mutmut_14': x_x_check_budget__mutmut_10__mutmut_14, 
    'x_x_check_budget__mutmut_10__mutmut_15': x_x_check_budget__mutmut_10__mutmut_15, 
    'x_x_check_budget__mutmut_10__mutmut_16': x_x_check_budget__mutmut_10__mutmut_16, 
    'x_x_check_budget__mutmut_10__mutmut_17': x_x_check_budget__mutmut_10__mutmut_17, 
    'x_x_check_budget__mutmut_10__mutmut_18': x_x_check_budget__mutmut_10__mutmut_18, 
    'x_x_check_budget__mutmut_10__mutmut_19': x_x_check_budget__mutmut_10__mutmut_19, 
    'x_x_check_budget__mutmut_10__mutmut_20': x_x_check_budget__mutmut_10__mutmut_20, 
    'x_x_check_budget__mutmut_10__mutmut_21': x_x_check_budget__mutmut_10__mutmut_21
}
x_x_check_budget__mutmut_10__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_10'


def x_check_budget__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_11__mutmut_orig, x_x_check_budget__mutmut_11__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_11__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_11__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_11__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_11__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_11__mutmut_1': x_x_check_budget__mutmut_11__mutmut_1, 
    'x_x_check_budget__mutmut_11__mutmut_2': x_x_check_budget__mutmut_11__mutmut_2, 
    'x_x_check_budget__mutmut_11__mutmut_3': x_x_check_budget__mutmut_11__mutmut_3, 
    'x_x_check_budget__mutmut_11__mutmut_4': x_x_check_budget__mutmut_11__mutmut_4, 
    'x_x_check_budget__mutmut_11__mutmut_5': x_x_check_budget__mutmut_11__mutmut_5, 
    'x_x_check_budget__mutmut_11__mutmut_6': x_x_check_budget__mutmut_11__mutmut_6, 
    'x_x_check_budget__mutmut_11__mutmut_7': x_x_check_budget__mutmut_11__mutmut_7, 
    'x_x_check_budget__mutmut_11__mutmut_8': x_x_check_budget__mutmut_11__mutmut_8, 
    'x_x_check_budget__mutmut_11__mutmut_9': x_x_check_budget__mutmut_11__mutmut_9, 
    'x_x_check_budget__mutmut_11__mutmut_10': x_x_check_budget__mutmut_11__mutmut_10, 
    'x_x_check_budget__mutmut_11__mutmut_11': x_x_check_budget__mutmut_11__mutmut_11, 
    'x_x_check_budget__mutmut_11__mutmut_12': x_x_check_budget__mutmut_11__mutmut_12, 
    'x_x_check_budget__mutmut_11__mutmut_13': x_x_check_budget__mutmut_11__mutmut_13, 
    'x_x_check_budget__mutmut_11__mutmut_14': x_x_check_budget__mutmut_11__mutmut_14, 
    'x_x_check_budget__mutmut_11__mutmut_15': x_x_check_budget__mutmut_11__mutmut_15, 
    'x_x_check_budget__mutmut_11__mutmut_16': x_x_check_budget__mutmut_11__mutmut_16, 
    'x_x_check_budget__mutmut_11__mutmut_17': x_x_check_budget__mutmut_11__mutmut_17, 
    'x_x_check_budget__mutmut_11__mutmut_18': x_x_check_budget__mutmut_11__mutmut_18, 
    'x_x_check_budget__mutmut_11__mutmut_19': x_x_check_budget__mutmut_11__mutmut_19, 
    'x_x_check_budget__mutmut_11__mutmut_20': x_x_check_budget__mutmut_11__mutmut_20, 
    'x_x_check_budget__mutmut_11__mutmut_21': x_x_check_budget__mutmut_11__mutmut_21, 
    'x_x_check_budget__mutmut_11__mutmut_22': x_x_check_budget__mutmut_11__mutmut_22
}
x_x_check_budget__mutmut_11__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_11'


def x_check_budget__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_12__mutmut_orig, x_x_check_budget__mutmut_12__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_12__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_12__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_12__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_12__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_12__mutmut_1': x_x_check_budget__mutmut_12__mutmut_1, 
    'x_x_check_budget__mutmut_12__mutmut_2': x_x_check_budget__mutmut_12__mutmut_2, 
    'x_x_check_budget__mutmut_12__mutmut_3': x_x_check_budget__mutmut_12__mutmut_3, 
    'x_x_check_budget__mutmut_12__mutmut_4': x_x_check_budget__mutmut_12__mutmut_4, 
    'x_x_check_budget__mutmut_12__mutmut_5': x_x_check_budget__mutmut_12__mutmut_5, 
    'x_x_check_budget__mutmut_12__mutmut_6': x_x_check_budget__mutmut_12__mutmut_6, 
    'x_x_check_budget__mutmut_12__mutmut_7': x_x_check_budget__mutmut_12__mutmut_7, 
    'x_x_check_budget__mutmut_12__mutmut_8': x_x_check_budget__mutmut_12__mutmut_8, 
    'x_x_check_budget__mutmut_12__mutmut_9': x_x_check_budget__mutmut_12__mutmut_9, 
    'x_x_check_budget__mutmut_12__mutmut_10': x_x_check_budget__mutmut_12__mutmut_10, 
    'x_x_check_budget__mutmut_12__mutmut_11': x_x_check_budget__mutmut_12__mutmut_11, 
    'x_x_check_budget__mutmut_12__mutmut_12': x_x_check_budget__mutmut_12__mutmut_12, 
    'x_x_check_budget__mutmut_12__mutmut_13': x_x_check_budget__mutmut_12__mutmut_13, 
    'x_x_check_budget__mutmut_12__mutmut_14': x_x_check_budget__mutmut_12__mutmut_14, 
    'x_x_check_budget__mutmut_12__mutmut_15': x_x_check_budget__mutmut_12__mutmut_15, 
    'x_x_check_budget__mutmut_12__mutmut_16': x_x_check_budget__mutmut_12__mutmut_16, 
    'x_x_check_budget__mutmut_12__mutmut_17': x_x_check_budget__mutmut_12__mutmut_17, 
    'x_x_check_budget__mutmut_12__mutmut_18': x_x_check_budget__mutmut_12__mutmut_18, 
    'x_x_check_budget__mutmut_12__mutmut_19': x_x_check_budget__mutmut_12__mutmut_19, 
    'x_x_check_budget__mutmut_12__mutmut_20': x_x_check_budget__mutmut_12__mutmut_20, 
    'x_x_check_budget__mutmut_12__mutmut_21': x_x_check_budget__mutmut_12__mutmut_21, 
    'x_x_check_budget__mutmut_12__mutmut_22': x_x_check_budget__mutmut_12__mutmut_22
}
x_x_check_budget__mutmut_12__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_12'


def x_check_budget__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_13__mutmut_orig, x_x_check_budget__mutmut_13__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_13__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXXXConsecutive errors exceededXXXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "xxconsecutive errors exceededxx"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXCONSECUTIVE ERRORS EXCEEDEDXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_13__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_13__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_13__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_13__mutmut_1': x_x_check_budget__mutmut_13__mutmut_1, 
    'x_x_check_budget__mutmut_13__mutmut_2': x_x_check_budget__mutmut_13__mutmut_2, 
    'x_x_check_budget__mutmut_13__mutmut_3': x_x_check_budget__mutmut_13__mutmut_3, 
    'x_x_check_budget__mutmut_13__mutmut_4': x_x_check_budget__mutmut_13__mutmut_4, 
    'x_x_check_budget__mutmut_13__mutmut_5': x_x_check_budget__mutmut_13__mutmut_5, 
    'x_x_check_budget__mutmut_13__mutmut_6': x_x_check_budget__mutmut_13__mutmut_6, 
    'x_x_check_budget__mutmut_13__mutmut_7': x_x_check_budget__mutmut_13__mutmut_7, 
    'x_x_check_budget__mutmut_13__mutmut_8': x_x_check_budget__mutmut_13__mutmut_8, 
    'x_x_check_budget__mutmut_13__mutmut_9': x_x_check_budget__mutmut_13__mutmut_9, 
    'x_x_check_budget__mutmut_13__mutmut_10': x_x_check_budget__mutmut_13__mutmut_10, 
    'x_x_check_budget__mutmut_13__mutmut_11': x_x_check_budget__mutmut_13__mutmut_11, 
    'x_x_check_budget__mutmut_13__mutmut_12': x_x_check_budget__mutmut_13__mutmut_12, 
    'x_x_check_budget__mutmut_13__mutmut_13': x_x_check_budget__mutmut_13__mutmut_13, 
    'x_x_check_budget__mutmut_13__mutmut_14': x_x_check_budget__mutmut_13__mutmut_14, 
    'x_x_check_budget__mutmut_13__mutmut_15': x_x_check_budget__mutmut_13__mutmut_15, 
    'x_x_check_budget__mutmut_13__mutmut_16': x_x_check_budget__mutmut_13__mutmut_16, 
    'x_x_check_budget__mutmut_13__mutmut_17': x_x_check_budget__mutmut_13__mutmut_17, 
    'x_x_check_budget__mutmut_13__mutmut_18': x_x_check_budget__mutmut_13__mutmut_18, 
    'x_x_check_budget__mutmut_13__mutmut_19': x_x_check_budget__mutmut_13__mutmut_19, 
    'x_x_check_budget__mutmut_13__mutmut_20': x_x_check_budget__mutmut_13__mutmut_20, 
    'x_x_check_budget__mutmut_13__mutmut_21': x_x_check_budget__mutmut_13__mutmut_21, 
    'x_x_check_budget__mutmut_13__mutmut_22': x_x_check_budget__mutmut_13__mutmut_22
}
x_x_check_budget__mutmut_13__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_13'


def x_check_budget__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_14__mutmut_orig, x_x_check_budget__mutmut_14__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_14__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXconsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_14__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_14__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_14__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_14__mutmut_1': x_x_check_budget__mutmut_14__mutmut_1, 
    'x_x_check_budget__mutmut_14__mutmut_2': x_x_check_budget__mutmut_14__mutmut_2, 
    'x_x_check_budget__mutmut_14__mutmut_3': x_x_check_budget__mutmut_14__mutmut_3, 
    'x_x_check_budget__mutmut_14__mutmut_4': x_x_check_budget__mutmut_14__mutmut_4, 
    'x_x_check_budget__mutmut_14__mutmut_5': x_x_check_budget__mutmut_14__mutmut_5, 
    'x_x_check_budget__mutmut_14__mutmut_6': x_x_check_budget__mutmut_14__mutmut_6, 
    'x_x_check_budget__mutmut_14__mutmut_7': x_x_check_budget__mutmut_14__mutmut_7, 
    'x_x_check_budget__mutmut_14__mutmut_8': x_x_check_budget__mutmut_14__mutmut_8, 
    'x_x_check_budget__mutmut_14__mutmut_9': x_x_check_budget__mutmut_14__mutmut_9, 
    'x_x_check_budget__mutmut_14__mutmut_10': x_x_check_budget__mutmut_14__mutmut_10, 
    'x_x_check_budget__mutmut_14__mutmut_11': x_x_check_budget__mutmut_14__mutmut_11, 
    'x_x_check_budget__mutmut_14__mutmut_12': x_x_check_budget__mutmut_14__mutmut_12, 
    'x_x_check_budget__mutmut_14__mutmut_13': x_x_check_budget__mutmut_14__mutmut_13, 
    'x_x_check_budget__mutmut_14__mutmut_14': x_x_check_budget__mutmut_14__mutmut_14, 
    'x_x_check_budget__mutmut_14__mutmut_15': x_x_check_budget__mutmut_14__mutmut_15, 
    'x_x_check_budget__mutmut_14__mutmut_16': x_x_check_budget__mutmut_14__mutmut_16, 
    'x_x_check_budget__mutmut_14__mutmut_17': x_x_check_budget__mutmut_14__mutmut_17, 
    'x_x_check_budget__mutmut_14__mutmut_18': x_x_check_budget__mutmut_14__mutmut_18, 
    'x_x_check_budget__mutmut_14__mutmut_19': x_x_check_budget__mutmut_14__mutmut_19, 
    'x_x_check_budget__mutmut_14__mutmut_20': x_x_check_budget__mutmut_14__mutmut_20, 
    'x_x_check_budget__mutmut_14__mutmut_21': x_x_check_budget__mutmut_14__mutmut_21
}
x_x_check_budget__mutmut_14__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_14'


def x_check_budget__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_15__mutmut_orig, x_x_check_budget__mutmut_15__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_15__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXCONSECUTIVE ERRORS EXCEEDEDXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_15__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_15__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_15__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_15__mutmut_1': x_x_check_budget__mutmut_15__mutmut_1, 
    'x_x_check_budget__mutmut_15__mutmut_2': x_x_check_budget__mutmut_15__mutmut_2, 
    'x_x_check_budget__mutmut_15__mutmut_3': x_x_check_budget__mutmut_15__mutmut_3, 
    'x_x_check_budget__mutmut_15__mutmut_4': x_x_check_budget__mutmut_15__mutmut_4, 
    'x_x_check_budget__mutmut_15__mutmut_5': x_x_check_budget__mutmut_15__mutmut_5, 
    'x_x_check_budget__mutmut_15__mutmut_6': x_x_check_budget__mutmut_15__mutmut_6, 
    'x_x_check_budget__mutmut_15__mutmut_7': x_x_check_budget__mutmut_15__mutmut_7, 
    'x_x_check_budget__mutmut_15__mutmut_8': x_x_check_budget__mutmut_15__mutmut_8, 
    'x_x_check_budget__mutmut_15__mutmut_9': x_x_check_budget__mutmut_15__mutmut_9, 
    'x_x_check_budget__mutmut_15__mutmut_10': x_x_check_budget__mutmut_15__mutmut_10, 
    'x_x_check_budget__mutmut_15__mutmut_11': x_x_check_budget__mutmut_15__mutmut_11, 
    'x_x_check_budget__mutmut_15__mutmut_12': x_x_check_budget__mutmut_15__mutmut_12, 
    'x_x_check_budget__mutmut_15__mutmut_13': x_x_check_budget__mutmut_15__mutmut_13, 
    'x_x_check_budget__mutmut_15__mutmut_14': x_x_check_budget__mutmut_15__mutmut_14, 
    'x_x_check_budget__mutmut_15__mutmut_15': x_x_check_budget__mutmut_15__mutmut_15, 
    'x_x_check_budget__mutmut_15__mutmut_16': x_x_check_budget__mutmut_15__mutmut_16, 
    'x_x_check_budget__mutmut_15__mutmut_17': x_x_check_budget__mutmut_15__mutmut_17, 
    'x_x_check_budget__mutmut_15__mutmut_18': x_x_check_budget__mutmut_15__mutmut_18, 
    'x_x_check_budget__mutmut_15__mutmut_19': x_x_check_budget__mutmut_15__mutmut_19, 
    'x_x_check_budget__mutmut_15__mutmut_20': x_x_check_budget__mutmut_15__mutmut_20, 
    'x_x_check_budget__mutmut_15__mutmut_21': x_x_check_budget__mutmut_15__mutmut_21
}
x_x_check_budget__mutmut_15__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_15'


def x_check_budget__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_16__mutmut_orig, x_x_check_budget__mutmut_16__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_16__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_16__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_16__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_16__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_16__mutmut_1': x_x_check_budget__mutmut_16__mutmut_1, 
    'x_x_check_budget__mutmut_16__mutmut_2': x_x_check_budget__mutmut_16__mutmut_2, 
    'x_x_check_budget__mutmut_16__mutmut_3': x_x_check_budget__mutmut_16__mutmut_3, 
    'x_x_check_budget__mutmut_16__mutmut_4': x_x_check_budget__mutmut_16__mutmut_4, 
    'x_x_check_budget__mutmut_16__mutmut_5': x_x_check_budget__mutmut_16__mutmut_5, 
    'x_x_check_budget__mutmut_16__mutmut_6': x_x_check_budget__mutmut_16__mutmut_6, 
    'x_x_check_budget__mutmut_16__mutmut_7': x_x_check_budget__mutmut_16__mutmut_7, 
    'x_x_check_budget__mutmut_16__mutmut_8': x_x_check_budget__mutmut_16__mutmut_8, 
    'x_x_check_budget__mutmut_16__mutmut_9': x_x_check_budget__mutmut_16__mutmut_9, 
    'x_x_check_budget__mutmut_16__mutmut_10': x_x_check_budget__mutmut_16__mutmut_10, 
    'x_x_check_budget__mutmut_16__mutmut_11': x_x_check_budget__mutmut_16__mutmut_11, 
    'x_x_check_budget__mutmut_16__mutmut_12': x_x_check_budget__mutmut_16__mutmut_12, 
    'x_x_check_budget__mutmut_16__mutmut_13': x_x_check_budget__mutmut_16__mutmut_13, 
    'x_x_check_budget__mutmut_16__mutmut_14': x_x_check_budget__mutmut_16__mutmut_14, 
    'x_x_check_budget__mutmut_16__mutmut_15': x_x_check_budget__mutmut_16__mutmut_15, 
    'x_x_check_budget__mutmut_16__mutmut_16': x_x_check_budget__mutmut_16__mutmut_16, 
    'x_x_check_budget__mutmut_16__mutmut_17': x_x_check_budget__mutmut_16__mutmut_17, 
    'x_x_check_budget__mutmut_16__mutmut_18': x_x_check_budget__mutmut_16__mutmut_18, 
    'x_x_check_budget__mutmut_16__mutmut_19': x_x_check_budget__mutmut_16__mutmut_19, 
    'x_x_check_budget__mutmut_16__mutmut_20': x_x_check_budget__mutmut_16__mutmut_20, 
    'x_x_check_budget__mutmut_16__mutmut_21': x_x_check_budget__mutmut_16__mutmut_21, 
    'x_x_check_budget__mutmut_16__mutmut_22': x_x_check_budget__mutmut_16__mutmut_22
}
x_x_check_budget__mutmut_16__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_16'


def x_check_budget__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_17__mutmut_orig, x_x_check_budget__mutmut_17__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_17__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_17__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_17__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_17__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_17__mutmut_1': x_x_check_budget__mutmut_17__mutmut_1, 
    'x_x_check_budget__mutmut_17__mutmut_2': x_x_check_budget__mutmut_17__mutmut_2, 
    'x_x_check_budget__mutmut_17__mutmut_3': x_x_check_budget__mutmut_17__mutmut_3, 
    'x_x_check_budget__mutmut_17__mutmut_4': x_x_check_budget__mutmut_17__mutmut_4, 
    'x_x_check_budget__mutmut_17__mutmut_5': x_x_check_budget__mutmut_17__mutmut_5, 
    'x_x_check_budget__mutmut_17__mutmut_6': x_x_check_budget__mutmut_17__mutmut_6, 
    'x_x_check_budget__mutmut_17__mutmut_7': x_x_check_budget__mutmut_17__mutmut_7, 
    'x_x_check_budget__mutmut_17__mutmut_8': x_x_check_budget__mutmut_17__mutmut_8, 
    'x_x_check_budget__mutmut_17__mutmut_9': x_x_check_budget__mutmut_17__mutmut_9, 
    'x_x_check_budget__mutmut_17__mutmut_10': x_x_check_budget__mutmut_17__mutmut_10, 
    'x_x_check_budget__mutmut_17__mutmut_11': x_x_check_budget__mutmut_17__mutmut_11, 
    'x_x_check_budget__mutmut_17__mutmut_12': x_x_check_budget__mutmut_17__mutmut_12, 
    'x_x_check_budget__mutmut_17__mutmut_13': x_x_check_budget__mutmut_17__mutmut_13, 
    'x_x_check_budget__mutmut_17__mutmut_14': x_x_check_budget__mutmut_17__mutmut_14, 
    'x_x_check_budget__mutmut_17__mutmut_15': x_x_check_budget__mutmut_17__mutmut_15, 
    'x_x_check_budget__mutmut_17__mutmut_16': x_x_check_budget__mutmut_17__mutmut_16, 
    'x_x_check_budget__mutmut_17__mutmut_17': x_x_check_budget__mutmut_17__mutmut_17, 
    'x_x_check_budget__mutmut_17__mutmut_18': x_x_check_budget__mutmut_17__mutmut_18, 
    'x_x_check_budget__mutmut_17__mutmut_19': x_x_check_budget__mutmut_17__mutmut_19, 
    'x_x_check_budget__mutmut_17__mutmut_20': x_x_check_budget__mutmut_17__mutmut_20, 
    'x_x_check_budget__mutmut_17__mutmut_21': x_x_check_budget__mutmut_17__mutmut_21, 
    'x_x_check_budget__mutmut_17__mutmut_22': x_x_check_budget__mutmut_17__mutmut_22
}
x_x_check_budget__mutmut_17__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_17'


def x_check_budget__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_18__mutmut_orig, x_x_check_budget__mutmut_18__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_18__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "XXCost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXXXCost budget exceededXXXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "xxcost budget exceededxx"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCOST BUDGET EXCEEDEDXX"
    return True, ""


def x_x_check_budget__mutmut_18__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return False, ""


def x_x_check_budget__mutmut_18__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, "XXXX"

x_x_check_budget__mutmut_18__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_18__mutmut_1': x_x_check_budget__mutmut_18__mutmut_1, 
    'x_x_check_budget__mutmut_18__mutmut_2': x_x_check_budget__mutmut_18__mutmut_2, 
    'x_x_check_budget__mutmut_18__mutmut_3': x_x_check_budget__mutmut_18__mutmut_3, 
    'x_x_check_budget__mutmut_18__mutmut_4': x_x_check_budget__mutmut_18__mutmut_4, 
    'x_x_check_budget__mutmut_18__mutmut_5': x_x_check_budget__mutmut_18__mutmut_5, 
    'x_x_check_budget__mutmut_18__mutmut_6': x_x_check_budget__mutmut_18__mutmut_6, 
    'x_x_check_budget__mutmut_18__mutmut_7': x_x_check_budget__mutmut_18__mutmut_7, 
    'x_x_check_budget__mutmut_18__mutmut_8': x_x_check_budget__mutmut_18__mutmut_8, 
    'x_x_check_budget__mutmut_18__mutmut_9': x_x_check_budget__mutmut_18__mutmut_9, 
    'x_x_check_budget__mutmut_18__mutmut_10': x_x_check_budget__mutmut_18__mutmut_10, 
    'x_x_check_budget__mutmut_18__mutmut_11': x_x_check_budget__mutmut_18__mutmut_11, 
    'x_x_check_budget__mutmut_18__mutmut_12': x_x_check_budget__mutmut_18__mutmut_12, 
    'x_x_check_budget__mutmut_18__mutmut_13': x_x_check_budget__mutmut_18__mutmut_13, 
    'x_x_check_budget__mutmut_18__mutmut_14': x_x_check_budget__mutmut_18__mutmut_14, 
    'x_x_check_budget__mutmut_18__mutmut_15': x_x_check_budget__mutmut_18__mutmut_15, 
    'x_x_check_budget__mutmut_18__mutmut_16': x_x_check_budget__mutmut_18__mutmut_16, 
    'x_x_check_budget__mutmut_18__mutmut_17': x_x_check_budget__mutmut_18__mutmut_17, 
    'x_x_check_budget__mutmut_18__mutmut_18': x_x_check_budget__mutmut_18__mutmut_18, 
    'x_x_check_budget__mutmut_18__mutmut_19': x_x_check_budget__mutmut_18__mutmut_19, 
    'x_x_check_budget__mutmut_18__mutmut_20': x_x_check_budget__mutmut_18__mutmut_20, 
    'x_x_check_budget__mutmut_18__mutmut_21': x_x_check_budget__mutmut_18__mutmut_21, 
    'x_x_check_budget__mutmut_18__mutmut_22': x_x_check_budget__mutmut_18__mutmut_22
}
x_x_check_budget__mutmut_18__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_18'


def x_check_budget__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_19__mutmut_orig, x_x_check_budget__mutmut_19__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_19__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXcost budget exceededXX"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_19__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_19__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, "XXXX"

x_x_check_budget__mutmut_19__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_19__mutmut_1': x_x_check_budget__mutmut_19__mutmut_1, 
    'x_x_check_budget__mutmut_19__mutmut_2': x_x_check_budget__mutmut_19__mutmut_2, 
    'x_x_check_budget__mutmut_19__mutmut_3': x_x_check_budget__mutmut_19__mutmut_3, 
    'x_x_check_budget__mutmut_19__mutmut_4': x_x_check_budget__mutmut_19__mutmut_4, 
    'x_x_check_budget__mutmut_19__mutmut_5': x_x_check_budget__mutmut_19__mutmut_5, 
    'x_x_check_budget__mutmut_19__mutmut_6': x_x_check_budget__mutmut_19__mutmut_6, 
    'x_x_check_budget__mutmut_19__mutmut_7': x_x_check_budget__mutmut_19__mutmut_7, 
    'x_x_check_budget__mutmut_19__mutmut_8': x_x_check_budget__mutmut_19__mutmut_8, 
    'x_x_check_budget__mutmut_19__mutmut_9': x_x_check_budget__mutmut_19__mutmut_9, 
    'x_x_check_budget__mutmut_19__mutmut_10': x_x_check_budget__mutmut_19__mutmut_10, 
    'x_x_check_budget__mutmut_19__mutmut_11': x_x_check_budget__mutmut_19__mutmut_11, 
    'x_x_check_budget__mutmut_19__mutmut_12': x_x_check_budget__mutmut_19__mutmut_12, 
    'x_x_check_budget__mutmut_19__mutmut_13': x_x_check_budget__mutmut_19__mutmut_13, 
    'x_x_check_budget__mutmut_19__mutmut_14': x_x_check_budget__mutmut_19__mutmut_14, 
    'x_x_check_budget__mutmut_19__mutmut_15': x_x_check_budget__mutmut_19__mutmut_15, 
    'x_x_check_budget__mutmut_19__mutmut_16': x_x_check_budget__mutmut_19__mutmut_16, 
    'x_x_check_budget__mutmut_19__mutmut_17': x_x_check_budget__mutmut_19__mutmut_17, 
    'x_x_check_budget__mutmut_19__mutmut_18': x_x_check_budget__mutmut_19__mutmut_18, 
    'x_x_check_budget__mutmut_19__mutmut_19': x_x_check_budget__mutmut_19__mutmut_19, 
    'x_x_check_budget__mutmut_19__mutmut_20': x_x_check_budget__mutmut_19__mutmut_20, 
    'x_x_check_budget__mutmut_19__mutmut_21': x_x_check_budget__mutmut_19__mutmut_21
}
x_x_check_budget__mutmut_19__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_19'


def x_check_budget__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_20__mutmut_orig, x_x_check_budget__mutmut_20__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_20__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "COST BUDGET EXCEEDED"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCOST BUDGET EXCEEDEDXX"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_20__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return False, ""


def x_x_check_budget__mutmut_20__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, "XXXX"

x_x_check_budget__mutmut_20__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_20__mutmut_1': x_x_check_budget__mutmut_20__mutmut_1, 
    'x_x_check_budget__mutmut_20__mutmut_2': x_x_check_budget__mutmut_20__mutmut_2, 
    'x_x_check_budget__mutmut_20__mutmut_3': x_x_check_budget__mutmut_20__mutmut_3, 
    'x_x_check_budget__mutmut_20__mutmut_4': x_x_check_budget__mutmut_20__mutmut_4, 
    'x_x_check_budget__mutmut_20__mutmut_5': x_x_check_budget__mutmut_20__mutmut_5, 
    'x_x_check_budget__mutmut_20__mutmut_6': x_x_check_budget__mutmut_20__mutmut_6, 
    'x_x_check_budget__mutmut_20__mutmut_7': x_x_check_budget__mutmut_20__mutmut_7, 
    'x_x_check_budget__mutmut_20__mutmut_8': x_x_check_budget__mutmut_20__mutmut_8, 
    'x_x_check_budget__mutmut_20__mutmut_9': x_x_check_budget__mutmut_20__mutmut_9, 
    'x_x_check_budget__mutmut_20__mutmut_10': x_x_check_budget__mutmut_20__mutmut_10, 
    'x_x_check_budget__mutmut_20__mutmut_11': x_x_check_budget__mutmut_20__mutmut_11, 
    'x_x_check_budget__mutmut_20__mutmut_12': x_x_check_budget__mutmut_20__mutmut_12, 
    'x_x_check_budget__mutmut_20__mutmut_13': x_x_check_budget__mutmut_20__mutmut_13, 
    'x_x_check_budget__mutmut_20__mutmut_14': x_x_check_budget__mutmut_20__mutmut_14, 
    'x_x_check_budget__mutmut_20__mutmut_15': x_x_check_budget__mutmut_20__mutmut_15, 
    'x_x_check_budget__mutmut_20__mutmut_16': x_x_check_budget__mutmut_20__mutmut_16, 
    'x_x_check_budget__mutmut_20__mutmut_17': x_x_check_budget__mutmut_20__mutmut_17, 
    'x_x_check_budget__mutmut_20__mutmut_18': x_x_check_budget__mutmut_20__mutmut_18, 
    'x_x_check_budget__mutmut_20__mutmut_19': x_x_check_budget__mutmut_20__mutmut_19, 
    'x_x_check_budget__mutmut_20__mutmut_20': x_x_check_budget__mutmut_20__mutmut_20, 
    'x_x_check_budget__mutmut_20__mutmut_21': x_x_check_budget__mutmut_20__mutmut_21
}
x_x_check_budget__mutmut_20__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_20'


def x_check_budget__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_21__mutmut_orig, x_x_check_budget__mutmut_21__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_21__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return False, ""


def x_x_check_budget__mutmut_21__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, ""


def x_x_check_budget__mutmut_21__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, "XXXX"

x_x_check_budget__mutmut_21__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_21__mutmut_1': x_x_check_budget__mutmut_21__mutmut_1, 
    'x_x_check_budget__mutmut_21__mutmut_2': x_x_check_budget__mutmut_21__mutmut_2, 
    'x_x_check_budget__mutmut_21__mutmut_3': x_x_check_budget__mutmut_21__mutmut_3, 
    'x_x_check_budget__mutmut_21__mutmut_4': x_x_check_budget__mutmut_21__mutmut_4, 
    'x_x_check_budget__mutmut_21__mutmut_5': x_x_check_budget__mutmut_21__mutmut_5, 
    'x_x_check_budget__mutmut_21__mutmut_6': x_x_check_budget__mutmut_21__mutmut_6, 
    'x_x_check_budget__mutmut_21__mutmut_7': x_x_check_budget__mutmut_21__mutmut_7, 
    'x_x_check_budget__mutmut_21__mutmut_8': x_x_check_budget__mutmut_21__mutmut_8, 
    'x_x_check_budget__mutmut_21__mutmut_9': x_x_check_budget__mutmut_21__mutmut_9, 
    'x_x_check_budget__mutmut_21__mutmut_10': x_x_check_budget__mutmut_21__mutmut_10, 
    'x_x_check_budget__mutmut_21__mutmut_11': x_x_check_budget__mutmut_21__mutmut_11, 
    'x_x_check_budget__mutmut_21__mutmut_12': x_x_check_budget__mutmut_21__mutmut_12, 
    'x_x_check_budget__mutmut_21__mutmut_13': x_x_check_budget__mutmut_21__mutmut_13, 
    'x_x_check_budget__mutmut_21__mutmut_14': x_x_check_budget__mutmut_21__mutmut_14, 
    'x_x_check_budget__mutmut_21__mutmut_15': x_x_check_budget__mutmut_21__mutmut_15, 
    'x_x_check_budget__mutmut_21__mutmut_16': x_x_check_budget__mutmut_21__mutmut_16, 
    'x_x_check_budget__mutmut_21__mutmut_17': x_x_check_budget__mutmut_21__mutmut_17, 
    'x_x_check_budget__mutmut_21__mutmut_18': x_x_check_budget__mutmut_21__mutmut_18, 
    'x_x_check_budget__mutmut_21__mutmut_19': x_x_check_budget__mutmut_21__mutmut_19, 
    'x_x_check_budget__mutmut_21__mutmut_20': x_x_check_budget__mutmut_21__mutmut_20, 
    'x_x_check_budget__mutmut_21__mutmut_21': x_x_check_budget__mutmut_21__mutmut_21, 
    'x_x_check_budget__mutmut_21__mutmut_22': x_x_check_budget__mutmut_21__mutmut_22
}
x_x_check_budget__mutmut_21__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_21'


def x_check_budget__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_budget__mutmut_22__mutmut_orig, x_x_check_budget__mutmut_22__mutmut_mutants, args, kwargs, None)


def x_x_check_budget__mutmut_22__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used >= limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return True, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "XXToken budget exceededXX"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "TOKEN BUDGET EXCEEDED"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls >= limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return True, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "XXTool calls per turn exceededXX"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "TOOL CALLS PER TURN EXCEEDED"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors >= limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return True, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "XXConsecutive errors exceededXX"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "CONSECUTIVE ERRORS EXCEEDED"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd >= limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_17(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return True, "Cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_18(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "XXCost budget exceededXX"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_19(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "cost budget exceeded"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_20(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "COST BUDGET EXCEEDED"
    return True, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_21(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return False, "XXXX"


def x_x_check_budget__mutmut_22__mutmut_22(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "XXXXXXXX"


def x_x_check_budget__mutmut_22__mutmut_23(state: BudgetState, limits: BudgetLimits) -> tuple[bool, str]:
    if state.tokens_used > limits.max_tokens:
        return False, "Token budget exceeded"
    if state.tool_calls > limits.max_tool_calls_per_turn:
        return False, "Tool calls per turn exceeded"
    if state.consecutive_errors > limits.max_consecutive_errors:
        return False, "Consecutive errors exceeded"
    if state.cost_usd > limits.max_cost_usd:
        return False, "Cost budget exceeded"
    return True, "xxxx"

x_x_check_budget__mutmut_22__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_budget__mutmut_22__mutmut_1': x_x_check_budget__mutmut_22__mutmut_1, 
    'x_x_check_budget__mutmut_22__mutmut_2': x_x_check_budget__mutmut_22__mutmut_2, 
    'x_x_check_budget__mutmut_22__mutmut_3': x_x_check_budget__mutmut_22__mutmut_3, 
    'x_x_check_budget__mutmut_22__mutmut_4': x_x_check_budget__mutmut_22__mutmut_4, 
    'x_x_check_budget__mutmut_22__mutmut_5': x_x_check_budget__mutmut_22__mutmut_5, 
    'x_x_check_budget__mutmut_22__mutmut_6': x_x_check_budget__mutmut_22__mutmut_6, 
    'x_x_check_budget__mutmut_22__mutmut_7': x_x_check_budget__mutmut_22__mutmut_7, 
    'x_x_check_budget__mutmut_22__mutmut_8': x_x_check_budget__mutmut_22__mutmut_8, 
    'x_x_check_budget__mutmut_22__mutmut_9': x_x_check_budget__mutmut_22__mutmut_9, 
    'x_x_check_budget__mutmut_22__mutmut_10': x_x_check_budget__mutmut_22__mutmut_10, 
    'x_x_check_budget__mutmut_22__mutmut_11': x_x_check_budget__mutmut_22__mutmut_11, 
    'x_x_check_budget__mutmut_22__mutmut_12': x_x_check_budget__mutmut_22__mutmut_12, 
    'x_x_check_budget__mutmut_22__mutmut_13': x_x_check_budget__mutmut_22__mutmut_13, 
    'x_x_check_budget__mutmut_22__mutmut_14': x_x_check_budget__mutmut_22__mutmut_14, 
    'x_x_check_budget__mutmut_22__mutmut_15': x_x_check_budget__mutmut_22__mutmut_15, 
    'x_x_check_budget__mutmut_22__mutmut_16': x_x_check_budget__mutmut_22__mutmut_16, 
    'x_x_check_budget__mutmut_22__mutmut_17': x_x_check_budget__mutmut_22__mutmut_17, 
    'x_x_check_budget__mutmut_22__mutmut_18': x_x_check_budget__mutmut_22__mutmut_18, 
    'x_x_check_budget__mutmut_22__mutmut_19': x_x_check_budget__mutmut_22__mutmut_19, 
    'x_x_check_budget__mutmut_22__mutmut_20': x_x_check_budget__mutmut_22__mutmut_20, 
    'x_x_check_budget__mutmut_22__mutmut_21': x_x_check_budget__mutmut_22__mutmut_21, 
    'x_x_check_budget__mutmut_22__mutmut_22': x_x_check_budget__mutmut_22__mutmut_22, 
    'x_x_check_budget__mutmut_22__mutmut_23': x_x_check_budget__mutmut_22__mutmut_23
}
x_x_check_budget__mutmut_22__mutmut_orig.__name__ = 'x_x_check_budget__mutmut_22'

x_check_budget__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_budget__mutmut_1': x_check_budget__mutmut_1, 
    'x_check_budget__mutmut_2': x_check_budget__mutmut_2, 
    'x_check_budget__mutmut_3': x_check_budget__mutmut_3, 
    'x_check_budget__mutmut_4': x_check_budget__mutmut_4, 
    'x_check_budget__mutmut_5': x_check_budget__mutmut_5, 
    'x_check_budget__mutmut_6': x_check_budget__mutmut_6, 
    'x_check_budget__mutmut_7': x_check_budget__mutmut_7, 
    'x_check_budget__mutmut_8': x_check_budget__mutmut_8, 
    'x_check_budget__mutmut_9': x_check_budget__mutmut_9, 
    'x_check_budget__mutmut_10': x_check_budget__mutmut_10, 
    'x_check_budget__mutmut_11': x_check_budget__mutmut_11, 
    'x_check_budget__mutmut_12': x_check_budget__mutmut_12, 
    'x_check_budget__mutmut_13': x_check_budget__mutmut_13, 
    'x_check_budget__mutmut_14': x_check_budget__mutmut_14, 
    'x_check_budget__mutmut_15': x_check_budget__mutmut_15, 
    'x_check_budget__mutmut_16': x_check_budget__mutmut_16, 
    'x_check_budget__mutmut_17': x_check_budget__mutmut_17, 
    'x_check_budget__mutmut_18': x_check_budget__mutmut_18, 
    'x_check_budget__mutmut_19': x_check_budget__mutmut_19, 
    'x_check_budget__mutmut_20': x_check_budget__mutmut_20, 
    'x_check_budget__mutmut_21': x_check_budget__mutmut_21, 
    'x_check_budget__mutmut_22': x_check_budget__mutmut_22
}
x_check_budget__mutmut_orig.__name__ = 'x_check_budget'


def add_tokens(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, args, kwargs, None)


def x_add_tokens__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, args, kwargs, None)


def x_add_tokens__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, args, kwargs, None)


def x_add_tokens__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, args, kwargs, None)


def x_add_tokens__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_add_tokens__mutmut_mutants, args, kwargs, None)


def x_add_tokens__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, None, args, kwargs, None)


def x_add_tokens__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, None, kwargs, None)


def x_add_tokens__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, args, None, None)


def x_add_tokens__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_mutants, args, kwargs, None)


def x_add_tokens__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, args, kwargs, None)


def x_add_tokens__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, kwargs, None)


def x_add_tokens__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, args, None)


def x_add_tokens__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_add_tokens__mutmut_orig, x_add_tokens__mutmut_mutants, args, kwargs, )

x_add_tokens__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_add_tokens__mutmut_1': x_add_tokens__mutmut_1, 
    'x_add_tokens__mutmut_2': x_add_tokens__mutmut_2, 
    'x_add_tokens__mutmut_3': x_add_tokens__mutmut_3, 
    'x_add_tokens__mutmut_4': x_add_tokens__mutmut_4, 
    'x_add_tokens__mutmut_5': x_add_tokens__mutmut_5, 
    'x_add_tokens__mutmut_6': x_add_tokens__mutmut_6, 
    'x_add_tokens__mutmut_7': x_add_tokens__mutmut_7, 
    'x_add_tokens__mutmut_8': x_add_tokens__mutmut_8, 
    'x_add_tokens__mutmut_9': x_add_tokens__mutmut_9, 
    'x_add_tokens__mutmut_10': x_add_tokens__mutmut_10, 
    'x_add_tokens__mutmut_11': x_add_tokens__mutmut_11
}
x_add_tokens__mutmut_orig.__name__ = 'x_add_tokens'


def x_add_tokens__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_orig__mutmut_orig, x_x_add_tokens__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_orig__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_orig__mutmut_18(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_orig__mutmut_1': x_x_add_tokens__mutmut_orig__mutmut_1, 
    'x_x_add_tokens__mutmut_orig__mutmut_2': x_x_add_tokens__mutmut_orig__mutmut_2, 
    'x_x_add_tokens__mutmut_orig__mutmut_3': x_x_add_tokens__mutmut_orig__mutmut_3, 
    'x_x_add_tokens__mutmut_orig__mutmut_4': x_x_add_tokens__mutmut_orig__mutmut_4, 
    'x_x_add_tokens__mutmut_orig__mutmut_5': x_x_add_tokens__mutmut_orig__mutmut_5, 
    'x_x_add_tokens__mutmut_orig__mutmut_6': x_x_add_tokens__mutmut_orig__mutmut_6, 
    'x_x_add_tokens__mutmut_orig__mutmut_7': x_x_add_tokens__mutmut_orig__mutmut_7, 
    'x_x_add_tokens__mutmut_orig__mutmut_8': x_x_add_tokens__mutmut_orig__mutmut_8, 
    'x_x_add_tokens__mutmut_orig__mutmut_9': x_x_add_tokens__mutmut_orig__mutmut_9, 
    'x_x_add_tokens__mutmut_orig__mutmut_10': x_x_add_tokens__mutmut_orig__mutmut_10, 
    'x_x_add_tokens__mutmut_orig__mutmut_11': x_x_add_tokens__mutmut_orig__mutmut_11, 
    'x_x_add_tokens__mutmut_orig__mutmut_12': x_x_add_tokens__mutmut_orig__mutmut_12, 
    'x_x_add_tokens__mutmut_orig__mutmut_13': x_x_add_tokens__mutmut_orig__mutmut_13, 
    'x_x_add_tokens__mutmut_orig__mutmut_14': x_x_add_tokens__mutmut_orig__mutmut_14, 
    'x_x_add_tokens__mutmut_orig__mutmut_15': x_x_add_tokens__mutmut_orig__mutmut_15, 
    'x_x_add_tokens__mutmut_orig__mutmut_16': x_x_add_tokens__mutmut_orig__mutmut_16, 
    'x_x_add_tokens__mutmut_orig__mutmut_17': x_x_add_tokens__mutmut_orig__mutmut_17, 
    'x_x_add_tokens__mutmut_orig__mutmut_18': x_x_add_tokens__mutmut_orig__mutmut_18
}
x_x_add_tokens__mutmut_orig__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_orig'


def x_add_tokens__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_1__mutmut_orig, x_x_add_tokens__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_1__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = ""
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_1__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_1__mutmut_1': x_x_add_tokens__mutmut_1__mutmut_1, 
    'x_x_add_tokens__mutmut_1__mutmut_2': x_x_add_tokens__mutmut_1__mutmut_2, 
    'x_x_add_tokens__mutmut_1__mutmut_3': x_x_add_tokens__mutmut_1__mutmut_3, 
    'x_x_add_tokens__mutmut_1__mutmut_4': x_x_add_tokens__mutmut_1__mutmut_4, 
    'x_x_add_tokens__mutmut_1__mutmut_5': x_x_add_tokens__mutmut_1__mutmut_5, 
    'x_x_add_tokens__mutmut_1__mutmut_6': x_x_add_tokens__mutmut_1__mutmut_6, 
    'x_x_add_tokens__mutmut_1__mutmut_7': x_x_add_tokens__mutmut_1__mutmut_7, 
    'x_x_add_tokens__mutmut_1__mutmut_8': x_x_add_tokens__mutmut_1__mutmut_8, 
    'x_x_add_tokens__mutmut_1__mutmut_9': x_x_add_tokens__mutmut_1__mutmut_9, 
    'x_x_add_tokens__mutmut_1__mutmut_10': x_x_add_tokens__mutmut_1__mutmut_10, 
    'x_x_add_tokens__mutmut_1__mutmut_11': x_x_add_tokens__mutmut_1__mutmut_11, 
    'x_x_add_tokens__mutmut_1__mutmut_12': x_x_add_tokens__mutmut_1__mutmut_12, 
    'x_x_add_tokens__mutmut_1__mutmut_13': x_x_add_tokens__mutmut_1__mutmut_13, 
    'x_x_add_tokens__mutmut_1__mutmut_14': x_x_add_tokens__mutmut_1__mutmut_14, 
    'x_x_add_tokens__mutmut_1__mutmut_15': x_x_add_tokens__mutmut_1__mutmut_15, 
    'x_x_add_tokens__mutmut_1__mutmut_16': x_x_add_tokens__mutmut_1__mutmut_16, 
    'x_x_add_tokens__mutmut_1__mutmut_17': x_x_add_tokens__mutmut_1__mutmut_17
}
x_x_add_tokens__mutmut_1__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_1'


def x_add_tokens__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_2__mutmut_orig, x_x_add_tokens__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_2__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_2__mutmut_18(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_2__mutmut_1': x_x_add_tokens__mutmut_2__mutmut_1, 
    'x_x_add_tokens__mutmut_2__mutmut_2': x_x_add_tokens__mutmut_2__mutmut_2, 
    'x_x_add_tokens__mutmut_2__mutmut_3': x_x_add_tokens__mutmut_2__mutmut_3, 
    'x_x_add_tokens__mutmut_2__mutmut_4': x_x_add_tokens__mutmut_2__mutmut_4, 
    'x_x_add_tokens__mutmut_2__mutmut_5': x_x_add_tokens__mutmut_2__mutmut_5, 
    'x_x_add_tokens__mutmut_2__mutmut_6': x_x_add_tokens__mutmut_2__mutmut_6, 
    'x_x_add_tokens__mutmut_2__mutmut_7': x_x_add_tokens__mutmut_2__mutmut_7, 
    'x_x_add_tokens__mutmut_2__mutmut_8': x_x_add_tokens__mutmut_2__mutmut_8, 
    'x_x_add_tokens__mutmut_2__mutmut_9': x_x_add_tokens__mutmut_2__mutmut_9, 
    'x_x_add_tokens__mutmut_2__mutmut_10': x_x_add_tokens__mutmut_2__mutmut_10, 
    'x_x_add_tokens__mutmut_2__mutmut_11': x_x_add_tokens__mutmut_2__mutmut_11, 
    'x_x_add_tokens__mutmut_2__mutmut_12': x_x_add_tokens__mutmut_2__mutmut_12, 
    'x_x_add_tokens__mutmut_2__mutmut_13': x_x_add_tokens__mutmut_2__mutmut_13, 
    'x_x_add_tokens__mutmut_2__mutmut_14': x_x_add_tokens__mutmut_2__mutmut_14, 
    'x_x_add_tokens__mutmut_2__mutmut_15': x_x_add_tokens__mutmut_2__mutmut_15, 
    'x_x_add_tokens__mutmut_2__mutmut_16': x_x_add_tokens__mutmut_2__mutmut_16, 
    'x_x_add_tokens__mutmut_2__mutmut_17': x_x_add_tokens__mutmut_2__mutmut_17, 
    'x_x_add_tokens__mutmut_2__mutmut_18': x_x_add_tokens__mutmut_2__mutmut_18
}
x_x_add_tokens__mutmut_2__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_2'


def x_add_tokens__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_3__mutmut_orig, x_x_add_tokens__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_3__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_3__mutmut_18(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_3__mutmut_1': x_x_add_tokens__mutmut_3__mutmut_1, 
    'x_x_add_tokens__mutmut_3__mutmut_2': x_x_add_tokens__mutmut_3__mutmut_2, 
    'x_x_add_tokens__mutmut_3__mutmut_3': x_x_add_tokens__mutmut_3__mutmut_3, 
    'x_x_add_tokens__mutmut_3__mutmut_4': x_x_add_tokens__mutmut_3__mutmut_4, 
    'x_x_add_tokens__mutmut_3__mutmut_5': x_x_add_tokens__mutmut_3__mutmut_5, 
    'x_x_add_tokens__mutmut_3__mutmut_6': x_x_add_tokens__mutmut_3__mutmut_6, 
    'x_x_add_tokens__mutmut_3__mutmut_7': x_x_add_tokens__mutmut_3__mutmut_7, 
    'x_x_add_tokens__mutmut_3__mutmut_8': x_x_add_tokens__mutmut_3__mutmut_8, 
    'x_x_add_tokens__mutmut_3__mutmut_9': x_x_add_tokens__mutmut_3__mutmut_9, 
    'x_x_add_tokens__mutmut_3__mutmut_10': x_x_add_tokens__mutmut_3__mutmut_10, 
    'x_x_add_tokens__mutmut_3__mutmut_11': x_x_add_tokens__mutmut_3__mutmut_11, 
    'x_x_add_tokens__mutmut_3__mutmut_12': x_x_add_tokens__mutmut_3__mutmut_12, 
    'x_x_add_tokens__mutmut_3__mutmut_13': x_x_add_tokens__mutmut_3__mutmut_13, 
    'x_x_add_tokens__mutmut_3__mutmut_14': x_x_add_tokens__mutmut_3__mutmut_14, 
    'x_x_add_tokens__mutmut_3__mutmut_15': x_x_add_tokens__mutmut_3__mutmut_15, 
    'x_x_add_tokens__mutmut_3__mutmut_16': x_x_add_tokens__mutmut_3__mutmut_16, 
    'x_x_add_tokens__mutmut_3__mutmut_17': x_x_add_tokens__mutmut_3__mutmut_17, 
    'x_x_add_tokens__mutmut_3__mutmut_18': x_x_add_tokens__mutmut_3__mutmut_18
}
x_x_add_tokens__mutmut_3__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_3'


def x_add_tokens__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_4__mutmut_orig, x_x_add_tokens__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_4__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_4__mutmut_18(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_4__mutmut_1': x_x_add_tokens__mutmut_4__mutmut_1, 
    'x_x_add_tokens__mutmut_4__mutmut_2': x_x_add_tokens__mutmut_4__mutmut_2, 
    'x_x_add_tokens__mutmut_4__mutmut_3': x_x_add_tokens__mutmut_4__mutmut_3, 
    'x_x_add_tokens__mutmut_4__mutmut_4': x_x_add_tokens__mutmut_4__mutmut_4, 
    'x_x_add_tokens__mutmut_4__mutmut_5': x_x_add_tokens__mutmut_4__mutmut_5, 
    'x_x_add_tokens__mutmut_4__mutmut_6': x_x_add_tokens__mutmut_4__mutmut_6, 
    'x_x_add_tokens__mutmut_4__mutmut_7': x_x_add_tokens__mutmut_4__mutmut_7, 
    'x_x_add_tokens__mutmut_4__mutmut_8': x_x_add_tokens__mutmut_4__mutmut_8, 
    'x_x_add_tokens__mutmut_4__mutmut_9': x_x_add_tokens__mutmut_4__mutmut_9, 
    'x_x_add_tokens__mutmut_4__mutmut_10': x_x_add_tokens__mutmut_4__mutmut_10, 
    'x_x_add_tokens__mutmut_4__mutmut_11': x_x_add_tokens__mutmut_4__mutmut_11, 
    'x_x_add_tokens__mutmut_4__mutmut_12': x_x_add_tokens__mutmut_4__mutmut_12, 
    'x_x_add_tokens__mutmut_4__mutmut_13': x_x_add_tokens__mutmut_4__mutmut_13, 
    'x_x_add_tokens__mutmut_4__mutmut_14': x_x_add_tokens__mutmut_4__mutmut_14, 
    'x_x_add_tokens__mutmut_4__mutmut_15': x_x_add_tokens__mutmut_4__mutmut_15, 
    'x_x_add_tokens__mutmut_4__mutmut_16': x_x_add_tokens__mutmut_4__mutmut_16, 
    'x_x_add_tokens__mutmut_4__mutmut_17': x_x_add_tokens__mutmut_4__mutmut_17, 
    'x_x_add_tokens__mutmut_4__mutmut_18': x_x_add_tokens__mutmut_4__mutmut_18
}
x_x_add_tokens__mutmut_4__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_4'


def x_add_tokens__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_5__mutmut_orig, x_x_add_tokens__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_5__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = ""
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_5__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_5__mutmut_1': x_x_add_tokens__mutmut_5__mutmut_1, 
    'x_x_add_tokens__mutmut_5__mutmut_2': x_x_add_tokens__mutmut_5__mutmut_2, 
    'x_x_add_tokens__mutmut_5__mutmut_3': x_x_add_tokens__mutmut_5__mutmut_3, 
    'x_x_add_tokens__mutmut_5__mutmut_4': x_x_add_tokens__mutmut_5__mutmut_4, 
    'x_x_add_tokens__mutmut_5__mutmut_5': x_x_add_tokens__mutmut_5__mutmut_5, 
    'x_x_add_tokens__mutmut_5__mutmut_6': x_x_add_tokens__mutmut_5__mutmut_6, 
    'x_x_add_tokens__mutmut_5__mutmut_7': x_x_add_tokens__mutmut_5__mutmut_7, 
    'x_x_add_tokens__mutmut_5__mutmut_8': x_x_add_tokens__mutmut_5__mutmut_8, 
    'x_x_add_tokens__mutmut_5__mutmut_9': x_x_add_tokens__mutmut_5__mutmut_9, 
    'x_x_add_tokens__mutmut_5__mutmut_10': x_x_add_tokens__mutmut_5__mutmut_10
}
x_x_add_tokens__mutmut_5__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_5'


def x_add_tokens__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_6__mutmut_orig, x_x_add_tokens__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_6__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_6__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_6__mutmut_1': x_x_add_tokens__mutmut_6__mutmut_1, 
    'x_x_add_tokens__mutmut_6__mutmut_2': x_x_add_tokens__mutmut_6__mutmut_2, 
    'x_x_add_tokens__mutmut_6__mutmut_3': x_x_add_tokens__mutmut_6__mutmut_3, 
    'x_x_add_tokens__mutmut_6__mutmut_4': x_x_add_tokens__mutmut_6__mutmut_4, 
    'x_x_add_tokens__mutmut_6__mutmut_5': x_x_add_tokens__mutmut_6__mutmut_5, 
    'x_x_add_tokens__mutmut_6__mutmut_6': x_x_add_tokens__mutmut_6__mutmut_6, 
    'x_x_add_tokens__mutmut_6__mutmut_7': x_x_add_tokens__mutmut_6__mutmut_7, 
    'x_x_add_tokens__mutmut_6__mutmut_8': x_x_add_tokens__mutmut_6__mutmut_8, 
    'x_x_add_tokens__mutmut_6__mutmut_9': x_x_add_tokens__mutmut_6__mutmut_9, 
    'x_x_add_tokens__mutmut_6__mutmut_10': x_x_add_tokens__mutmut_6__mutmut_10, 
    'x_x_add_tokens__mutmut_6__mutmut_11': x_x_add_tokens__mutmut_6__mutmut_11, 
    'x_x_add_tokens__mutmut_6__mutmut_12': x_x_add_tokens__mutmut_6__mutmut_12, 
    'x_x_add_tokens__mutmut_6__mutmut_13': x_x_add_tokens__mutmut_6__mutmut_13, 
    'x_x_add_tokens__mutmut_6__mutmut_14': x_x_add_tokens__mutmut_6__mutmut_14, 
    'x_x_add_tokens__mutmut_6__mutmut_15': x_x_add_tokens__mutmut_6__mutmut_15, 
    'x_x_add_tokens__mutmut_6__mutmut_16': x_x_add_tokens__mutmut_6__mutmut_16, 
    'x_x_add_tokens__mutmut_6__mutmut_17': x_x_add_tokens__mutmut_6__mutmut_17
}
x_x_add_tokens__mutmut_6__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_6'


def x_add_tokens__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_7__mutmut_orig, x_x_add_tokens__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_7__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_7__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_7__mutmut_1': x_x_add_tokens__mutmut_7__mutmut_1, 
    'x_x_add_tokens__mutmut_7__mutmut_2': x_x_add_tokens__mutmut_7__mutmut_2, 
    'x_x_add_tokens__mutmut_7__mutmut_3': x_x_add_tokens__mutmut_7__mutmut_3, 
    'x_x_add_tokens__mutmut_7__mutmut_4': x_x_add_tokens__mutmut_7__mutmut_4, 
    'x_x_add_tokens__mutmut_7__mutmut_5': x_x_add_tokens__mutmut_7__mutmut_5, 
    'x_x_add_tokens__mutmut_7__mutmut_6': x_x_add_tokens__mutmut_7__mutmut_6, 
    'x_x_add_tokens__mutmut_7__mutmut_7': x_x_add_tokens__mutmut_7__mutmut_7, 
    'x_x_add_tokens__mutmut_7__mutmut_8': x_x_add_tokens__mutmut_7__mutmut_8, 
    'x_x_add_tokens__mutmut_7__mutmut_9': x_x_add_tokens__mutmut_7__mutmut_9, 
    'x_x_add_tokens__mutmut_7__mutmut_10': x_x_add_tokens__mutmut_7__mutmut_10, 
    'x_x_add_tokens__mutmut_7__mutmut_11': x_x_add_tokens__mutmut_7__mutmut_11, 
    'x_x_add_tokens__mutmut_7__mutmut_12': x_x_add_tokens__mutmut_7__mutmut_12, 
    'x_x_add_tokens__mutmut_7__mutmut_13': x_x_add_tokens__mutmut_7__mutmut_13, 
    'x_x_add_tokens__mutmut_7__mutmut_14': x_x_add_tokens__mutmut_7__mutmut_14, 
    'x_x_add_tokens__mutmut_7__mutmut_15': x_x_add_tokens__mutmut_7__mutmut_15, 
    'x_x_add_tokens__mutmut_7__mutmut_16': x_x_add_tokens__mutmut_7__mutmut_16, 
    'x_x_add_tokens__mutmut_7__mutmut_17': x_x_add_tokens__mutmut_7__mutmut_17
}
x_x_add_tokens__mutmut_7__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_7'


def x_add_tokens__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_8__mutmut_orig, x_x_add_tokens__mutmut_8__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_8__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_8__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_8__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_8__mutmut_1': x_x_add_tokens__mutmut_8__mutmut_1, 
    'x_x_add_tokens__mutmut_8__mutmut_2': x_x_add_tokens__mutmut_8__mutmut_2, 
    'x_x_add_tokens__mutmut_8__mutmut_3': x_x_add_tokens__mutmut_8__mutmut_3, 
    'x_x_add_tokens__mutmut_8__mutmut_4': x_x_add_tokens__mutmut_8__mutmut_4, 
    'x_x_add_tokens__mutmut_8__mutmut_5': x_x_add_tokens__mutmut_8__mutmut_5, 
    'x_x_add_tokens__mutmut_8__mutmut_6': x_x_add_tokens__mutmut_8__mutmut_6, 
    'x_x_add_tokens__mutmut_8__mutmut_7': x_x_add_tokens__mutmut_8__mutmut_7, 
    'x_x_add_tokens__mutmut_8__mutmut_8': x_x_add_tokens__mutmut_8__mutmut_8, 
    'x_x_add_tokens__mutmut_8__mutmut_9': x_x_add_tokens__mutmut_8__mutmut_9, 
    'x_x_add_tokens__mutmut_8__mutmut_10': x_x_add_tokens__mutmut_8__mutmut_10, 
    'x_x_add_tokens__mutmut_8__mutmut_11': x_x_add_tokens__mutmut_8__mutmut_11, 
    'x_x_add_tokens__mutmut_8__mutmut_12': x_x_add_tokens__mutmut_8__mutmut_12, 
    'x_x_add_tokens__mutmut_8__mutmut_13': x_x_add_tokens__mutmut_8__mutmut_13, 
    'x_x_add_tokens__mutmut_8__mutmut_14': x_x_add_tokens__mutmut_8__mutmut_14, 
    'x_x_add_tokens__mutmut_8__mutmut_15': x_x_add_tokens__mutmut_8__mutmut_15, 
    'x_x_add_tokens__mutmut_8__mutmut_16': x_x_add_tokens__mutmut_8__mutmut_16, 
    'x_x_add_tokens__mutmut_8__mutmut_17': x_x_add_tokens__mutmut_8__mutmut_17
}
x_x_add_tokens__mutmut_8__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_8'


def x_add_tokens__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_9__mutmut_orig, x_x_add_tokens__mutmut_9__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_9__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_9__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_9__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_9__mutmut_1': x_x_add_tokens__mutmut_9__mutmut_1, 
    'x_x_add_tokens__mutmut_9__mutmut_2': x_x_add_tokens__mutmut_9__mutmut_2, 
    'x_x_add_tokens__mutmut_9__mutmut_3': x_x_add_tokens__mutmut_9__mutmut_3, 
    'x_x_add_tokens__mutmut_9__mutmut_4': x_x_add_tokens__mutmut_9__mutmut_4, 
    'x_x_add_tokens__mutmut_9__mutmut_5': x_x_add_tokens__mutmut_9__mutmut_5, 
    'x_x_add_tokens__mutmut_9__mutmut_6': x_x_add_tokens__mutmut_9__mutmut_6, 
    'x_x_add_tokens__mutmut_9__mutmut_7': x_x_add_tokens__mutmut_9__mutmut_7, 
    'x_x_add_tokens__mutmut_9__mutmut_8': x_x_add_tokens__mutmut_9__mutmut_8, 
    'x_x_add_tokens__mutmut_9__mutmut_9': x_x_add_tokens__mutmut_9__mutmut_9, 
    'x_x_add_tokens__mutmut_9__mutmut_10': x_x_add_tokens__mutmut_9__mutmut_10, 
    'x_x_add_tokens__mutmut_9__mutmut_11': x_x_add_tokens__mutmut_9__mutmut_11, 
    'x_x_add_tokens__mutmut_9__mutmut_12': x_x_add_tokens__mutmut_9__mutmut_12, 
    'x_x_add_tokens__mutmut_9__mutmut_13': x_x_add_tokens__mutmut_9__mutmut_13, 
    'x_x_add_tokens__mutmut_9__mutmut_14': x_x_add_tokens__mutmut_9__mutmut_14, 
    'x_x_add_tokens__mutmut_9__mutmut_15': x_x_add_tokens__mutmut_9__mutmut_15, 
    'x_x_add_tokens__mutmut_9__mutmut_16': x_x_add_tokens__mutmut_9__mutmut_16, 
    'x_x_add_tokens__mutmut_9__mutmut_17': x_x_add_tokens__mutmut_9__mutmut_17
}
x_x_add_tokens__mutmut_9__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_9'


def x_add_tokens__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_10__mutmut_orig, x_x_add_tokens__mutmut_10__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_10__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_10__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_10__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_10__mutmut_1': x_x_add_tokens__mutmut_10__mutmut_1, 
    'x_x_add_tokens__mutmut_10__mutmut_2': x_x_add_tokens__mutmut_10__mutmut_2, 
    'x_x_add_tokens__mutmut_10__mutmut_3': x_x_add_tokens__mutmut_10__mutmut_3, 
    'x_x_add_tokens__mutmut_10__mutmut_4': x_x_add_tokens__mutmut_10__mutmut_4, 
    'x_x_add_tokens__mutmut_10__mutmut_5': x_x_add_tokens__mutmut_10__mutmut_5, 
    'x_x_add_tokens__mutmut_10__mutmut_6': x_x_add_tokens__mutmut_10__mutmut_6, 
    'x_x_add_tokens__mutmut_10__mutmut_7': x_x_add_tokens__mutmut_10__mutmut_7, 
    'x_x_add_tokens__mutmut_10__mutmut_8': x_x_add_tokens__mutmut_10__mutmut_8, 
    'x_x_add_tokens__mutmut_10__mutmut_9': x_x_add_tokens__mutmut_10__mutmut_9, 
    'x_x_add_tokens__mutmut_10__mutmut_10': x_x_add_tokens__mutmut_10__mutmut_10, 
    'x_x_add_tokens__mutmut_10__mutmut_11': x_x_add_tokens__mutmut_10__mutmut_11, 
    'x_x_add_tokens__mutmut_10__mutmut_12': x_x_add_tokens__mutmut_10__mutmut_12, 
    'x_x_add_tokens__mutmut_10__mutmut_13': x_x_add_tokens__mutmut_10__mutmut_13, 
    'x_x_add_tokens__mutmut_10__mutmut_14': x_x_add_tokens__mutmut_10__mutmut_14, 
    'x_x_add_tokens__mutmut_10__mutmut_15': x_x_add_tokens__mutmut_10__mutmut_15, 
    'x_x_add_tokens__mutmut_10__mutmut_16': x_x_add_tokens__mutmut_10__mutmut_16
}
x_x_add_tokens__mutmut_10__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_10'


def x_add_tokens__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_11__mutmut_orig, x_x_add_tokens__mutmut_11__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_11__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_11__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_11__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_11__mutmut_1': x_x_add_tokens__mutmut_11__mutmut_1, 
    'x_x_add_tokens__mutmut_11__mutmut_2': x_x_add_tokens__mutmut_11__mutmut_2, 
    'x_x_add_tokens__mutmut_11__mutmut_3': x_x_add_tokens__mutmut_11__mutmut_3, 
    'x_x_add_tokens__mutmut_11__mutmut_4': x_x_add_tokens__mutmut_11__mutmut_4, 
    'x_x_add_tokens__mutmut_11__mutmut_5': x_x_add_tokens__mutmut_11__mutmut_5, 
    'x_x_add_tokens__mutmut_11__mutmut_6': x_x_add_tokens__mutmut_11__mutmut_6, 
    'x_x_add_tokens__mutmut_11__mutmut_7': x_x_add_tokens__mutmut_11__mutmut_7, 
    'x_x_add_tokens__mutmut_11__mutmut_8': x_x_add_tokens__mutmut_11__mutmut_8, 
    'x_x_add_tokens__mutmut_11__mutmut_9': x_x_add_tokens__mutmut_11__mutmut_9, 
    'x_x_add_tokens__mutmut_11__mutmut_10': x_x_add_tokens__mutmut_11__mutmut_10, 
    'x_x_add_tokens__mutmut_11__mutmut_11': x_x_add_tokens__mutmut_11__mutmut_11, 
    'x_x_add_tokens__mutmut_11__mutmut_12': x_x_add_tokens__mutmut_11__mutmut_12, 
    'x_x_add_tokens__mutmut_11__mutmut_13': x_x_add_tokens__mutmut_11__mutmut_13, 
    'x_x_add_tokens__mutmut_11__mutmut_14': x_x_add_tokens__mutmut_11__mutmut_14, 
    'x_x_add_tokens__mutmut_11__mutmut_15': x_x_add_tokens__mutmut_11__mutmut_15, 
    'x_x_add_tokens__mutmut_11__mutmut_16': x_x_add_tokens__mutmut_11__mutmut_16
}
x_x_add_tokens__mutmut_11__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_11'


def x_add_tokens__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_12__mutmut_orig, x_x_add_tokens__mutmut_12__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_12__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_12__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_12__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_12__mutmut_1': x_x_add_tokens__mutmut_12__mutmut_1, 
    'x_x_add_tokens__mutmut_12__mutmut_2': x_x_add_tokens__mutmut_12__mutmut_2, 
    'x_x_add_tokens__mutmut_12__mutmut_3': x_x_add_tokens__mutmut_12__mutmut_3, 
    'x_x_add_tokens__mutmut_12__mutmut_4': x_x_add_tokens__mutmut_12__mutmut_4, 
    'x_x_add_tokens__mutmut_12__mutmut_5': x_x_add_tokens__mutmut_12__mutmut_5, 
    'x_x_add_tokens__mutmut_12__mutmut_6': x_x_add_tokens__mutmut_12__mutmut_6, 
    'x_x_add_tokens__mutmut_12__mutmut_7': x_x_add_tokens__mutmut_12__mutmut_7, 
    'x_x_add_tokens__mutmut_12__mutmut_8': x_x_add_tokens__mutmut_12__mutmut_8, 
    'x_x_add_tokens__mutmut_12__mutmut_9': x_x_add_tokens__mutmut_12__mutmut_9, 
    'x_x_add_tokens__mutmut_12__mutmut_10': x_x_add_tokens__mutmut_12__mutmut_10, 
    'x_x_add_tokens__mutmut_12__mutmut_11': x_x_add_tokens__mutmut_12__mutmut_11, 
    'x_x_add_tokens__mutmut_12__mutmut_12': x_x_add_tokens__mutmut_12__mutmut_12, 
    'x_x_add_tokens__mutmut_12__mutmut_13': x_x_add_tokens__mutmut_12__mutmut_13, 
    'x_x_add_tokens__mutmut_12__mutmut_14': x_x_add_tokens__mutmut_12__mutmut_14, 
    'x_x_add_tokens__mutmut_12__mutmut_15': x_x_add_tokens__mutmut_12__mutmut_15, 
    'x_x_add_tokens__mutmut_12__mutmut_16': x_x_add_tokens__mutmut_12__mutmut_16
}
x_x_add_tokens__mutmut_12__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_12'


def x_add_tokens__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_13__mutmut_orig, x_x_add_tokens__mutmut_13__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_13__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_13__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_13__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_13__mutmut_1': x_x_add_tokens__mutmut_13__mutmut_1, 
    'x_x_add_tokens__mutmut_13__mutmut_2': x_x_add_tokens__mutmut_13__mutmut_2, 
    'x_x_add_tokens__mutmut_13__mutmut_3': x_x_add_tokens__mutmut_13__mutmut_3, 
    'x_x_add_tokens__mutmut_13__mutmut_4': x_x_add_tokens__mutmut_13__mutmut_4, 
    'x_x_add_tokens__mutmut_13__mutmut_5': x_x_add_tokens__mutmut_13__mutmut_5, 
    'x_x_add_tokens__mutmut_13__mutmut_6': x_x_add_tokens__mutmut_13__mutmut_6, 
    'x_x_add_tokens__mutmut_13__mutmut_7': x_x_add_tokens__mutmut_13__mutmut_7, 
    'x_x_add_tokens__mutmut_13__mutmut_8': x_x_add_tokens__mutmut_13__mutmut_8, 
    'x_x_add_tokens__mutmut_13__mutmut_9': x_x_add_tokens__mutmut_13__mutmut_9, 
    'x_x_add_tokens__mutmut_13__mutmut_10': x_x_add_tokens__mutmut_13__mutmut_10, 
    'x_x_add_tokens__mutmut_13__mutmut_11': x_x_add_tokens__mutmut_13__mutmut_11, 
    'x_x_add_tokens__mutmut_13__mutmut_12': x_x_add_tokens__mutmut_13__mutmut_12, 
    'x_x_add_tokens__mutmut_13__mutmut_13': x_x_add_tokens__mutmut_13__mutmut_13, 
    'x_x_add_tokens__mutmut_13__mutmut_14': x_x_add_tokens__mutmut_13__mutmut_14, 
    'x_x_add_tokens__mutmut_13__mutmut_15': x_x_add_tokens__mutmut_13__mutmut_15, 
    'x_x_add_tokens__mutmut_13__mutmut_16': x_x_add_tokens__mutmut_13__mutmut_16
}
x_x_add_tokens__mutmut_13__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_13'


def x_add_tokens__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_14__mutmut_orig, x_x_add_tokens__mutmut_14__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_14__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_14__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = ""
    return new_state, within

x_x_add_tokens__mutmut_14__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_14__mutmut_1': x_x_add_tokens__mutmut_14__mutmut_1, 
    'x_x_add_tokens__mutmut_14__mutmut_2': x_x_add_tokens__mutmut_14__mutmut_2, 
    'x_x_add_tokens__mutmut_14__mutmut_3': x_x_add_tokens__mutmut_14__mutmut_3, 
    'x_x_add_tokens__mutmut_14__mutmut_4': x_x_add_tokens__mutmut_14__mutmut_4, 
    'x_x_add_tokens__mutmut_14__mutmut_5': x_x_add_tokens__mutmut_14__mutmut_5, 
    'x_x_add_tokens__mutmut_14__mutmut_6': x_x_add_tokens__mutmut_14__mutmut_6, 
    'x_x_add_tokens__mutmut_14__mutmut_7': x_x_add_tokens__mutmut_14__mutmut_7, 
    'x_x_add_tokens__mutmut_14__mutmut_8': x_x_add_tokens__mutmut_14__mutmut_8, 
    'x_x_add_tokens__mutmut_14__mutmut_9': x_x_add_tokens__mutmut_14__mutmut_9, 
    'x_x_add_tokens__mutmut_14__mutmut_10': x_x_add_tokens__mutmut_14__mutmut_10, 
    'x_x_add_tokens__mutmut_14__mutmut_11': x_x_add_tokens__mutmut_14__mutmut_11, 
    'x_x_add_tokens__mutmut_14__mutmut_12': x_x_add_tokens__mutmut_14__mutmut_12, 
    'x_x_add_tokens__mutmut_14__mutmut_13': x_x_add_tokens__mutmut_14__mutmut_13, 
    'x_x_add_tokens__mutmut_14__mutmut_14': x_x_add_tokens__mutmut_14__mutmut_14
}
x_x_add_tokens__mutmut_14__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_14'


def x_add_tokens__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_15__mutmut_orig, x_x_add_tokens__mutmut_15__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_15__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, None)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_15__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, )
    return new_state, within

x_x_add_tokens__mutmut_15__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_15__mutmut_1': x_x_add_tokens__mutmut_15__mutmut_1, 
    'x_x_add_tokens__mutmut_15__mutmut_2': x_x_add_tokens__mutmut_15__mutmut_2, 
    'x_x_add_tokens__mutmut_15__mutmut_3': x_x_add_tokens__mutmut_15__mutmut_3, 
    'x_x_add_tokens__mutmut_15__mutmut_4': x_x_add_tokens__mutmut_15__mutmut_4, 
    'x_x_add_tokens__mutmut_15__mutmut_5': x_x_add_tokens__mutmut_15__mutmut_5, 
    'x_x_add_tokens__mutmut_15__mutmut_6': x_x_add_tokens__mutmut_15__mutmut_6, 
    'x_x_add_tokens__mutmut_15__mutmut_7': x_x_add_tokens__mutmut_15__mutmut_7, 
    'x_x_add_tokens__mutmut_15__mutmut_8': x_x_add_tokens__mutmut_15__mutmut_8, 
    'x_x_add_tokens__mutmut_15__mutmut_9': x_x_add_tokens__mutmut_15__mutmut_9, 
    'x_x_add_tokens__mutmut_15__mutmut_10': x_x_add_tokens__mutmut_15__mutmut_10, 
    'x_x_add_tokens__mutmut_15__mutmut_11': x_x_add_tokens__mutmut_15__mutmut_11, 
    'x_x_add_tokens__mutmut_15__mutmut_12': x_x_add_tokens__mutmut_15__mutmut_12, 
    'x_x_add_tokens__mutmut_15__mutmut_13': x_x_add_tokens__mutmut_15__mutmut_13, 
    'x_x_add_tokens__mutmut_15__mutmut_14': x_x_add_tokens__mutmut_15__mutmut_14, 
    'x_x_add_tokens__mutmut_15__mutmut_15': x_x_add_tokens__mutmut_15__mutmut_15, 
    'x_x_add_tokens__mutmut_15__mutmut_16': x_x_add_tokens__mutmut_15__mutmut_16, 
    'x_x_add_tokens__mutmut_15__mutmut_17': x_x_add_tokens__mutmut_15__mutmut_17
}
x_x_add_tokens__mutmut_15__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_15'


def x_add_tokens__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_16__mutmut_orig, x_x_add_tokens__mutmut_16__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_16__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_16(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None)
    return new_state, within


def x_x_add_tokens__mutmut_16__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_add_tokens__mutmut_16__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_16__mutmut_1': x_x_add_tokens__mutmut_16__mutmut_1, 
    'x_x_add_tokens__mutmut_16__mutmut_2': x_x_add_tokens__mutmut_16__mutmut_2, 
    'x_x_add_tokens__mutmut_16__mutmut_3': x_x_add_tokens__mutmut_16__mutmut_3, 
    'x_x_add_tokens__mutmut_16__mutmut_4': x_x_add_tokens__mutmut_16__mutmut_4, 
    'x_x_add_tokens__mutmut_16__mutmut_5': x_x_add_tokens__mutmut_16__mutmut_5, 
    'x_x_add_tokens__mutmut_16__mutmut_6': x_x_add_tokens__mutmut_16__mutmut_6, 
    'x_x_add_tokens__mutmut_16__mutmut_7': x_x_add_tokens__mutmut_16__mutmut_7, 
    'x_x_add_tokens__mutmut_16__mutmut_8': x_x_add_tokens__mutmut_16__mutmut_8, 
    'x_x_add_tokens__mutmut_16__mutmut_9': x_x_add_tokens__mutmut_16__mutmut_9, 
    'x_x_add_tokens__mutmut_16__mutmut_10': x_x_add_tokens__mutmut_16__mutmut_10, 
    'x_x_add_tokens__mutmut_16__mutmut_11': x_x_add_tokens__mutmut_16__mutmut_11, 
    'x_x_add_tokens__mutmut_16__mutmut_12': x_x_add_tokens__mutmut_16__mutmut_12, 
    'x_x_add_tokens__mutmut_16__mutmut_13': x_x_add_tokens__mutmut_16__mutmut_13, 
    'x_x_add_tokens__mutmut_16__mutmut_14': x_x_add_tokens__mutmut_16__mutmut_14, 
    'x_x_add_tokens__mutmut_16__mutmut_15': x_x_add_tokens__mutmut_16__mutmut_15, 
    'x_x_add_tokens__mutmut_16__mutmut_16': x_x_add_tokens__mutmut_16__mutmut_16, 
    'x_x_add_tokens__mutmut_16__mutmut_17': x_x_add_tokens__mutmut_16__mutmut_17
}
x_x_add_tokens__mutmut_16__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_16'


def x_add_tokens__mutmut_17(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_17__mutmut_orig, x_x_add_tokens__mutmut_17__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_17__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_17__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None)
    return new_state, within

x_x_add_tokens__mutmut_17__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_17__mutmut_1': x_x_add_tokens__mutmut_17__mutmut_1, 
    'x_x_add_tokens__mutmut_17__mutmut_2': x_x_add_tokens__mutmut_17__mutmut_2, 
    'x_x_add_tokens__mutmut_17__mutmut_3': x_x_add_tokens__mutmut_17__mutmut_3, 
    'x_x_add_tokens__mutmut_17__mutmut_4': x_x_add_tokens__mutmut_17__mutmut_4, 
    'x_x_add_tokens__mutmut_17__mutmut_5': x_x_add_tokens__mutmut_17__mutmut_5, 
    'x_x_add_tokens__mutmut_17__mutmut_6': x_x_add_tokens__mutmut_17__mutmut_6, 
    'x_x_add_tokens__mutmut_17__mutmut_7': x_x_add_tokens__mutmut_17__mutmut_7, 
    'x_x_add_tokens__mutmut_17__mutmut_8': x_x_add_tokens__mutmut_17__mutmut_8, 
    'x_x_add_tokens__mutmut_17__mutmut_9': x_x_add_tokens__mutmut_17__mutmut_9, 
    'x_x_add_tokens__mutmut_17__mutmut_10': x_x_add_tokens__mutmut_17__mutmut_10, 
    'x_x_add_tokens__mutmut_17__mutmut_11': x_x_add_tokens__mutmut_17__mutmut_11, 
    'x_x_add_tokens__mutmut_17__mutmut_12': x_x_add_tokens__mutmut_17__mutmut_12, 
    'x_x_add_tokens__mutmut_17__mutmut_13': x_x_add_tokens__mutmut_17__mutmut_13, 
    'x_x_add_tokens__mutmut_17__mutmut_14': x_x_add_tokens__mutmut_17__mutmut_14, 
    'x_x_add_tokens__mutmut_17__mutmut_15': x_x_add_tokens__mutmut_17__mutmut_15
}
x_x_add_tokens__mutmut_17__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_17'


def x_add_tokens__mutmut_18(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, count, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_add_tokens__mutmut_18__mutmut_orig, x_x_add_tokens__mutmut_18__mutmut_mutants, args, kwargs, None)


def x_x_add_tokens__mutmut_18__mutmut_orig(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_1(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = None
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_2(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used - count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_3(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total >= limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_4(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, True
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_5(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = None
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_6(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_7(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_8(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_9(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_10(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_11(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_12(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_13(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_14(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_add_tokens__mutmut_18__mutmut_15(state: BudgetState, count: int, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_total = state.tokens_used + count
    if new_total > limits.max_tokens:
        return state, False
    new_state = BudgetState(
        tokens_used=new_total,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, )
    return new_state, within

x_x_add_tokens__mutmut_18__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_add_tokens__mutmut_18__mutmut_1': x_x_add_tokens__mutmut_18__mutmut_1, 
    'x_x_add_tokens__mutmut_18__mutmut_2': x_x_add_tokens__mutmut_18__mutmut_2, 
    'x_x_add_tokens__mutmut_18__mutmut_3': x_x_add_tokens__mutmut_18__mutmut_3, 
    'x_x_add_tokens__mutmut_18__mutmut_4': x_x_add_tokens__mutmut_18__mutmut_4, 
    'x_x_add_tokens__mutmut_18__mutmut_5': x_x_add_tokens__mutmut_18__mutmut_5, 
    'x_x_add_tokens__mutmut_18__mutmut_6': x_x_add_tokens__mutmut_18__mutmut_6, 
    'x_x_add_tokens__mutmut_18__mutmut_7': x_x_add_tokens__mutmut_18__mutmut_7, 
    'x_x_add_tokens__mutmut_18__mutmut_8': x_x_add_tokens__mutmut_18__mutmut_8, 
    'x_x_add_tokens__mutmut_18__mutmut_9': x_x_add_tokens__mutmut_18__mutmut_9, 
    'x_x_add_tokens__mutmut_18__mutmut_10': x_x_add_tokens__mutmut_18__mutmut_10, 
    'x_x_add_tokens__mutmut_18__mutmut_11': x_x_add_tokens__mutmut_18__mutmut_11, 
    'x_x_add_tokens__mutmut_18__mutmut_12': x_x_add_tokens__mutmut_18__mutmut_12, 
    'x_x_add_tokens__mutmut_18__mutmut_13': x_x_add_tokens__mutmut_18__mutmut_13, 
    'x_x_add_tokens__mutmut_18__mutmut_14': x_x_add_tokens__mutmut_18__mutmut_14, 
    'x_x_add_tokens__mutmut_18__mutmut_15': x_x_add_tokens__mutmut_18__mutmut_15
}
x_x_add_tokens__mutmut_18__mutmut_orig.__name__ = 'x_x_add_tokens__mutmut_18'

x_add_tokens__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_add_tokens__mutmut_1': x_add_tokens__mutmut_1, 
    'x_add_tokens__mutmut_2': x_add_tokens__mutmut_2, 
    'x_add_tokens__mutmut_3': x_add_tokens__mutmut_3, 
    'x_add_tokens__mutmut_4': x_add_tokens__mutmut_4, 
    'x_add_tokens__mutmut_5': x_add_tokens__mutmut_5, 
    'x_add_tokens__mutmut_6': x_add_tokens__mutmut_6, 
    'x_add_tokens__mutmut_7': x_add_tokens__mutmut_7, 
    'x_add_tokens__mutmut_8': x_add_tokens__mutmut_8, 
    'x_add_tokens__mutmut_9': x_add_tokens__mutmut_9, 
    'x_add_tokens__mutmut_10': x_add_tokens__mutmut_10, 
    'x_add_tokens__mutmut_11': x_add_tokens__mutmut_11, 
    'x_add_tokens__mutmut_12': x_add_tokens__mutmut_12, 
    'x_add_tokens__mutmut_13': x_add_tokens__mutmut_13, 
    'x_add_tokens__mutmut_14': x_add_tokens__mutmut_14, 
    'x_add_tokens__mutmut_15': x_add_tokens__mutmut_15, 
    'x_add_tokens__mutmut_16': x_add_tokens__mutmut_16, 
    'x_add_tokens__mutmut_17': x_add_tokens__mutmut_17, 
    'x_add_tokens__mutmut_18': x_add_tokens__mutmut_18
}
x_add_tokens__mutmut_orig.__name__ = 'x_add_tokens'


def record_tool_call(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, args, kwargs, None)


def x_record_tool_call__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, args, kwargs, None)


def x_record_tool_call__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, args, kwargs, None)


def x_record_tool_call__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, args, kwargs, None)


def x_record_tool_call__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_record_tool_call__mutmut_mutants, args, kwargs, None)


def x_record_tool_call__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, None, args, kwargs, None)


def x_record_tool_call__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, None, kwargs, None)


def x_record_tool_call__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, args, None, None)


def x_record_tool_call__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_mutants, args, kwargs, None)


def x_record_tool_call__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, args, kwargs, None)


def x_record_tool_call__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, kwargs, None)


def x_record_tool_call__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, args, None)


def x_record_tool_call__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_tool_call__mutmut_orig, x_record_tool_call__mutmut_mutants, args, kwargs, )

x_record_tool_call__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_record_tool_call__mutmut_1': x_record_tool_call__mutmut_1, 
    'x_record_tool_call__mutmut_2': x_record_tool_call__mutmut_2, 
    'x_record_tool_call__mutmut_3': x_record_tool_call__mutmut_3, 
    'x_record_tool_call__mutmut_4': x_record_tool_call__mutmut_4, 
    'x_record_tool_call__mutmut_5': x_record_tool_call__mutmut_5, 
    'x_record_tool_call__mutmut_6': x_record_tool_call__mutmut_6, 
    'x_record_tool_call__mutmut_7': x_record_tool_call__mutmut_7, 
    'x_record_tool_call__mutmut_8': x_record_tool_call__mutmut_8, 
    'x_record_tool_call__mutmut_9': x_record_tool_call__mutmut_9, 
    'x_record_tool_call__mutmut_10': x_record_tool_call__mutmut_10, 
    'x_record_tool_call__mutmut_11': x_record_tool_call__mutmut_11
}
x_record_tool_call__mutmut_orig.__name__ = 'x_record_tool_call'


def x_record_tool_call__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_orig__mutmut_orig, x_x_record_tool_call__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_orig__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_orig__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_orig__mutmut_1': x_x_record_tool_call__mutmut_orig__mutmut_1, 
    'x_x_record_tool_call__mutmut_orig__mutmut_2': x_x_record_tool_call__mutmut_orig__mutmut_2, 
    'x_x_record_tool_call__mutmut_orig__mutmut_3': x_x_record_tool_call__mutmut_orig__mutmut_3, 
    'x_x_record_tool_call__mutmut_orig__mutmut_4': x_x_record_tool_call__mutmut_orig__mutmut_4, 
    'x_x_record_tool_call__mutmut_orig__mutmut_5': x_x_record_tool_call__mutmut_orig__mutmut_5, 
    'x_x_record_tool_call__mutmut_orig__mutmut_6': x_x_record_tool_call__mutmut_orig__mutmut_6, 
    'x_x_record_tool_call__mutmut_orig__mutmut_7': x_x_record_tool_call__mutmut_orig__mutmut_7, 
    'x_x_record_tool_call__mutmut_orig__mutmut_8': x_x_record_tool_call__mutmut_orig__mutmut_8, 
    'x_x_record_tool_call__mutmut_orig__mutmut_9': x_x_record_tool_call__mutmut_orig__mutmut_9, 
    'x_x_record_tool_call__mutmut_orig__mutmut_10': x_x_record_tool_call__mutmut_orig__mutmut_10, 
    'x_x_record_tool_call__mutmut_orig__mutmut_11': x_x_record_tool_call__mutmut_orig__mutmut_11, 
    'x_x_record_tool_call__mutmut_orig__mutmut_12': x_x_record_tool_call__mutmut_orig__mutmut_12, 
    'x_x_record_tool_call__mutmut_orig__mutmut_13': x_x_record_tool_call__mutmut_orig__mutmut_13, 
    'x_x_record_tool_call__mutmut_orig__mutmut_14': x_x_record_tool_call__mutmut_orig__mutmut_14, 
    'x_x_record_tool_call__mutmut_orig__mutmut_15': x_x_record_tool_call__mutmut_orig__mutmut_15, 
    'x_x_record_tool_call__mutmut_orig__mutmut_16': x_x_record_tool_call__mutmut_orig__mutmut_16
}
x_x_record_tool_call__mutmut_orig__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_orig'


def x_record_tool_call__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_1__mutmut_orig, x_x_record_tool_call__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_1__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_1__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = ""
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_1__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_1__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_1__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_1__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_1__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_1__mutmut_1': x_x_record_tool_call__mutmut_1__mutmut_1, 
    'x_x_record_tool_call__mutmut_1__mutmut_2': x_x_record_tool_call__mutmut_1__mutmut_2, 
    'x_x_record_tool_call__mutmut_1__mutmut_3': x_x_record_tool_call__mutmut_1__mutmut_3, 
    'x_x_record_tool_call__mutmut_1__mutmut_4': x_x_record_tool_call__mutmut_1__mutmut_4, 
    'x_x_record_tool_call__mutmut_1__mutmut_5': x_x_record_tool_call__mutmut_1__mutmut_5, 
    'x_x_record_tool_call__mutmut_1__mutmut_6': x_x_record_tool_call__mutmut_1__mutmut_6
}
x_x_record_tool_call__mutmut_1__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_1'


def x_record_tool_call__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_2__mutmut_orig, x_x_record_tool_call__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_2__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_2__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_2__mutmut_1': x_x_record_tool_call__mutmut_2__mutmut_1, 
    'x_x_record_tool_call__mutmut_2__mutmut_2': x_x_record_tool_call__mutmut_2__mutmut_2, 
    'x_x_record_tool_call__mutmut_2__mutmut_3': x_x_record_tool_call__mutmut_2__mutmut_3, 
    'x_x_record_tool_call__mutmut_2__mutmut_4': x_x_record_tool_call__mutmut_2__mutmut_4, 
    'x_x_record_tool_call__mutmut_2__mutmut_5': x_x_record_tool_call__mutmut_2__mutmut_5, 
    'x_x_record_tool_call__mutmut_2__mutmut_6': x_x_record_tool_call__mutmut_2__mutmut_6, 
    'x_x_record_tool_call__mutmut_2__mutmut_7': x_x_record_tool_call__mutmut_2__mutmut_7, 
    'x_x_record_tool_call__mutmut_2__mutmut_8': x_x_record_tool_call__mutmut_2__mutmut_8, 
    'x_x_record_tool_call__mutmut_2__mutmut_9': x_x_record_tool_call__mutmut_2__mutmut_9, 
    'x_x_record_tool_call__mutmut_2__mutmut_10': x_x_record_tool_call__mutmut_2__mutmut_10, 
    'x_x_record_tool_call__mutmut_2__mutmut_11': x_x_record_tool_call__mutmut_2__mutmut_11, 
    'x_x_record_tool_call__mutmut_2__mutmut_12': x_x_record_tool_call__mutmut_2__mutmut_12, 
    'x_x_record_tool_call__mutmut_2__mutmut_13': x_x_record_tool_call__mutmut_2__mutmut_13, 
    'x_x_record_tool_call__mutmut_2__mutmut_14': x_x_record_tool_call__mutmut_2__mutmut_14, 
    'x_x_record_tool_call__mutmut_2__mutmut_15': x_x_record_tool_call__mutmut_2__mutmut_15
}
x_x_record_tool_call__mutmut_2__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_2'


def x_record_tool_call__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_3__mutmut_orig, x_x_record_tool_call__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_3__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_3__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_3__mutmut_1': x_x_record_tool_call__mutmut_3__mutmut_1, 
    'x_x_record_tool_call__mutmut_3__mutmut_2': x_x_record_tool_call__mutmut_3__mutmut_2, 
    'x_x_record_tool_call__mutmut_3__mutmut_3': x_x_record_tool_call__mutmut_3__mutmut_3, 
    'x_x_record_tool_call__mutmut_3__mutmut_4': x_x_record_tool_call__mutmut_3__mutmut_4, 
    'x_x_record_tool_call__mutmut_3__mutmut_5': x_x_record_tool_call__mutmut_3__mutmut_5, 
    'x_x_record_tool_call__mutmut_3__mutmut_6': x_x_record_tool_call__mutmut_3__mutmut_6, 
    'x_x_record_tool_call__mutmut_3__mutmut_7': x_x_record_tool_call__mutmut_3__mutmut_7, 
    'x_x_record_tool_call__mutmut_3__mutmut_8': x_x_record_tool_call__mutmut_3__mutmut_8, 
    'x_x_record_tool_call__mutmut_3__mutmut_9': x_x_record_tool_call__mutmut_3__mutmut_9, 
    'x_x_record_tool_call__mutmut_3__mutmut_10': x_x_record_tool_call__mutmut_3__mutmut_10, 
    'x_x_record_tool_call__mutmut_3__mutmut_11': x_x_record_tool_call__mutmut_3__mutmut_11, 
    'x_x_record_tool_call__mutmut_3__mutmut_12': x_x_record_tool_call__mutmut_3__mutmut_12, 
    'x_x_record_tool_call__mutmut_3__mutmut_13': x_x_record_tool_call__mutmut_3__mutmut_13
}
x_x_record_tool_call__mutmut_3__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_3'


def x_record_tool_call__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_4__mutmut_orig, x_x_record_tool_call__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_4__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_4__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_4__mutmut_1': x_x_record_tool_call__mutmut_4__mutmut_1, 
    'x_x_record_tool_call__mutmut_4__mutmut_2': x_x_record_tool_call__mutmut_4__mutmut_2, 
    'x_x_record_tool_call__mutmut_4__mutmut_3': x_x_record_tool_call__mutmut_4__mutmut_3, 
    'x_x_record_tool_call__mutmut_4__mutmut_4': x_x_record_tool_call__mutmut_4__mutmut_4, 
    'x_x_record_tool_call__mutmut_4__mutmut_5': x_x_record_tool_call__mutmut_4__mutmut_5, 
    'x_x_record_tool_call__mutmut_4__mutmut_6': x_x_record_tool_call__mutmut_4__mutmut_6, 
    'x_x_record_tool_call__mutmut_4__mutmut_7': x_x_record_tool_call__mutmut_4__mutmut_7, 
    'x_x_record_tool_call__mutmut_4__mutmut_8': x_x_record_tool_call__mutmut_4__mutmut_8, 
    'x_x_record_tool_call__mutmut_4__mutmut_9': x_x_record_tool_call__mutmut_4__mutmut_9, 
    'x_x_record_tool_call__mutmut_4__mutmut_10': x_x_record_tool_call__mutmut_4__mutmut_10, 
    'x_x_record_tool_call__mutmut_4__mutmut_11': x_x_record_tool_call__mutmut_4__mutmut_11, 
    'x_x_record_tool_call__mutmut_4__mutmut_12': x_x_record_tool_call__mutmut_4__mutmut_12, 
    'x_x_record_tool_call__mutmut_4__mutmut_13': x_x_record_tool_call__mutmut_4__mutmut_13, 
    'x_x_record_tool_call__mutmut_4__mutmut_14': x_x_record_tool_call__mutmut_4__mutmut_14, 
    'x_x_record_tool_call__mutmut_4__mutmut_15': x_x_record_tool_call__mutmut_4__mutmut_15
}
x_x_record_tool_call__mutmut_4__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_4'


def x_record_tool_call__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_5__mutmut_orig, x_x_record_tool_call__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_5__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_5__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_5__mutmut_1': x_x_record_tool_call__mutmut_5__mutmut_1, 
    'x_x_record_tool_call__mutmut_5__mutmut_2': x_x_record_tool_call__mutmut_5__mutmut_2, 
    'x_x_record_tool_call__mutmut_5__mutmut_3': x_x_record_tool_call__mutmut_5__mutmut_3, 
    'x_x_record_tool_call__mutmut_5__mutmut_4': x_x_record_tool_call__mutmut_5__mutmut_4, 
    'x_x_record_tool_call__mutmut_5__mutmut_5': x_x_record_tool_call__mutmut_5__mutmut_5, 
    'x_x_record_tool_call__mutmut_5__mutmut_6': x_x_record_tool_call__mutmut_5__mutmut_6, 
    'x_x_record_tool_call__mutmut_5__mutmut_7': x_x_record_tool_call__mutmut_5__mutmut_7, 
    'x_x_record_tool_call__mutmut_5__mutmut_8': x_x_record_tool_call__mutmut_5__mutmut_8, 
    'x_x_record_tool_call__mutmut_5__mutmut_9': x_x_record_tool_call__mutmut_5__mutmut_9, 
    'x_x_record_tool_call__mutmut_5__mutmut_10': x_x_record_tool_call__mutmut_5__mutmut_10, 
    'x_x_record_tool_call__mutmut_5__mutmut_11': x_x_record_tool_call__mutmut_5__mutmut_11, 
    'x_x_record_tool_call__mutmut_5__mutmut_12': x_x_record_tool_call__mutmut_5__mutmut_12, 
    'x_x_record_tool_call__mutmut_5__mutmut_13': x_x_record_tool_call__mutmut_5__mutmut_13, 
    'x_x_record_tool_call__mutmut_5__mutmut_14': x_x_record_tool_call__mutmut_5__mutmut_14, 
    'x_x_record_tool_call__mutmut_5__mutmut_15': x_x_record_tool_call__mutmut_5__mutmut_15
}
x_x_record_tool_call__mutmut_5__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_5'


def x_record_tool_call__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_6__mutmut_orig, x_x_record_tool_call__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_6__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_6__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_6__mutmut_1': x_x_record_tool_call__mutmut_6__mutmut_1, 
    'x_x_record_tool_call__mutmut_6__mutmut_2': x_x_record_tool_call__mutmut_6__mutmut_2, 
    'x_x_record_tool_call__mutmut_6__mutmut_3': x_x_record_tool_call__mutmut_6__mutmut_3, 
    'x_x_record_tool_call__mutmut_6__mutmut_4': x_x_record_tool_call__mutmut_6__mutmut_4, 
    'x_x_record_tool_call__mutmut_6__mutmut_5': x_x_record_tool_call__mutmut_6__mutmut_5, 
    'x_x_record_tool_call__mutmut_6__mutmut_6': x_x_record_tool_call__mutmut_6__mutmut_6, 
    'x_x_record_tool_call__mutmut_6__mutmut_7': x_x_record_tool_call__mutmut_6__mutmut_7, 
    'x_x_record_tool_call__mutmut_6__mutmut_8': x_x_record_tool_call__mutmut_6__mutmut_8, 
    'x_x_record_tool_call__mutmut_6__mutmut_9': x_x_record_tool_call__mutmut_6__mutmut_9, 
    'x_x_record_tool_call__mutmut_6__mutmut_10': x_x_record_tool_call__mutmut_6__mutmut_10, 
    'x_x_record_tool_call__mutmut_6__mutmut_11': x_x_record_tool_call__mutmut_6__mutmut_11, 
    'x_x_record_tool_call__mutmut_6__mutmut_12': x_x_record_tool_call__mutmut_6__mutmut_12, 
    'x_x_record_tool_call__mutmut_6__mutmut_13': x_x_record_tool_call__mutmut_6__mutmut_13, 
    'x_x_record_tool_call__mutmut_6__mutmut_14': x_x_record_tool_call__mutmut_6__mutmut_14
}
x_x_record_tool_call__mutmut_6__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_6'


def x_record_tool_call__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_7__mutmut_orig, x_x_record_tool_call__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_7__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_7__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_7__mutmut_1': x_x_record_tool_call__mutmut_7__mutmut_1, 
    'x_x_record_tool_call__mutmut_7__mutmut_2': x_x_record_tool_call__mutmut_7__mutmut_2, 
    'x_x_record_tool_call__mutmut_7__mutmut_3': x_x_record_tool_call__mutmut_7__mutmut_3, 
    'x_x_record_tool_call__mutmut_7__mutmut_4': x_x_record_tool_call__mutmut_7__mutmut_4, 
    'x_x_record_tool_call__mutmut_7__mutmut_5': x_x_record_tool_call__mutmut_7__mutmut_5, 
    'x_x_record_tool_call__mutmut_7__mutmut_6': x_x_record_tool_call__mutmut_7__mutmut_6, 
    'x_x_record_tool_call__mutmut_7__mutmut_7': x_x_record_tool_call__mutmut_7__mutmut_7, 
    'x_x_record_tool_call__mutmut_7__mutmut_8': x_x_record_tool_call__mutmut_7__mutmut_8, 
    'x_x_record_tool_call__mutmut_7__mutmut_9': x_x_record_tool_call__mutmut_7__mutmut_9, 
    'x_x_record_tool_call__mutmut_7__mutmut_10': x_x_record_tool_call__mutmut_7__mutmut_10, 
    'x_x_record_tool_call__mutmut_7__mutmut_11': x_x_record_tool_call__mutmut_7__mutmut_11, 
    'x_x_record_tool_call__mutmut_7__mutmut_12': x_x_record_tool_call__mutmut_7__mutmut_12
}
x_x_record_tool_call__mutmut_7__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_7'


def x_record_tool_call__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_8__mutmut_orig, x_x_record_tool_call__mutmut_8__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_8__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_8__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_8__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_8__mutmut_1': x_x_record_tool_call__mutmut_8__mutmut_1, 
    'x_x_record_tool_call__mutmut_8__mutmut_2': x_x_record_tool_call__mutmut_8__mutmut_2, 
    'x_x_record_tool_call__mutmut_8__mutmut_3': x_x_record_tool_call__mutmut_8__mutmut_3, 
    'x_x_record_tool_call__mutmut_8__mutmut_4': x_x_record_tool_call__mutmut_8__mutmut_4, 
    'x_x_record_tool_call__mutmut_8__mutmut_5': x_x_record_tool_call__mutmut_8__mutmut_5, 
    'x_x_record_tool_call__mutmut_8__mutmut_6': x_x_record_tool_call__mutmut_8__mutmut_6, 
    'x_x_record_tool_call__mutmut_8__mutmut_7': x_x_record_tool_call__mutmut_8__mutmut_7, 
    'x_x_record_tool_call__mutmut_8__mutmut_8': x_x_record_tool_call__mutmut_8__mutmut_8, 
    'x_x_record_tool_call__mutmut_8__mutmut_9': x_x_record_tool_call__mutmut_8__mutmut_9, 
    'x_x_record_tool_call__mutmut_8__mutmut_10': x_x_record_tool_call__mutmut_8__mutmut_10, 
    'x_x_record_tool_call__mutmut_8__mutmut_11': x_x_record_tool_call__mutmut_8__mutmut_11, 
    'x_x_record_tool_call__mutmut_8__mutmut_12': x_x_record_tool_call__mutmut_8__mutmut_12, 
    'x_x_record_tool_call__mutmut_8__mutmut_13': x_x_record_tool_call__mutmut_8__mutmut_13, 
    'x_x_record_tool_call__mutmut_8__mutmut_14': x_x_record_tool_call__mutmut_8__mutmut_14
}
x_x_record_tool_call__mutmut_8__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_8'


def x_record_tool_call__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_9__mutmut_orig, x_x_record_tool_call__mutmut_9__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_9__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_9__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_9__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_9__mutmut_1': x_x_record_tool_call__mutmut_9__mutmut_1, 
    'x_x_record_tool_call__mutmut_9__mutmut_2': x_x_record_tool_call__mutmut_9__mutmut_2, 
    'x_x_record_tool_call__mutmut_9__mutmut_3': x_x_record_tool_call__mutmut_9__mutmut_3, 
    'x_x_record_tool_call__mutmut_9__mutmut_4': x_x_record_tool_call__mutmut_9__mutmut_4, 
    'x_x_record_tool_call__mutmut_9__mutmut_5': x_x_record_tool_call__mutmut_9__mutmut_5, 
    'x_x_record_tool_call__mutmut_9__mutmut_6': x_x_record_tool_call__mutmut_9__mutmut_6, 
    'x_x_record_tool_call__mutmut_9__mutmut_7': x_x_record_tool_call__mutmut_9__mutmut_7, 
    'x_x_record_tool_call__mutmut_9__mutmut_8': x_x_record_tool_call__mutmut_9__mutmut_8, 
    'x_x_record_tool_call__mutmut_9__mutmut_9': x_x_record_tool_call__mutmut_9__mutmut_9, 
    'x_x_record_tool_call__mutmut_9__mutmut_10': x_x_record_tool_call__mutmut_9__mutmut_10, 
    'x_x_record_tool_call__mutmut_9__mutmut_11': x_x_record_tool_call__mutmut_9__mutmut_11, 
    'x_x_record_tool_call__mutmut_9__mutmut_12': x_x_record_tool_call__mutmut_9__mutmut_12, 
    'x_x_record_tool_call__mutmut_9__mutmut_13': x_x_record_tool_call__mutmut_9__mutmut_13, 
    'x_x_record_tool_call__mutmut_9__mutmut_14': x_x_record_tool_call__mutmut_9__mutmut_14
}
x_x_record_tool_call__mutmut_9__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_9'


def x_record_tool_call__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_10__mutmut_orig, x_x_record_tool_call__mutmut_10__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_10__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_10__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_10__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_10__mutmut_1': x_x_record_tool_call__mutmut_10__mutmut_1, 
    'x_x_record_tool_call__mutmut_10__mutmut_2': x_x_record_tool_call__mutmut_10__mutmut_2, 
    'x_x_record_tool_call__mutmut_10__mutmut_3': x_x_record_tool_call__mutmut_10__mutmut_3, 
    'x_x_record_tool_call__mutmut_10__mutmut_4': x_x_record_tool_call__mutmut_10__mutmut_4, 
    'x_x_record_tool_call__mutmut_10__mutmut_5': x_x_record_tool_call__mutmut_10__mutmut_5, 
    'x_x_record_tool_call__mutmut_10__mutmut_6': x_x_record_tool_call__mutmut_10__mutmut_6, 
    'x_x_record_tool_call__mutmut_10__mutmut_7': x_x_record_tool_call__mutmut_10__mutmut_7, 
    'x_x_record_tool_call__mutmut_10__mutmut_8': x_x_record_tool_call__mutmut_10__mutmut_8, 
    'x_x_record_tool_call__mutmut_10__mutmut_9': x_x_record_tool_call__mutmut_10__mutmut_9, 
    'x_x_record_tool_call__mutmut_10__mutmut_10': x_x_record_tool_call__mutmut_10__mutmut_10, 
    'x_x_record_tool_call__mutmut_10__mutmut_11': x_x_record_tool_call__mutmut_10__mutmut_11, 
    'x_x_record_tool_call__mutmut_10__mutmut_12': x_x_record_tool_call__mutmut_10__mutmut_12, 
    'x_x_record_tool_call__mutmut_10__mutmut_13': x_x_record_tool_call__mutmut_10__mutmut_13, 
    'x_x_record_tool_call__mutmut_10__mutmut_14': x_x_record_tool_call__mutmut_10__mutmut_14, 
    'x_x_record_tool_call__mutmut_10__mutmut_15': x_x_record_tool_call__mutmut_10__mutmut_15, 
    'x_x_record_tool_call__mutmut_10__mutmut_16': x_x_record_tool_call__mutmut_10__mutmut_16
}
x_x_record_tool_call__mutmut_10__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_10'


def x_record_tool_call__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_11__mutmut_orig, x_x_record_tool_call__mutmut_11__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_11__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 3,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_11__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_11__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_11__mutmut_1': x_x_record_tool_call__mutmut_11__mutmut_1, 
    'x_x_record_tool_call__mutmut_11__mutmut_2': x_x_record_tool_call__mutmut_11__mutmut_2, 
    'x_x_record_tool_call__mutmut_11__mutmut_3': x_x_record_tool_call__mutmut_11__mutmut_3, 
    'x_x_record_tool_call__mutmut_11__mutmut_4': x_x_record_tool_call__mutmut_11__mutmut_4, 
    'x_x_record_tool_call__mutmut_11__mutmut_5': x_x_record_tool_call__mutmut_11__mutmut_5, 
    'x_x_record_tool_call__mutmut_11__mutmut_6': x_x_record_tool_call__mutmut_11__mutmut_6, 
    'x_x_record_tool_call__mutmut_11__mutmut_7': x_x_record_tool_call__mutmut_11__mutmut_7, 
    'x_x_record_tool_call__mutmut_11__mutmut_8': x_x_record_tool_call__mutmut_11__mutmut_8, 
    'x_x_record_tool_call__mutmut_11__mutmut_9': x_x_record_tool_call__mutmut_11__mutmut_9, 
    'x_x_record_tool_call__mutmut_11__mutmut_10': x_x_record_tool_call__mutmut_11__mutmut_10, 
    'x_x_record_tool_call__mutmut_11__mutmut_11': x_x_record_tool_call__mutmut_11__mutmut_11, 
    'x_x_record_tool_call__mutmut_11__mutmut_12': x_x_record_tool_call__mutmut_11__mutmut_12, 
    'x_x_record_tool_call__mutmut_11__mutmut_13': x_x_record_tool_call__mutmut_11__mutmut_13, 
    'x_x_record_tool_call__mutmut_11__mutmut_14': x_x_record_tool_call__mutmut_11__mutmut_14, 
    'x_x_record_tool_call__mutmut_11__mutmut_15': x_x_record_tool_call__mutmut_11__mutmut_15, 
    'x_x_record_tool_call__mutmut_11__mutmut_16': x_x_record_tool_call__mutmut_11__mutmut_16
}
x_x_record_tool_call__mutmut_11__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_11'


def x_record_tool_call__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_12__mutmut_orig, x_x_record_tool_call__mutmut_12__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_12__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_12__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = ""
    return new_state, within

x_x_record_tool_call__mutmut_12__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_12__mutmut_1': x_x_record_tool_call__mutmut_12__mutmut_1, 
    'x_x_record_tool_call__mutmut_12__mutmut_2': x_x_record_tool_call__mutmut_12__mutmut_2, 
    'x_x_record_tool_call__mutmut_12__mutmut_3': x_x_record_tool_call__mutmut_12__mutmut_3, 
    'x_x_record_tool_call__mutmut_12__mutmut_4': x_x_record_tool_call__mutmut_12__mutmut_4, 
    'x_x_record_tool_call__mutmut_12__mutmut_5': x_x_record_tool_call__mutmut_12__mutmut_5, 
    'x_x_record_tool_call__mutmut_12__mutmut_6': x_x_record_tool_call__mutmut_12__mutmut_6, 
    'x_x_record_tool_call__mutmut_12__mutmut_7': x_x_record_tool_call__mutmut_12__mutmut_7, 
    'x_x_record_tool_call__mutmut_12__mutmut_8': x_x_record_tool_call__mutmut_12__mutmut_8, 
    'x_x_record_tool_call__mutmut_12__mutmut_9': x_x_record_tool_call__mutmut_12__mutmut_9, 
    'x_x_record_tool_call__mutmut_12__mutmut_10': x_x_record_tool_call__mutmut_12__mutmut_10, 
    'x_x_record_tool_call__mutmut_12__mutmut_11': x_x_record_tool_call__mutmut_12__mutmut_11, 
    'x_x_record_tool_call__mutmut_12__mutmut_12': x_x_record_tool_call__mutmut_12__mutmut_12
}
x_x_record_tool_call__mutmut_12__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_12'


def x_record_tool_call__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_13__mutmut_orig, x_x_record_tool_call__mutmut_13__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_13__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, None)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_13__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, )
    return new_state, within

x_x_record_tool_call__mutmut_13__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_13__mutmut_1': x_x_record_tool_call__mutmut_13__mutmut_1, 
    'x_x_record_tool_call__mutmut_13__mutmut_2': x_x_record_tool_call__mutmut_13__mutmut_2, 
    'x_x_record_tool_call__mutmut_13__mutmut_3': x_x_record_tool_call__mutmut_13__mutmut_3, 
    'x_x_record_tool_call__mutmut_13__mutmut_4': x_x_record_tool_call__mutmut_13__mutmut_4, 
    'x_x_record_tool_call__mutmut_13__mutmut_5': x_x_record_tool_call__mutmut_13__mutmut_5, 
    'x_x_record_tool_call__mutmut_13__mutmut_6': x_x_record_tool_call__mutmut_13__mutmut_6, 
    'x_x_record_tool_call__mutmut_13__mutmut_7': x_x_record_tool_call__mutmut_13__mutmut_7, 
    'x_x_record_tool_call__mutmut_13__mutmut_8': x_x_record_tool_call__mutmut_13__mutmut_8, 
    'x_x_record_tool_call__mutmut_13__mutmut_9': x_x_record_tool_call__mutmut_13__mutmut_9, 
    'x_x_record_tool_call__mutmut_13__mutmut_10': x_x_record_tool_call__mutmut_13__mutmut_10, 
    'x_x_record_tool_call__mutmut_13__mutmut_11': x_x_record_tool_call__mutmut_13__mutmut_11, 
    'x_x_record_tool_call__mutmut_13__mutmut_12': x_x_record_tool_call__mutmut_13__mutmut_12, 
    'x_x_record_tool_call__mutmut_13__mutmut_13': x_x_record_tool_call__mutmut_13__mutmut_13, 
    'x_x_record_tool_call__mutmut_13__mutmut_14': x_x_record_tool_call__mutmut_13__mutmut_14, 
    'x_x_record_tool_call__mutmut_13__mutmut_15': x_x_record_tool_call__mutmut_13__mutmut_15
}
x_x_record_tool_call__mutmut_13__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_13'


def x_record_tool_call__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_14__mutmut_orig, x_x_record_tool_call__mutmut_14__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_14__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None)
    return new_state, within


def x_x_record_tool_call__mutmut_14__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_tool_call__mutmut_14__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_14__mutmut_1': x_x_record_tool_call__mutmut_14__mutmut_1, 
    'x_x_record_tool_call__mutmut_14__mutmut_2': x_x_record_tool_call__mutmut_14__mutmut_2, 
    'x_x_record_tool_call__mutmut_14__mutmut_3': x_x_record_tool_call__mutmut_14__mutmut_3, 
    'x_x_record_tool_call__mutmut_14__mutmut_4': x_x_record_tool_call__mutmut_14__mutmut_4, 
    'x_x_record_tool_call__mutmut_14__mutmut_5': x_x_record_tool_call__mutmut_14__mutmut_5, 
    'x_x_record_tool_call__mutmut_14__mutmut_6': x_x_record_tool_call__mutmut_14__mutmut_6, 
    'x_x_record_tool_call__mutmut_14__mutmut_7': x_x_record_tool_call__mutmut_14__mutmut_7, 
    'x_x_record_tool_call__mutmut_14__mutmut_8': x_x_record_tool_call__mutmut_14__mutmut_8, 
    'x_x_record_tool_call__mutmut_14__mutmut_9': x_x_record_tool_call__mutmut_14__mutmut_9, 
    'x_x_record_tool_call__mutmut_14__mutmut_10': x_x_record_tool_call__mutmut_14__mutmut_10, 
    'x_x_record_tool_call__mutmut_14__mutmut_11': x_x_record_tool_call__mutmut_14__mutmut_11, 
    'x_x_record_tool_call__mutmut_14__mutmut_12': x_x_record_tool_call__mutmut_14__mutmut_12, 
    'x_x_record_tool_call__mutmut_14__mutmut_13': x_x_record_tool_call__mutmut_14__mutmut_13, 
    'x_x_record_tool_call__mutmut_14__mutmut_14': x_x_record_tool_call__mutmut_14__mutmut_14, 
    'x_x_record_tool_call__mutmut_14__mutmut_15': x_x_record_tool_call__mutmut_14__mutmut_15
}
x_x_record_tool_call__mutmut_14__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_14'


def x_record_tool_call__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_15__mutmut_orig, x_x_record_tool_call__mutmut_15__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_15__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_15__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None)
    return new_state, within

x_x_record_tool_call__mutmut_15__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_15__mutmut_1': x_x_record_tool_call__mutmut_15__mutmut_1, 
    'x_x_record_tool_call__mutmut_15__mutmut_2': x_x_record_tool_call__mutmut_15__mutmut_2, 
    'x_x_record_tool_call__mutmut_15__mutmut_3': x_x_record_tool_call__mutmut_15__mutmut_3, 
    'x_x_record_tool_call__mutmut_15__mutmut_4': x_x_record_tool_call__mutmut_15__mutmut_4, 
    'x_x_record_tool_call__mutmut_15__mutmut_5': x_x_record_tool_call__mutmut_15__mutmut_5, 
    'x_x_record_tool_call__mutmut_15__mutmut_6': x_x_record_tool_call__mutmut_15__mutmut_6, 
    'x_x_record_tool_call__mutmut_15__mutmut_7': x_x_record_tool_call__mutmut_15__mutmut_7, 
    'x_x_record_tool_call__mutmut_15__mutmut_8': x_x_record_tool_call__mutmut_15__mutmut_8, 
    'x_x_record_tool_call__mutmut_15__mutmut_9': x_x_record_tool_call__mutmut_15__mutmut_9, 
    'x_x_record_tool_call__mutmut_15__mutmut_10': x_x_record_tool_call__mutmut_15__mutmut_10, 
    'x_x_record_tool_call__mutmut_15__mutmut_11': x_x_record_tool_call__mutmut_15__mutmut_11, 
    'x_x_record_tool_call__mutmut_15__mutmut_12': x_x_record_tool_call__mutmut_15__mutmut_12, 
    'x_x_record_tool_call__mutmut_15__mutmut_13': x_x_record_tool_call__mutmut_15__mutmut_13
}
x_x_record_tool_call__mutmut_15__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_15'


def x_record_tool_call__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_tool_call__mutmut_16__mutmut_orig, x_x_record_tool_call__mutmut_16__mutmut_mutants, args, kwargs, None)


def x_x_record_tool_call__mutmut_16__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls - 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 2,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_tool_call__mutmut_16__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls + 1,
        consecutive_errors=state.consecutive_errors,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, )
    return new_state, within

x_x_record_tool_call__mutmut_16__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_tool_call__mutmut_16__mutmut_1': x_x_record_tool_call__mutmut_16__mutmut_1, 
    'x_x_record_tool_call__mutmut_16__mutmut_2': x_x_record_tool_call__mutmut_16__mutmut_2, 
    'x_x_record_tool_call__mutmut_16__mutmut_3': x_x_record_tool_call__mutmut_16__mutmut_3, 
    'x_x_record_tool_call__mutmut_16__mutmut_4': x_x_record_tool_call__mutmut_16__mutmut_4, 
    'x_x_record_tool_call__mutmut_16__mutmut_5': x_x_record_tool_call__mutmut_16__mutmut_5, 
    'x_x_record_tool_call__mutmut_16__mutmut_6': x_x_record_tool_call__mutmut_16__mutmut_6, 
    'x_x_record_tool_call__mutmut_16__mutmut_7': x_x_record_tool_call__mutmut_16__mutmut_7, 
    'x_x_record_tool_call__mutmut_16__mutmut_8': x_x_record_tool_call__mutmut_16__mutmut_8, 
    'x_x_record_tool_call__mutmut_16__mutmut_9': x_x_record_tool_call__mutmut_16__mutmut_9, 
    'x_x_record_tool_call__mutmut_16__mutmut_10': x_x_record_tool_call__mutmut_16__mutmut_10, 
    'x_x_record_tool_call__mutmut_16__mutmut_11': x_x_record_tool_call__mutmut_16__mutmut_11, 
    'x_x_record_tool_call__mutmut_16__mutmut_12': x_x_record_tool_call__mutmut_16__mutmut_12, 
    'x_x_record_tool_call__mutmut_16__mutmut_13': x_x_record_tool_call__mutmut_16__mutmut_13
}
x_x_record_tool_call__mutmut_16__mutmut_orig.__name__ = 'x_x_record_tool_call__mutmut_16'

x_record_tool_call__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_record_tool_call__mutmut_1': x_record_tool_call__mutmut_1, 
    'x_record_tool_call__mutmut_2': x_record_tool_call__mutmut_2, 
    'x_record_tool_call__mutmut_3': x_record_tool_call__mutmut_3, 
    'x_record_tool_call__mutmut_4': x_record_tool_call__mutmut_4, 
    'x_record_tool_call__mutmut_5': x_record_tool_call__mutmut_5, 
    'x_record_tool_call__mutmut_6': x_record_tool_call__mutmut_6, 
    'x_record_tool_call__mutmut_7': x_record_tool_call__mutmut_7, 
    'x_record_tool_call__mutmut_8': x_record_tool_call__mutmut_8, 
    'x_record_tool_call__mutmut_9': x_record_tool_call__mutmut_9, 
    'x_record_tool_call__mutmut_10': x_record_tool_call__mutmut_10, 
    'x_record_tool_call__mutmut_11': x_record_tool_call__mutmut_11, 
    'x_record_tool_call__mutmut_12': x_record_tool_call__mutmut_12, 
    'x_record_tool_call__mutmut_13': x_record_tool_call__mutmut_13, 
    'x_record_tool_call__mutmut_14': x_record_tool_call__mutmut_14, 
    'x_record_tool_call__mutmut_15': x_record_tool_call__mutmut_15, 
    'x_record_tool_call__mutmut_16': x_record_tool_call__mutmut_16
}
x_record_tool_call__mutmut_orig.__name__ = 'x_record_tool_call'


def record_error(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, args, kwargs, None)


def x_record_error__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, args, kwargs, None)


def x_record_error__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, args, kwargs, None)


def x_record_error__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, args, kwargs, None)


def x_record_error__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_record_error__mutmut_mutants, args, kwargs, None)


def x_record_error__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, None, args, kwargs, None)


def x_record_error__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, None, kwargs, None)


def x_record_error__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, args, None, None)


def x_record_error__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_mutants, args, kwargs, None)


def x_record_error__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, args, kwargs, None)


def x_record_error__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, kwargs, None)


def x_record_error__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, args, None)


def x_record_error__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_error__mutmut_orig, x_record_error__mutmut_mutants, args, kwargs, )

x_record_error__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_record_error__mutmut_1': x_record_error__mutmut_1, 
    'x_record_error__mutmut_2': x_record_error__mutmut_2, 
    'x_record_error__mutmut_3': x_record_error__mutmut_3, 
    'x_record_error__mutmut_4': x_record_error__mutmut_4, 
    'x_record_error__mutmut_5': x_record_error__mutmut_5, 
    'x_record_error__mutmut_6': x_record_error__mutmut_6, 
    'x_record_error__mutmut_7': x_record_error__mutmut_7, 
    'x_record_error__mutmut_8': x_record_error__mutmut_8, 
    'x_record_error__mutmut_9': x_record_error__mutmut_9, 
    'x_record_error__mutmut_10': x_record_error__mutmut_10, 
    'x_record_error__mutmut_11': x_record_error__mutmut_11
}
x_record_error__mutmut_orig.__name__ = 'x_record_error'


def x_record_error__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_orig__mutmut_orig, x_x_record_error__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_orig__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_orig__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_orig__mutmut_1': x_x_record_error__mutmut_orig__mutmut_1, 
    'x_x_record_error__mutmut_orig__mutmut_2': x_x_record_error__mutmut_orig__mutmut_2, 
    'x_x_record_error__mutmut_orig__mutmut_3': x_x_record_error__mutmut_orig__mutmut_3, 
    'x_x_record_error__mutmut_orig__mutmut_4': x_x_record_error__mutmut_orig__mutmut_4, 
    'x_x_record_error__mutmut_orig__mutmut_5': x_x_record_error__mutmut_orig__mutmut_5, 
    'x_x_record_error__mutmut_orig__mutmut_6': x_x_record_error__mutmut_orig__mutmut_6, 
    'x_x_record_error__mutmut_orig__mutmut_7': x_x_record_error__mutmut_orig__mutmut_7, 
    'x_x_record_error__mutmut_orig__mutmut_8': x_x_record_error__mutmut_orig__mutmut_8, 
    'x_x_record_error__mutmut_orig__mutmut_9': x_x_record_error__mutmut_orig__mutmut_9, 
    'x_x_record_error__mutmut_orig__mutmut_10': x_x_record_error__mutmut_orig__mutmut_10, 
    'x_x_record_error__mutmut_orig__mutmut_11': x_x_record_error__mutmut_orig__mutmut_11, 
    'x_x_record_error__mutmut_orig__mutmut_12': x_x_record_error__mutmut_orig__mutmut_12, 
    'x_x_record_error__mutmut_orig__mutmut_13': x_x_record_error__mutmut_orig__mutmut_13, 
    'x_x_record_error__mutmut_orig__mutmut_14': x_x_record_error__mutmut_orig__mutmut_14, 
    'x_x_record_error__mutmut_orig__mutmut_15': x_x_record_error__mutmut_orig__mutmut_15, 
    'x_x_record_error__mutmut_orig__mutmut_16': x_x_record_error__mutmut_orig__mutmut_16
}
x_x_record_error__mutmut_orig__mutmut_orig.__name__ = 'x_x_record_error__mutmut_orig'


def x_record_error__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_1__mutmut_orig, x_x_record_error__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_1__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_1__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = ""
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_1__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_1__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_1__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_1__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_1__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_1__mutmut_1': x_x_record_error__mutmut_1__mutmut_1, 
    'x_x_record_error__mutmut_1__mutmut_2': x_x_record_error__mutmut_1__mutmut_2, 
    'x_x_record_error__mutmut_1__mutmut_3': x_x_record_error__mutmut_1__mutmut_3, 
    'x_x_record_error__mutmut_1__mutmut_4': x_x_record_error__mutmut_1__mutmut_4, 
    'x_x_record_error__mutmut_1__mutmut_5': x_x_record_error__mutmut_1__mutmut_5, 
    'x_x_record_error__mutmut_1__mutmut_6': x_x_record_error__mutmut_1__mutmut_6
}
x_x_record_error__mutmut_1__mutmut_orig.__name__ = 'x_x_record_error__mutmut_1'


def x_record_error__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_2__mutmut_orig, x_x_record_error__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_2__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_2__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_2__mutmut_1': x_x_record_error__mutmut_2__mutmut_1, 
    'x_x_record_error__mutmut_2__mutmut_2': x_x_record_error__mutmut_2__mutmut_2, 
    'x_x_record_error__mutmut_2__mutmut_3': x_x_record_error__mutmut_2__mutmut_3, 
    'x_x_record_error__mutmut_2__mutmut_4': x_x_record_error__mutmut_2__mutmut_4, 
    'x_x_record_error__mutmut_2__mutmut_5': x_x_record_error__mutmut_2__mutmut_5, 
    'x_x_record_error__mutmut_2__mutmut_6': x_x_record_error__mutmut_2__mutmut_6, 
    'x_x_record_error__mutmut_2__mutmut_7': x_x_record_error__mutmut_2__mutmut_7, 
    'x_x_record_error__mutmut_2__mutmut_8': x_x_record_error__mutmut_2__mutmut_8, 
    'x_x_record_error__mutmut_2__mutmut_9': x_x_record_error__mutmut_2__mutmut_9, 
    'x_x_record_error__mutmut_2__mutmut_10': x_x_record_error__mutmut_2__mutmut_10, 
    'x_x_record_error__mutmut_2__mutmut_11': x_x_record_error__mutmut_2__mutmut_11, 
    'x_x_record_error__mutmut_2__mutmut_12': x_x_record_error__mutmut_2__mutmut_12, 
    'x_x_record_error__mutmut_2__mutmut_13': x_x_record_error__mutmut_2__mutmut_13, 
    'x_x_record_error__mutmut_2__mutmut_14': x_x_record_error__mutmut_2__mutmut_14, 
    'x_x_record_error__mutmut_2__mutmut_15': x_x_record_error__mutmut_2__mutmut_15
}
x_x_record_error__mutmut_2__mutmut_orig.__name__ = 'x_x_record_error__mutmut_2'


def x_record_error__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_3__mutmut_orig, x_x_record_error__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_3__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_3__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_3__mutmut_1': x_x_record_error__mutmut_3__mutmut_1, 
    'x_x_record_error__mutmut_3__mutmut_2': x_x_record_error__mutmut_3__mutmut_2, 
    'x_x_record_error__mutmut_3__mutmut_3': x_x_record_error__mutmut_3__mutmut_3, 
    'x_x_record_error__mutmut_3__mutmut_4': x_x_record_error__mutmut_3__mutmut_4, 
    'x_x_record_error__mutmut_3__mutmut_5': x_x_record_error__mutmut_3__mutmut_5, 
    'x_x_record_error__mutmut_3__mutmut_6': x_x_record_error__mutmut_3__mutmut_6, 
    'x_x_record_error__mutmut_3__mutmut_7': x_x_record_error__mutmut_3__mutmut_7, 
    'x_x_record_error__mutmut_3__mutmut_8': x_x_record_error__mutmut_3__mutmut_8, 
    'x_x_record_error__mutmut_3__mutmut_9': x_x_record_error__mutmut_3__mutmut_9, 
    'x_x_record_error__mutmut_3__mutmut_10': x_x_record_error__mutmut_3__mutmut_10, 
    'x_x_record_error__mutmut_3__mutmut_11': x_x_record_error__mutmut_3__mutmut_11, 
    'x_x_record_error__mutmut_3__mutmut_12': x_x_record_error__mutmut_3__mutmut_12, 
    'x_x_record_error__mutmut_3__mutmut_13': x_x_record_error__mutmut_3__mutmut_13, 
    'x_x_record_error__mutmut_3__mutmut_14': x_x_record_error__mutmut_3__mutmut_14, 
    'x_x_record_error__mutmut_3__mutmut_15': x_x_record_error__mutmut_3__mutmut_15
}
x_x_record_error__mutmut_3__mutmut_orig.__name__ = 'x_x_record_error__mutmut_3'


def x_record_error__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_4__mutmut_orig, x_x_record_error__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_4__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_4__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_4__mutmut_1': x_x_record_error__mutmut_4__mutmut_1, 
    'x_x_record_error__mutmut_4__mutmut_2': x_x_record_error__mutmut_4__mutmut_2, 
    'x_x_record_error__mutmut_4__mutmut_3': x_x_record_error__mutmut_4__mutmut_3, 
    'x_x_record_error__mutmut_4__mutmut_4': x_x_record_error__mutmut_4__mutmut_4, 
    'x_x_record_error__mutmut_4__mutmut_5': x_x_record_error__mutmut_4__mutmut_5, 
    'x_x_record_error__mutmut_4__mutmut_6': x_x_record_error__mutmut_4__mutmut_6, 
    'x_x_record_error__mutmut_4__mutmut_7': x_x_record_error__mutmut_4__mutmut_7, 
    'x_x_record_error__mutmut_4__mutmut_8': x_x_record_error__mutmut_4__mutmut_8, 
    'x_x_record_error__mutmut_4__mutmut_9': x_x_record_error__mutmut_4__mutmut_9, 
    'x_x_record_error__mutmut_4__mutmut_10': x_x_record_error__mutmut_4__mutmut_10, 
    'x_x_record_error__mutmut_4__mutmut_11': x_x_record_error__mutmut_4__mutmut_11, 
    'x_x_record_error__mutmut_4__mutmut_12': x_x_record_error__mutmut_4__mutmut_12, 
    'x_x_record_error__mutmut_4__mutmut_13': x_x_record_error__mutmut_4__mutmut_13
}
x_x_record_error__mutmut_4__mutmut_orig.__name__ = 'x_x_record_error__mutmut_4'


def x_record_error__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_5__mutmut_orig, x_x_record_error__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_5__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_5__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_5__mutmut_1': x_x_record_error__mutmut_5__mutmut_1, 
    'x_x_record_error__mutmut_5__mutmut_2': x_x_record_error__mutmut_5__mutmut_2, 
    'x_x_record_error__mutmut_5__mutmut_3': x_x_record_error__mutmut_5__mutmut_3, 
    'x_x_record_error__mutmut_5__mutmut_4': x_x_record_error__mutmut_5__mutmut_4, 
    'x_x_record_error__mutmut_5__mutmut_5': x_x_record_error__mutmut_5__mutmut_5, 
    'x_x_record_error__mutmut_5__mutmut_6': x_x_record_error__mutmut_5__mutmut_6, 
    'x_x_record_error__mutmut_5__mutmut_7': x_x_record_error__mutmut_5__mutmut_7, 
    'x_x_record_error__mutmut_5__mutmut_8': x_x_record_error__mutmut_5__mutmut_8, 
    'x_x_record_error__mutmut_5__mutmut_9': x_x_record_error__mutmut_5__mutmut_9, 
    'x_x_record_error__mutmut_5__mutmut_10': x_x_record_error__mutmut_5__mutmut_10, 
    'x_x_record_error__mutmut_5__mutmut_11': x_x_record_error__mutmut_5__mutmut_11, 
    'x_x_record_error__mutmut_5__mutmut_12': x_x_record_error__mutmut_5__mutmut_12, 
    'x_x_record_error__mutmut_5__mutmut_13': x_x_record_error__mutmut_5__mutmut_13, 
    'x_x_record_error__mutmut_5__mutmut_14': x_x_record_error__mutmut_5__mutmut_14, 
    'x_x_record_error__mutmut_5__mutmut_15': x_x_record_error__mutmut_5__mutmut_15
}
x_x_record_error__mutmut_5__mutmut_orig.__name__ = 'x_x_record_error__mutmut_5'


def x_record_error__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_6__mutmut_orig, x_x_record_error__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_6__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_6__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_6__mutmut_1': x_x_record_error__mutmut_6__mutmut_1, 
    'x_x_record_error__mutmut_6__mutmut_2': x_x_record_error__mutmut_6__mutmut_2, 
    'x_x_record_error__mutmut_6__mutmut_3': x_x_record_error__mutmut_6__mutmut_3, 
    'x_x_record_error__mutmut_6__mutmut_4': x_x_record_error__mutmut_6__mutmut_4, 
    'x_x_record_error__mutmut_6__mutmut_5': x_x_record_error__mutmut_6__mutmut_5, 
    'x_x_record_error__mutmut_6__mutmut_6': x_x_record_error__mutmut_6__mutmut_6, 
    'x_x_record_error__mutmut_6__mutmut_7': x_x_record_error__mutmut_6__mutmut_7, 
    'x_x_record_error__mutmut_6__mutmut_8': x_x_record_error__mutmut_6__mutmut_8, 
    'x_x_record_error__mutmut_6__mutmut_9': x_x_record_error__mutmut_6__mutmut_9, 
    'x_x_record_error__mutmut_6__mutmut_10': x_x_record_error__mutmut_6__mutmut_10, 
    'x_x_record_error__mutmut_6__mutmut_11': x_x_record_error__mutmut_6__mutmut_11, 
    'x_x_record_error__mutmut_6__mutmut_12': x_x_record_error__mutmut_6__mutmut_12, 
    'x_x_record_error__mutmut_6__mutmut_13': x_x_record_error__mutmut_6__mutmut_13, 
    'x_x_record_error__mutmut_6__mutmut_14': x_x_record_error__mutmut_6__mutmut_14
}
x_x_record_error__mutmut_6__mutmut_orig.__name__ = 'x_x_record_error__mutmut_6'


def x_record_error__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_7__mutmut_orig, x_x_record_error__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_7__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_7__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_7__mutmut_1': x_x_record_error__mutmut_7__mutmut_1, 
    'x_x_record_error__mutmut_7__mutmut_2': x_x_record_error__mutmut_7__mutmut_2, 
    'x_x_record_error__mutmut_7__mutmut_3': x_x_record_error__mutmut_7__mutmut_3, 
    'x_x_record_error__mutmut_7__mutmut_4': x_x_record_error__mutmut_7__mutmut_4, 
    'x_x_record_error__mutmut_7__mutmut_5': x_x_record_error__mutmut_7__mutmut_5, 
    'x_x_record_error__mutmut_7__mutmut_6': x_x_record_error__mutmut_7__mutmut_6, 
    'x_x_record_error__mutmut_7__mutmut_7': x_x_record_error__mutmut_7__mutmut_7, 
    'x_x_record_error__mutmut_7__mutmut_8': x_x_record_error__mutmut_7__mutmut_8, 
    'x_x_record_error__mutmut_7__mutmut_9': x_x_record_error__mutmut_7__mutmut_9, 
    'x_x_record_error__mutmut_7__mutmut_10': x_x_record_error__mutmut_7__mutmut_10, 
    'x_x_record_error__mutmut_7__mutmut_11': x_x_record_error__mutmut_7__mutmut_11, 
    'x_x_record_error__mutmut_7__mutmut_12': x_x_record_error__mutmut_7__mutmut_12, 
    'x_x_record_error__mutmut_7__mutmut_13': x_x_record_error__mutmut_7__mutmut_13, 
    'x_x_record_error__mutmut_7__mutmut_14': x_x_record_error__mutmut_7__mutmut_14
}
x_x_record_error__mutmut_7__mutmut_orig.__name__ = 'x_x_record_error__mutmut_7'


def x_record_error__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_8__mutmut_orig, x_x_record_error__mutmut_8__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_8__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_8__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_8__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_8__mutmut_1': x_x_record_error__mutmut_8__mutmut_1, 
    'x_x_record_error__mutmut_8__mutmut_2': x_x_record_error__mutmut_8__mutmut_2, 
    'x_x_record_error__mutmut_8__mutmut_3': x_x_record_error__mutmut_8__mutmut_3, 
    'x_x_record_error__mutmut_8__mutmut_4': x_x_record_error__mutmut_8__mutmut_4, 
    'x_x_record_error__mutmut_8__mutmut_5': x_x_record_error__mutmut_8__mutmut_5, 
    'x_x_record_error__mutmut_8__mutmut_6': x_x_record_error__mutmut_8__mutmut_6, 
    'x_x_record_error__mutmut_8__mutmut_7': x_x_record_error__mutmut_8__mutmut_7, 
    'x_x_record_error__mutmut_8__mutmut_8': x_x_record_error__mutmut_8__mutmut_8, 
    'x_x_record_error__mutmut_8__mutmut_9': x_x_record_error__mutmut_8__mutmut_9, 
    'x_x_record_error__mutmut_8__mutmut_10': x_x_record_error__mutmut_8__mutmut_10, 
    'x_x_record_error__mutmut_8__mutmut_11': x_x_record_error__mutmut_8__mutmut_11, 
    'x_x_record_error__mutmut_8__mutmut_12': x_x_record_error__mutmut_8__mutmut_12
}
x_x_record_error__mutmut_8__mutmut_orig.__name__ = 'x_x_record_error__mutmut_8'


def x_record_error__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_9__mutmut_orig, x_x_record_error__mutmut_9__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_9__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_9__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_9__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_9__mutmut_1': x_x_record_error__mutmut_9__mutmut_1, 
    'x_x_record_error__mutmut_9__mutmut_2': x_x_record_error__mutmut_9__mutmut_2, 
    'x_x_record_error__mutmut_9__mutmut_3': x_x_record_error__mutmut_9__mutmut_3, 
    'x_x_record_error__mutmut_9__mutmut_4': x_x_record_error__mutmut_9__mutmut_4, 
    'x_x_record_error__mutmut_9__mutmut_5': x_x_record_error__mutmut_9__mutmut_5, 
    'x_x_record_error__mutmut_9__mutmut_6': x_x_record_error__mutmut_9__mutmut_6, 
    'x_x_record_error__mutmut_9__mutmut_7': x_x_record_error__mutmut_9__mutmut_7, 
    'x_x_record_error__mutmut_9__mutmut_8': x_x_record_error__mutmut_9__mutmut_8, 
    'x_x_record_error__mutmut_9__mutmut_9': x_x_record_error__mutmut_9__mutmut_9, 
    'x_x_record_error__mutmut_9__mutmut_10': x_x_record_error__mutmut_9__mutmut_10, 
    'x_x_record_error__mutmut_9__mutmut_11': x_x_record_error__mutmut_9__mutmut_11, 
    'x_x_record_error__mutmut_9__mutmut_12': x_x_record_error__mutmut_9__mutmut_12, 
    'x_x_record_error__mutmut_9__mutmut_13': x_x_record_error__mutmut_9__mutmut_13, 
    'x_x_record_error__mutmut_9__mutmut_14': x_x_record_error__mutmut_9__mutmut_14
}
x_x_record_error__mutmut_9__mutmut_orig.__name__ = 'x_x_record_error__mutmut_9'


def x_record_error__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_10__mutmut_orig, x_x_record_error__mutmut_10__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_10__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_10__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_10__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_10__mutmut_1': x_x_record_error__mutmut_10__mutmut_1, 
    'x_x_record_error__mutmut_10__mutmut_2': x_x_record_error__mutmut_10__mutmut_2, 
    'x_x_record_error__mutmut_10__mutmut_3': x_x_record_error__mutmut_10__mutmut_3, 
    'x_x_record_error__mutmut_10__mutmut_4': x_x_record_error__mutmut_10__mutmut_4, 
    'x_x_record_error__mutmut_10__mutmut_5': x_x_record_error__mutmut_10__mutmut_5, 
    'x_x_record_error__mutmut_10__mutmut_6': x_x_record_error__mutmut_10__mutmut_6, 
    'x_x_record_error__mutmut_10__mutmut_7': x_x_record_error__mutmut_10__mutmut_7, 
    'x_x_record_error__mutmut_10__mutmut_8': x_x_record_error__mutmut_10__mutmut_8, 
    'x_x_record_error__mutmut_10__mutmut_9': x_x_record_error__mutmut_10__mutmut_9, 
    'x_x_record_error__mutmut_10__mutmut_10': x_x_record_error__mutmut_10__mutmut_10, 
    'x_x_record_error__mutmut_10__mutmut_11': x_x_record_error__mutmut_10__mutmut_11, 
    'x_x_record_error__mutmut_10__mutmut_12': x_x_record_error__mutmut_10__mutmut_12, 
    'x_x_record_error__mutmut_10__mutmut_13': x_x_record_error__mutmut_10__mutmut_13, 
    'x_x_record_error__mutmut_10__mutmut_14': x_x_record_error__mutmut_10__mutmut_14, 
    'x_x_record_error__mutmut_10__mutmut_15': x_x_record_error__mutmut_10__mutmut_15, 
    'x_x_record_error__mutmut_10__mutmut_16': x_x_record_error__mutmut_10__mutmut_16
}
x_x_record_error__mutmut_10__mutmut_orig.__name__ = 'x_x_record_error__mutmut_10'


def x_record_error__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_11__mutmut_orig, x_x_record_error__mutmut_11__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_11__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 3,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_11__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_11__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_11__mutmut_1': x_x_record_error__mutmut_11__mutmut_1, 
    'x_x_record_error__mutmut_11__mutmut_2': x_x_record_error__mutmut_11__mutmut_2, 
    'x_x_record_error__mutmut_11__mutmut_3': x_x_record_error__mutmut_11__mutmut_3, 
    'x_x_record_error__mutmut_11__mutmut_4': x_x_record_error__mutmut_11__mutmut_4, 
    'x_x_record_error__mutmut_11__mutmut_5': x_x_record_error__mutmut_11__mutmut_5, 
    'x_x_record_error__mutmut_11__mutmut_6': x_x_record_error__mutmut_11__mutmut_6, 
    'x_x_record_error__mutmut_11__mutmut_7': x_x_record_error__mutmut_11__mutmut_7, 
    'x_x_record_error__mutmut_11__mutmut_8': x_x_record_error__mutmut_11__mutmut_8, 
    'x_x_record_error__mutmut_11__mutmut_9': x_x_record_error__mutmut_11__mutmut_9, 
    'x_x_record_error__mutmut_11__mutmut_10': x_x_record_error__mutmut_11__mutmut_10, 
    'x_x_record_error__mutmut_11__mutmut_11': x_x_record_error__mutmut_11__mutmut_11, 
    'x_x_record_error__mutmut_11__mutmut_12': x_x_record_error__mutmut_11__mutmut_12, 
    'x_x_record_error__mutmut_11__mutmut_13': x_x_record_error__mutmut_11__mutmut_13, 
    'x_x_record_error__mutmut_11__mutmut_14': x_x_record_error__mutmut_11__mutmut_14, 
    'x_x_record_error__mutmut_11__mutmut_15': x_x_record_error__mutmut_11__mutmut_15, 
    'x_x_record_error__mutmut_11__mutmut_16': x_x_record_error__mutmut_11__mutmut_16
}
x_x_record_error__mutmut_11__mutmut_orig.__name__ = 'x_x_record_error__mutmut_11'


def x_record_error__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_12__mutmut_orig, x_x_record_error__mutmut_12__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_12__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_12__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = ""
    return new_state, within

x_x_record_error__mutmut_12__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_12__mutmut_1': x_x_record_error__mutmut_12__mutmut_1, 
    'x_x_record_error__mutmut_12__mutmut_2': x_x_record_error__mutmut_12__mutmut_2, 
    'x_x_record_error__mutmut_12__mutmut_3': x_x_record_error__mutmut_12__mutmut_3, 
    'x_x_record_error__mutmut_12__mutmut_4': x_x_record_error__mutmut_12__mutmut_4, 
    'x_x_record_error__mutmut_12__mutmut_5': x_x_record_error__mutmut_12__mutmut_5, 
    'x_x_record_error__mutmut_12__mutmut_6': x_x_record_error__mutmut_12__mutmut_6, 
    'x_x_record_error__mutmut_12__mutmut_7': x_x_record_error__mutmut_12__mutmut_7, 
    'x_x_record_error__mutmut_12__mutmut_8': x_x_record_error__mutmut_12__mutmut_8, 
    'x_x_record_error__mutmut_12__mutmut_9': x_x_record_error__mutmut_12__mutmut_9, 
    'x_x_record_error__mutmut_12__mutmut_10': x_x_record_error__mutmut_12__mutmut_10, 
    'x_x_record_error__mutmut_12__mutmut_11': x_x_record_error__mutmut_12__mutmut_11, 
    'x_x_record_error__mutmut_12__mutmut_12': x_x_record_error__mutmut_12__mutmut_12
}
x_x_record_error__mutmut_12__mutmut_orig.__name__ = 'x_x_record_error__mutmut_12'


def x_record_error__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_13__mutmut_orig, x_x_record_error__mutmut_13__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_13__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, None)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_13__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, )
    return new_state, within

x_x_record_error__mutmut_13__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_13__mutmut_1': x_x_record_error__mutmut_13__mutmut_1, 
    'x_x_record_error__mutmut_13__mutmut_2': x_x_record_error__mutmut_13__mutmut_2, 
    'x_x_record_error__mutmut_13__mutmut_3': x_x_record_error__mutmut_13__mutmut_3, 
    'x_x_record_error__mutmut_13__mutmut_4': x_x_record_error__mutmut_13__mutmut_4, 
    'x_x_record_error__mutmut_13__mutmut_5': x_x_record_error__mutmut_13__mutmut_5, 
    'x_x_record_error__mutmut_13__mutmut_6': x_x_record_error__mutmut_13__mutmut_6, 
    'x_x_record_error__mutmut_13__mutmut_7': x_x_record_error__mutmut_13__mutmut_7, 
    'x_x_record_error__mutmut_13__mutmut_8': x_x_record_error__mutmut_13__mutmut_8, 
    'x_x_record_error__mutmut_13__mutmut_9': x_x_record_error__mutmut_13__mutmut_9, 
    'x_x_record_error__mutmut_13__mutmut_10': x_x_record_error__mutmut_13__mutmut_10, 
    'x_x_record_error__mutmut_13__mutmut_11': x_x_record_error__mutmut_13__mutmut_11, 
    'x_x_record_error__mutmut_13__mutmut_12': x_x_record_error__mutmut_13__mutmut_12, 
    'x_x_record_error__mutmut_13__mutmut_13': x_x_record_error__mutmut_13__mutmut_13, 
    'x_x_record_error__mutmut_13__mutmut_14': x_x_record_error__mutmut_13__mutmut_14, 
    'x_x_record_error__mutmut_13__mutmut_15': x_x_record_error__mutmut_13__mutmut_15
}
x_x_record_error__mutmut_13__mutmut_orig.__name__ = 'x_x_record_error__mutmut_13'


def x_record_error__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_14__mutmut_orig, x_x_record_error__mutmut_14__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_14__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_14(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None)
    return new_state, within


def x_x_record_error__mutmut_14__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within

x_x_record_error__mutmut_14__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_14__mutmut_1': x_x_record_error__mutmut_14__mutmut_1, 
    'x_x_record_error__mutmut_14__mutmut_2': x_x_record_error__mutmut_14__mutmut_2, 
    'x_x_record_error__mutmut_14__mutmut_3': x_x_record_error__mutmut_14__mutmut_3, 
    'x_x_record_error__mutmut_14__mutmut_4': x_x_record_error__mutmut_14__mutmut_4, 
    'x_x_record_error__mutmut_14__mutmut_5': x_x_record_error__mutmut_14__mutmut_5, 
    'x_x_record_error__mutmut_14__mutmut_6': x_x_record_error__mutmut_14__mutmut_6, 
    'x_x_record_error__mutmut_14__mutmut_7': x_x_record_error__mutmut_14__mutmut_7, 
    'x_x_record_error__mutmut_14__mutmut_8': x_x_record_error__mutmut_14__mutmut_8, 
    'x_x_record_error__mutmut_14__mutmut_9': x_x_record_error__mutmut_14__mutmut_9, 
    'x_x_record_error__mutmut_14__mutmut_10': x_x_record_error__mutmut_14__mutmut_10, 
    'x_x_record_error__mutmut_14__mutmut_11': x_x_record_error__mutmut_14__mutmut_11, 
    'x_x_record_error__mutmut_14__mutmut_12': x_x_record_error__mutmut_14__mutmut_12, 
    'x_x_record_error__mutmut_14__mutmut_13': x_x_record_error__mutmut_14__mutmut_13, 
    'x_x_record_error__mutmut_14__mutmut_14': x_x_record_error__mutmut_14__mutmut_14, 
    'x_x_record_error__mutmut_14__mutmut_15': x_x_record_error__mutmut_14__mutmut_15
}
x_x_record_error__mutmut_14__mutmut_orig.__name__ = 'x_x_record_error__mutmut_14'


def x_record_error__mutmut_15(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_15__mutmut_orig, x_x_record_error__mutmut_15__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_15__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(limits)
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_15__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None)
    return new_state, within

x_x_record_error__mutmut_15__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_15__mutmut_1': x_x_record_error__mutmut_15__mutmut_1, 
    'x_x_record_error__mutmut_15__mutmut_2': x_x_record_error__mutmut_15__mutmut_2, 
    'x_x_record_error__mutmut_15__mutmut_3': x_x_record_error__mutmut_15__mutmut_3, 
    'x_x_record_error__mutmut_15__mutmut_4': x_x_record_error__mutmut_15__mutmut_4, 
    'x_x_record_error__mutmut_15__mutmut_5': x_x_record_error__mutmut_15__mutmut_5, 
    'x_x_record_error__mutmut_15__mutmut_6': x_x_record_error__mutmut_15__mutmut_6, 
    'x_x_record_error__mutmut_15__mutmut_7': x_x_record_error__mutmut_15__mutmut_7, 
    'x_x_record_error__mutmut_15__mutmut_8': x_x_record_error__mutmut_15__mutmut_8, 
    'x_x_record_error__mutmut_15__mutmut_9': x_x_record_error__mutmut_15__mutmut_9, 
    'x_x_record_error__mutmut_15__mutmut_10': x_x_record_error__mutmut_15__mutmut_10, 
    'x_x_record_error__mutmut_15__mutmut_11': x_x_record_error__mutmut_15__mutmut_11, 
    'x_x_record_error__mutmut_15__mutmut_12': x_x_record_error__mutmut_15__mutmut_12, 
    'x_x_record_error__mutmut_15__mutmut_13': x_x_record_error__mutmut_15__mutmut_13
}
x_x_record_error__mutmut_15__mutmut_orig.__name__ = 'x_x_record_error__mutmut_15'


def x_record_error__mutmut_16(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    args = [state, limits]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_error__mutmut_16__mutmut_orig, x_x_record_error__mutmut_16__mutmut_mutants, args, kwargs, None)


def x_x_record_error__mutmut_16__mutmut_orig(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_1(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = None
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_2(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_3(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_4(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_5(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=None,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_6(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_7(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_8(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_9(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_10(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors - 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_11(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 2,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(new_state, )
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_12(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = None
    return new_state, within


def x_x_record_error__mutmut_16__mutmut_13(state: BudgetState, limits: BudgetLimits) -> tuple[BudgetState, bool]:
    new_state = BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=state.consecutive_errors + 1,
        cost_usd=state.cost_usd,
    )
    within, _ = check_budget(None, )
    return new_state, within

x_x_record_error__mutmut_16__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_error__mutmut_16__mutmut_1': x_x_record_error__mutmut_16__mutmut_1, 
    'x_x_record_error__mutmut_16__mutmut_2': x_x_record_error__mutmut_16__mutmut_2, 
    'x_x_record_error__mutmut_16__mutmut_3': x_x_record_error__mutmut_16__mutmut_3, 
    'x_x_record_error__mutmut_16__mutmut_4': x_x_record_error__mutmut_16__mutmut_4, 
    'x_x_record_error__mutmut_16__mutmut_5': x_x_record_error__mutmut_16__mutmut_5, 
    'x_x_record_error__mutmut_16__mutmut_6': x_x_record_error__mutmut_16__mutmut_6, 
    'x_x_record_error__mutmut_16__mutmut_7': x_x_record_error__mutmut_16__mutmut_7, 
    'x_x_record_error__mutmut_16__mutmut_8': x_x_record_error__mutmut_16__mutmut_8, 
    'x_x_record_error__mutmut_16__mutmut_9': x_x_record_error__mutmut_16__mutmut_9, 
    'x_x_record_error__mutmut_16__mutmut_10': x_x_record_error__mutmut_16__mutmut_10, 
    'x_x_record_error__mutmut_16__mutmut_11': x_x_record_error__mutmut_16__mutmut_11, 
    'x_x_record_error__mutmut_16__mutmut_12': x_x_record_error__mutmut_16__mutmut_12, 
    'x_x_record_error__mutmut_16__mutmut_13': x_x_record_error__mutmut_16__mutmut_13
}
x_x_record_error__mutmut_16__mutmut_orig.__name__ = 'x_x_record_error__mutmut_16'

x_record_error__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_record_error__mutmut_1': x_record_error__mutmut_1, 
    'x_record_error__mutmut_2': x_record_error__mutmut_2, 
    'x_record_error__mutmut_3': x_record_error__mutmut_3, 
    'x_record_error__mutmut_4': x_record_error__mutmut_4, 
    'x_record_error__mutmut_5': x_record_error__mutmut_5, 
    'x_record_error__mutmut_6': x_record_error__mutmut_6, 
    'x_record_error__mutmut_7': x_record_error__mutmut_7, 
    'x_record_error__mutmut_8': x_record_error__mutmut_8, 
    'x_record_error__mutmut_9': x_record_error__mutmut_9, 
    'x_record_error__mutmut_10': x_record_error__mutmut_10, 
    'x_record_error__mutmut_11': x_record_error__mutmut_11, 
    'x_record_error__mutmut_12': x_record_error__mutmut_12, 
    'x_record_error__mutmut_13': x_record_error__mutmut_13, 
    'x_record_error__mutmut_14': x_record_error__mutmut_14, 
    'x_record_error__mutmut_15': x_record_error__mutmut_15, 
    'x_record_error__mutmut_16': x_record_error__mutmut_16
}
x_record_error__mutmut_orig.__name__ = 'x_record_error'


def record_success(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, args, kwargs, None)


def x_record_success__mutmut_orig(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, args, kwargs, None)


def x_record_success__mutmut_1(state: BudgetState) -> BudgetState:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, args, kwargs, None)


def x_record_success__mutmut_2(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, args, kwargs, None)


def x_record_success__mutmut_3(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_record_success__mutmut_mutants, args, kwargs, None)


def x_record_success__mutmut_4(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, None, args, kwargs, None)


def x_record_success__mutmut_5(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, None, kwargs, None)


def x_record_success__mutmut_6(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, args, None, None)


def x_record_success__mutmut_7(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_mutants, args, kwargs, None)


def x_record_success__mutmut_8(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, args, kwargs, None)


def x_record_success__mutmut_9(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, kwargs, None)


def x_record_success__mutmut_10(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, args, None)


def x_record_success__mutmut_11(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_record_success__mutmut_orig, x_record_success__mutmut_mutants, args, kwargs, )

x_record_success__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_record_success__mutmut_1': x_record_success__mutmut_1, 
    'x_record_success__mutmut_2': x_record_success__mutmut_2, 
    'x_record_success__mutmut_3': x_record_success__mutmut_3, 
    'x_record_success__mutmut_4': x_record_success__mutmut_4, 
    'x_record_success__mutmut_5': x_record_success__mutmut_5, 
    'x_record_success__mutmut_6': x_record_success__mutmut_6, 
    'x_record_success__mutmut_7': x_record_success__mutmut_7, 
    'x_record_success__mutmut_8': x_record_success__mutmut_8, 
    'x_record_success__mutmut_9': x_record_success__mutmut_9, 
    'x_record_success__mutmut_10': x_record_success__mutmut_10, 
    'x_record_success__mutmut_11': x_record_success__mutmut_11
}
x_record_success__mutmut_orig.__name__ = 'x_record_success'


def x_record_success__mutmut_orig(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_orig__mutmut_orig, x_x_record_success__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_orig__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_orig__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_orig__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_orig__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_orig__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_orig__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_orig__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_orig__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_orig__mutmut_8(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_orig__mutmut_9(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )

x_x_record_success__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_orig__mutmut_1': x_x_record_success__mutmut_orig__mutmut_1, 
    'x_x_record_success__mutmut_orig__mutmut_2': x_x_record_success__mutmut_orig__mutmut_2, 
    'x_x_record_success__mutmut_orig__mutmut_3': x_x_record_success__mutmut_orig__mutmut_3, 
    'x_x_record_success__mutmut_orig__mutmut_4': x_x_record_success__mutmut_orig__mutmut_4, 
    'x_x_record_success__mutmut_orig__mutmut_5': x_x_record_success__mutmut_orig__mutmut_5, 
    'x_x_record_success__mutmut_orig__mutmut_6': x_x_record_success__mutmut_orig__mutmut_6, 
    'x_x_record_success__mutmut_orig__mutmut_7': x_x_record_success__mutmut_orig__mutmut_7, 
    'x_x_record_success__mutmut_orig__mutmut_8': x_x_record_success__mutmut_orig__mutmut_8, 
    'x_x_record_success__mutmut_orig__mutmut_9': x_x_record_success__mutmut_orig__mutmut_9
}
x_x_record_success__mutmut_orig__mutmut_orig.__name__ = 'x_x_record_success__mutmut_orig'


def x_record_success__mutmut_1(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_1__mutmut_orig, x_x_record_success__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_1__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_1__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=None,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_1__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_1__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_1__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_1__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_1__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_1__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_1__mutmut_8(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )

x_x_record_success__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_1__mutmut_1': x_x_record_success__mutmut_1__mutmut_1, 
    'x_x_record_success__mutmut_1__mutmut_2': x_x_record_success__mutmut_1__mutmut_2, 
    'x_x_record_success__mutmut_1__mutmut_3': x_x_record_success__mutmut_1__mutmut_3, 
    'x_x_record_success__mutmut_1__mutmut_4': x_x_record_success__mutmut_1__mutmut_4, 
    'x_x_record_success__mutmut_1__mutmut_5': x_x_record_success__mutmut_1__mutmut_5, 
    'x_x_record_success__mutmut_1__mutmut_6': x_x_record_success__mutmut_1__mutmut_6, 
    'x_x_record_success__mutmut_1__mutmut_7': x_x_record_success__mutmut_1__mutmut_7, 
    'x_x_record_success__mutmut_1__mutmut_8': x_x_record_success__mutmut_1__mutmut_8
}
x_x_record_success__mutmut_1__mutmut_orig.__name__ = 'x_x_record_success__mutmut_1'


def x_record_success__mutmut_2(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_2__mutmut_orig, x_x_record_success__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_2__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_2__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=None,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_2__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_2__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_2__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=None,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_2__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_2__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_2__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_2__mutmut_8(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )

x_x_record_success__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_2__mutmut_1': x_x_record_success__mutmut_2__mutmut_1, 
    'x_x_record_success__mutmut_2__mutmut_2': x_x_record_success__mutmut_2__mutmut_2, 
    'x_x_record_success__mutmut_2__mutmut_3': x_x_record_success__mutmut_2__mutmut_3, 
    'x_x_record_success__mutmut_2__mutmut_4': x_x_record_success__mutmut_2__mutmut_4, 
    'x_x_record_success__mutmut_2__mutmut_5': x_x_record_success__mutmut_2__mutmut_5, 
    'x_x_record_success__mutmut_2__mutmut_6': x_x_record_success__mutmut_2__mutmut_6, 
    'x_x_record_success__mutmut_2__mutmut_7': x_x_record_success__mutmut_2__mutmut_7, 
    'x_x_record_success__mutmut_2__mutmut_8': x_x_record_success__mutmut_2__mutmut_8
}
x_x_record_success__mutmut_2__mutmut_orig.__name__ = 'x_x_record_success__mutmut_2'


def x_record_success__mutmut_3(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_3__mutmut_orig, x_x_record_success__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_3__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_3__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_3__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_3__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=None,
    )


def x_x_record_success__mutmut_3__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_3__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_3__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_3__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        )

x_x_record_success__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_3__mutmut_1': x_x_record_success__mutmut_3__mutmut_1, 
    'x_x_record_success__mutmut_3__mutmut_2': x_x_record_success__mutmut_3__mutmut_2, 
    'x_x_record_success__mutmut_3__mutmut_3': x_x_record_success__mutmut_3__mutmut_3, 
    'x_x_record_success__mutmut_3__mutmut_4': x_x_record_success__mutmut_3__mutmut_4, 
    'x_x_record_success__mutmut_3__mutmut_5': x_x_record_success__mutmut_3__mutmut_5, 
    'x_x_record_success__mutmut_3__mutmut_6': x_x_record_success__mutmut_3__mutmut_6, 
    'x_x_record_success__mutmut_3__mutmut_7': x_x_record_success__mutmut_3__mutmut_7
}
x_x_record_success__mutmut_3__mutmut_orig.__name__ = 'x_x_record_success__mutmut_3'


def x_record_success__mutmut_4(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_4__mutmut_orig, x_x_record_success__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_4__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_4__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_4__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_4__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=None,
    )


def x_x_record_success__mutmut_4__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_4__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_4__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=None,
    )


def x_x_record_success__mutmut_4__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_4__mutmut_8(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        cost_usd=None,
    )

x_x_record_success__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_4__mutmut_1': x_x_record_success__mutmut_4__mutmut_1, 
    'x_x_record_success__mutmut_4__mutmut_2': x_x_record_success__mutmut_4__mutmut_2, 
    'x_x_record_success__mutmut_4__mutmut_3': x_x_record_success__mutmut_4__mutmut_3, 
    'x_x_record_success__mutmut_4__mutmut_4': x_x_record_success__mutmut_4__mutmut_4, 
    'x_x_record_success__mutmut_4__mutmut_5': x_x_record_success__mutmut_4__mutmut_5, 
    'x_x_record_success__mutmut_4__mutmut_6': x_x_record_success__mutmut_4__mutmut_6, 
    'x_x_record_success__mutmut_4__mutmut_7': x_x_record_success__mutmut_4__mutmut_7, 
    'x_x_record_success__mutmut_4__mutmut_8': x_x_record_success__mutmut_4__mutmut_8
}
x_x_record_success__mutmut_4__mutmut_orig.__name__ = 'x_x_record_success__mutmut_4'


def x_record_success__mutmut_5(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_5__mutmut_orig, x_x_record_success__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_5__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_5__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=None,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_5__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_5__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_5__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_5__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_5__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_5__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )

x_x_record_success__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_5__mutmut_1': x_x_record_success__mutmut_5__mutmut_1, 
    'x_x_record_success__mutmut_5__mutmut_2': x_x_record_success__mutmut_5__mutmut_2, 
    'x_x_record_success__mutmut_5__mutmut_3': x_x_record_success__mutmut_5__mutmut_3, 
    'x_x_record_success__mutmut_5__mutmut_4': x_x_record_success__mutmut_5__mutmut_4, 
    'x_x_record_success__mutmut_5__mutmut_5': x_x_record_success__mutmut_5__mutmut_5, 
    'x_x_record_success__mutmut_5__mutmut_6': x_x_record_success__mutmut_5__mutmut_6, 
    'x_x_record_success__mutmut_5__mutmut_7': x_x_record_success__mutmut_5__mutmut_7
}
x_x_record_success__mutmut_5__mutmut_orig.__name__ = 'x_x_record_success__mutmut_5'


def x_record_success__mutmut_6(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_6__mutmut_orig, x_x_record_success__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_6__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_6__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_6__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_6__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=0,
        cost_usd=None,
    )


def x_x_record_success__mutmut_6__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        consecutive_errors=0,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_6__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_6__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_6__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )

x_x_record_success__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_6__mutmut_1': x_x_record_success__mutmut_6__mutmut_1, 
    'x_x_record_success__mutmut_6__mutmut_2': x_x_record_success__mutmut_6__mutmut_2, 
    'x_x_record_success__mutmut_6__mutmut_3': x_x_record_success__mutmut_6__mutmut_3, 
    'x_x_record_success__mutmut_6__mutmut_4': x_x_record_success__mutmut_6__mutmut_4, 
    'x_x_record_success__mutmut_6__mutmut_5': x_x_record_success__mutmut_6__mutmut_5, 
    'x_x_record_success__mutmut_6__mutmut_6': x_x_record_success__mutmut_6__mutmut_6, 
    'x_x_record_success__mutmut_6__mutmut_7': x_x_record_success__mutmut_6__mutmut_7
}
x_x_record_success__mutmut_6__mutmut_orig.__name__ = 'x_x_record_success__mutmut_6'


def x_record_success__mutmut_7(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_7__mutmut_orig, x_x_record_success__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_7__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_7__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_7__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_7__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=None,
    )


def x_x_record_success__mutmut_7__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_7__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_7__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        )

x_x_record_success__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_7__mutmut_1': x_x_record_success__mutmut_7__mutmut_1, 
    'x_x_record_success__mutmut_7__mutmut_2': x_x_record_success__mutmut_7__mutmut_2, 
    'x_x_record_success__mutmut_7__mutmut_3': x_x_record_success__mutmut_7__mutmut_3, 
    'x_x_record_success__mutmut_7__mutmut_4': x_x_record_success__mutmut_7__mutmut_4, 
    'x_x_record_success__mutmut_7__mutmut_5': x_x_record_success__mutmut_7__mutmut_5, 
    'x_x_record_success__mutmut_7__mutmut_6': x_x_record_success__mutmut_7__mutmut_6
}
x_x_record_success__mutmut_7__mutmut_orig.__name__ = 'x_x_record_success__mutmut_7'


def x_record_success__mutmut_8(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_8__mutmut_orig, x_x_record_success__mutmut_8__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_8__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_8__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_8__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_8__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        )


def x_x_record_success__mutmut_8__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_8__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=0,
        )


def x_x_record_success__mutmut_8__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        )


def x_x_record_success__mutmut_8__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        )

x_x_record_success__mutmut_8__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_8__mutmut_1': x_x_record_success__mutmut_8__mutmut_1, 
    'x_x_record_success__mutmut_8__mutmut_2': x_x_record_success__mutmut_8__mutmut_2, 
    'x_x_record_success__mutmut_8__mutmut_3': x_x_record_success__mutmut_8__mutmut_3, 
    'x_x_record_success__mutmut_8__mutmut_4': x_x_record_success__mutmut_8__mutmut_4, 
    'x_x_record_success__mutmut_8__mutmut_5': x_x_record_success__mutmut_8__mutmut_5, 
    'x_x_record_success__mutmut_8__mutmut_6': x_x_record_success__mutmut_8__mutmut_6, 
    'x_x_record_success__mutmut_8__mutmut_7': x_x_record_success__mutmut_8__mutmut_7
}
x_x_record_success__mutmut_8__mutmut_orig.__name__ = 'x_x_record_success__mutmut_8'


def x_record_success__mutmut_9(state: BudgetState) -> BudgetState:
    args = [state]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_record_success__mutmut_9__mutmut_orig, x_x_record_success__mutmut_9__mutmut_mutants, args, kwargs, None)


def x_x_record_success__mutmut_9__mutmut_orig(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_9__mutmut_1(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=None,
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_9__mutmut_2(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=None,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_9__mutmut_3(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=None,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_9__mutmut_4(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        cost_usd=None,
    )


def x_x_record_success__mutmut_9__mutmut_5(state: BudgetState) -> BudgetState:
    return BudgetState(
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_9__mutmut_6(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        consecutive_errors=1,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_9__mutmut_7(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        cost_usd=state.cost_usd,
    )


def x_x_record_success__mutmut_9__mutmut_8(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=1,
        )


def x_x_record_success__mutmut_9__mutmut_9(state: BudgetState) -> BudgetState:
    return BudgetState(
        tokens_used=state.tokens_used,
        tool_calls=state.tool_calls,
        consecutive_errors=2,
        cost_usd=state.cost_usd,
    )

x_x_record_success__mutmut_9__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_record_success__mutmut_9__mutmut_1': x_x_record_success__mutmut_9__mutmut_1, 
    'x_x_record_success__mutmut_9__mutmut_2': x_x_record_success__mutmut_9__mutmut_2, 
    'x_x_record_success__mutmut_9__mutmut_3': x_x_record_success__mutmut_9__mutmut_3, 
    'x_x_record_success__mutmut_9__mutmut_4': x_x_record_success__mutmut_9__mutmut_4, 
    'x_x_record_success__mutmut_9__mutmut_5': x_x_record_success__mutmut_9__mutmut_5, 
    'x_x_record_success__mutmut_9__mutmut_6': x_x_record_success__mutmut_9__mutmut_6, 
    'x_x_record_success__mutmut_9__mutmut_7': x_x_record_success__mutmut_9__mutmut_7, 
    'x_x_record_success__mutmut_9__mutmut_8': x_x_record_success__mutmut_9__mutmut_8, 
    'x_x_record_success__mutmut_9__mutmut_9': x_x_record_success__mutmut_9__mutmut_9
}
x_x_record_success__mutmut_9__mutmut_orig.__name__ = 'x_x_record_success__mutmut_9'

x_record_success__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_record_success__mutmut_1': x_record_success__mutmut_1, 
    'x_record_success__mutmut_2': x_record_success__mutmut_2, 
    'x_record_success__mutmut_3': x_record_success__mutmut_3, 
    'x_record_success__mutmut_4': x_record_success__mutmut_4, 
    'x_record_success__mutmut_5': x_record_success__mutmut_5, 
    'x_record_success__mutmut_6': x_record_success__mutmut_6, 
    'x_record_success__mutmut_7': x_record_success__mutmut_7, 
    'x_record_success__mutmut_8': x_record_success__mutmut_8, 
    'x_record_success__mutmut_9': x_record_success__mutmut_9
}
x_record_success__mutmut_orig.__name__ = 'x_record_success'


_daily_totals: dict[str, float] = {}


def check_daily_budget(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, args, kwargs, None)


def x_check_daily_budget__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, args, kwargs, None)


def x_check_daily_budget__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, args, kwargs, None)


def x_check_daily_budget__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, args, kwargs, None)


def x_check_daily_budget__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_check_daily_budget__mutmut_mutants, args, kwargs, None)


def x_check_daily_budget__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, None, args, kwargs, None)


def x_check_daily_budget__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, None, kwargs, None)


def x_check_daily_budget__mutmut_6(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, args, None, None)


def x_check_daily_budget__mutmut_7(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_mutants, args, kwargs, None)


def x_check_daily_budget__mutmut_8(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, args, kwargs, None)


def x_check_daily_budget__mutmut_9(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, kwargs, None)


def x_check_daily_budget__mutmut_10(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, args, None)


def x_check_daily_budget__mutmut_11(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_daily_budget__mutmut_orig, x_check_daily_budget__mutmut_mutants, args, kwargs, )

x_check_daily_budget__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_daily_budget__mutmut_1': x_check_daily_budget__mutmut_1, 
    'x_check_daily_budget__mutmut_2': x_check_daily_budget__mutmut_2, 
    'x_check_daily_budget__mutmut_3': x_check_daily_budget__mutmut_3, 
    'x_check_daily_budget__mutmut_4': x_check_daily_budget__mutmut_4, 
    'x_check_daily_budget__mutmut_5': x_check_daily_budget__mutmut_5, 
    'x_check_daily_budget__mutmut_6': x_check_daily_budget__mutmut_6, 
    'x_check_daily_budget__mutmut_7': x_check_daily_budget__mutmut_7, 
    'x_check_daily_budget__mutmut_8': x_check_daily_budget__mutmut_8, 
    'x_check_daily_budget__mutmut_9': x_check_daily_budget__mutmut_9, 
    'x_check_daily_budget__mutmut_10': x_check_daily_budget__mutmut_10, 
    'x_check_daily_budget__mutmut_11': x_check_daily_budget__mutmut_11
}
x_check_daily_budget__mutmut_orig.__name__ = 'x_check_daily_budget'


def x_check_daily_budget__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_daily_budget__mutmut_orig__mutmut_orig, x_x_check_daily_budget__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_check_daily_budget__mutmut_orig__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_orig__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_orig__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, 0.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_orig__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, None)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_orig__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(0.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_orig__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, )
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_orig__mutmut_6(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 1.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_orig__mutmut_7(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_orig__mutmut_8(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior + session_cost) < daily_limit

x_x_check_daily_budget__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_daily_budget__mutmut_orig__mutmut_1': x_x_check_daily_budget__mutmut_orig__mutmut_1, 
    'x_x_check_daily_budget__mutmut_orig__mutmut_2': x_x_check_daily_budget__mutmut_orig__mutmut_2, 
    'x_x_check_daily_budget__mutmut_orig__mutmut_3': x_x_check_daily_budget__mutmut_orig__mutmut_3, 
    'x_x_check_daily_budget__mutmut_orig__mutmut_4': x_x_check_daily_budget__mutmut_orig__mutmut_4, 
    'x_x_check_daily_budget__mutmut_orig__mutmut_5': x_x_check_daily_budget__mutmut_orig__mutmut_5, 
    'x_x_check_daily_budget__mutmut_orig__mutmut_6': x_x_check_daily_budget__mutmut_orig__mutmut_6, 
    'x_x_check_daily_budget__mutmut_orig__mutmut_7': x_x_check_daily_budget__mutmut_orig__mutmut_7, 
    'x_x_check_daily_budget__mutmut_orig__mutmut_8': x_x_check_daily_budget__mutmut_orig__mutmut_8
}
x_x_check_daily_budget__mutmut_orig__mutmut_orig.__name__ = 'x_x_check_daily_budget__mutmut_orig'


def x_check_daily_budget__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_daily_budget__mutmut_1__mutmut_orig, x_x_check_daily_budget__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_check_daily_budget__mutmut_1__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_1__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = ""
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_1__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_1__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) < daily_limit

x_x_check_daily_budget__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_daily_budget__mutmut_1__mutmut_1': x_x_check_daily_budget__mutmut_1__mutmut_1, 
    'x_x_check_daily_budget__mutmut_1__mutmut_2': x_x_check_daily_budget__mutmut_1__mutmut_2, 
    'x_x_check_daily_budget__mutmut_1__mutmut_3': x_x_check_daily_budget__mutmut_1__mutmut_3
}
x_x_check_daily_budget__mutmut_1__mutmut_orig.__name__ = 'x_x_check_daily_budget__mutmut_1'


def x_check_daily_budget__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_daily_budget__mutmut_2__mutmut_orig, x_x_check_daily_budget__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_check_daily_budget__mutmut_2__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, 0.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_2__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_2__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, None)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_2__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(0.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_2__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, )
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_2__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, 1.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_2__mutmut_6(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, 0.0)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_2__mutmut_7(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, 0.0)
    return (prior + session_cost) < daily_limit

x_x_check_daily_budget__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_daily_budget__mutmut_2__mutmut_1': x_x_check_daily_budget__mutmut_2__mutmut_1, 
    'x_x_check_daily_budget__mutmut_2__mutmut_2': x_x_check_daily_budget__mutmut_2__mutmut_2, 
    'x_x_check_daily_budget__mutmut_2__mutmut_3': x_x_check_daily_budget__mutmut_2__mutmut_3, 
    'x_x_check_daily_budget__mutmut_2__mutmut_4': x_x_check_daily_budget__mutmut_2__mutmut_4, 
    'x_x_check_daily_budget__mutmut_2__mutmut_5': x_x_check_daily_budget__mutmut_2__mutmut_5, 
    'x_x_check_daily_budget__mutmut_2__mutmut_6': x_x_check_daily_budget__mutmut_2__mutmut_6, 
    'x_x_check_daily_budget__mutmut_2__mutmut_7': x_x_check_daily_budget__mutmut_2__mutmut_7
}
x_x_check_daily_budget__mutmut_2__mutmut_orig.__name__ = 'x_x_check_daily_budget__mutmut_2'


def x_check_daily_budget__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_daily_budget__mutmut_3__mutmut_orig, x_x_check_daily_budget__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_check_daily_budget__mutmut_3__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, None)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_3__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_3__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, None)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_3__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_3__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, )
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_3__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, None)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_3__mutmut_6(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, None)
    return (prior + session_cost) < daily_limit

x_x_check_daily_budget__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_daily_budget__mutmut_3__mutmut_1': x_x_check_daily_budget__mutmut_3__mutmut_1, 
    'x_x_check_daily_budget__mutmut_3__mutmut_2': x_x_check_daily_budget__mutmut_3__mutmut_2, 
    'x_x_check_daily_budget__mutmut_3__mutmut_3': x_x_check_daily_budget__mutmut_3__mutmut_3, 
    'x_x_check_daily_budget__mutmut_3__mutmut_4': x_x_check_daily_budget__mutmut_3__mutmut_4, 
    'x_x_check_daily_budget__mutmut_3__mutmut_5': x_x_check_daily_budget__mutmut_3__mutmut_5, 
    'x_x_check_daily_budget__mutmut_3__mutmut_6': x_x_check_daily_budget__mutmut_3__mutmut_6
}
x_x_check_daily_budget__mutmut_3__mutmut_orig.__name__ = 'x_x_check_daily_budget__mutmut_3'


def x_check_daily_budget__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_daily_budget__mutmut_4__mutmut_orig, x_x_check_daily_budget__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_check_daily_budget__mutmut_4__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(0.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_4__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_4__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_4__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(1.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_4__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(0.0)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_4__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(0.0)
    return (prior + session_cost) < daily_limit

x_x_check_daily_budget__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_daily_budget__mutmut_4__mutmut_1': x_x_check_daily_budget__mutmut_4__mutmut_1, 
    'x_x_check_daily_budget__mutmut_4__mutmut_2': x_x_check_daily_budget__mutmut_4__mutmut_2, 
    'x_x_check_daily_budget__mutmut_4__mutmut_3': x_x_check_daily_budget__mutmut_4__mutmut_3, 
    'x_x_check_daily_budget__mutmut_4__mutmut_4': x_x_check_daily_budget__mutmut_4__mutmut_4, 
    'x_x_check_daily_budget__mutmut_4__mutmut_5': x_x_check_daily_budget__mutmut_4__mutmut_5
}
x_x_check_daily_budget__mutmut_4__mutmut_orig.__name__ = 'x_x_check_daily_budget__mutmut_4'


def x_check_daily_budget__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_daily_budget__mutmut_5__mutmut_orig, x_x_check_daily_budget__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_check_daily_budget__mutmut_5__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, )
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_5__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_5__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, )
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_5__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, )
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_5__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, )
    return (prior + session_cost) < daily_limit

x_x_check_daily_budget__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_daily_budget__mutmut_5__mutmut_1': x_x_check_daily_budget__mutmut_5__mutmut_1, 
    'x_x_check_daily_budget__mutmut_5__mutmut_2': x_x_check_daily_budget__mutmut_5__mutmut_2, 
    'x_x_check_daily_budget__mutmut_5__mutmut_3': x_x_check_daily_budget__mutmut_5__mutmut_3, 
    'x_x_check_daily_budget__mutmut_5__mutmut_4': x_x_check_daily_budget__mutmut_5__mutmut_4
}
x_x_check_daily_budget__mutmut_5__mutmut_orig.__name__ = 'x_x_check_daily_budget__mutmut_5'


def x_check_daily_budget__mutmut_6(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_daily_budget__mutmut_6__mutmut_orig, x_x_check_daily_budget__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_check_daily_budget__mutmut_6__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 1.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_6__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_6__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, 1.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_6__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, None)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_6__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(1.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_6__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, )
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_6__mutmut_6(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 2.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_6__mutmut_7(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 1.0)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_6__mutmut_8(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 1.0)
    return (prior + session_cost) < daily_limit

x_x_check_daily_budget__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_daily_budget__mutmut_6__mutmut_1': x_x_check_daily_budget__mutmut_6__mutmut_1, 
    'x_x_check_daily_budget__mutmut_6__mutmut_2': x_x_check_daily_budget__mutmut_6__mutmut_2, 
    'x_x_check_daily_budget__mutmut_6__mutmut_3': x_x_check_daily_budget__mutmut_6__mutmut_3, 
    'x_x_check_daily_budget__mutmut_6__mutmut_4': x_x_check_daily_budget__mutmut_6__mutmut_4, 
    'x_x_check_daily_budget__mutmut_6__mutmut_5': x_x_check_daily_budget__mutmut_6__mutmut_5, 
    'x_x_check_daily_budget__mutmut_6__mutmut_6': x_x_check_daily_budget__mutmut_6__mutmut_6, 
    'x_x_check_daily_budget__mutmut_6__mutmut_7': x_x_check_daily_budget__mutmut_6__mutmut_7, 
    'x_x_check_daily_budget__mutmut_6__mutmut_8': x_x_check_daily_budget__mutmut_6__mutmut_8
}
x_x_check_daily_budget__mutmut_6__mutmut_orig.__name__ = 'x_x_check_daily_budget__mutmut_6'


def x_check_daily_budget__mutmut_7(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_daily_budget__mutmut_7__mutmut_orig, x_x_check_daily_budget__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_check_daily_budget__mutmut_7__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_7__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_7__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, 0.0)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_7__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, None)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_7__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(0.0)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_7__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, )
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_7__mutmut_6(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 1.0)
    return (prior - session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_7__mutmut_7(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior + session_cost) <= daily_limit


def x_x_check_daily_budget__mutmut_7__mutmut_8(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior - session_cost) < daily_limit

x_x_check_daily_budget__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_daily_budget__mutmut_7__mutmut_1': x_x_check_daily_budget__mutmut_7__mutmut_1, 
    'x_x_check_daily_budget__mutmut_7__mutmut_2': x_x_check_daily_budget__mutmut_7__mutmut_2, 
    'x_x_check_daily_budget__mutmut_7__mutmut_3': x_x_check_daily_budget__mutmut_7__mutmut_3, 
    'x_x_check_daily_budget__mutmut_7__mutmut_4': x_x_check_daily_budget__mutmut_7__mutmut_4, 
    'x_x_check_daily_budget__mutmut_7__mutmut_5': x_x_check_daily_budget__mutmut_7__mutmut_5, 
    'x_x_check_daily_budget__mutmut_7__mutmut_6': x_x_check_daily_budget__mutmut_7__mutmut_6, 
    'x_x_check_daily_budget__mutmut_7__mutmut_7': x_x_check_daily_budget__mutmut_7__mutmut_7, 
    'x_x_check_daily_budget__mutmut_7__mutmut_8': x_x_check_daily_budget__mutmut_7__mutmut_8
}
x_x_check_daily_budget__mutmut_7__mutmut_orig.__name__ = 'x_x_check_daily_budget__mutmut_7'


def x_check_daily_budget__mutmut_8(user_id: str, session_cost: float, daily_limit: float) -> bool:
    args = [user_id, session_cost, daily_limit]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_daily_budget__mutmut_8__mutmut_orig, x_x_check_daily_budget__mutmut_8__mutmut_mutants, args, kwargs, None)


def x_x_check_daily_budget__mutmut_8__mutmut_orig(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior + session_cost) < daily_limit


def x_x_check_daily_budget__mutmut_8__mutmut_1(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = None
    return (prior + session_cost) < daily_limit


def x_x_check_daily_budget__mutmut_8__mutmut_2(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(None, 0.0)
    return (prior + session_cost) < daily_limit


def x_x_check_daily_budget__mutmut_8__mutmut_3(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, None)
    return (prior + session_cost) < daily_limit


def x_x_check_daily_budget__mutmut_8__mutmut_4(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(0.0)
    return (prior + session_cost) < daily_limit


def x_x_check_daily_budget__mutmut_8__mutmut_5(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, )
    return (prior + session_cost) < daily_limit


def x_x_check_daily_budget__mutmut_8__mutmut_6(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 1.0)
    return (prior + session_cost) < daily_limit


def x_x_check_daily_budget__mutmut_8__mutmut_7(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior - session_cost) < daily_limit


def x_x_check_daily_budget__mutmut_8__mutmut_8(user_id: str, session_cost: float, daily_limit: float) -> bool:
    prior = _daily_totals.get(user_id, 0.0)
    return (prior + session_cost) <= daily_limit

x_x_check_daily_budget__mutmut_8__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_daily_budget__mutmut_8__mutmut_1': x_x_check_daily_budget__mutmut_8__mutmut_1, 
    'x_x_check_daily_budget__mutmut_8__mutmut_2': x_x_check_daily_budget__mutmut_8__mutmut_2, 
    'x_x_check_daily_budget__mutmut_8__mutmut_3': x_x_check_daily_budget__mutmut_8__mutmut_3, 
    'x_x_check_daily_budget__mutmut_8__mutmut_4': x_x_check_daily_budget__mutmut_8__mutmut_4, 
    'x_x_check_daily_budget__mutmut_8__mutmut_5': x_x_check_daily_budget__mutmut_8__mutmut_5, 
    'x_x_check_daily_budget__mutmut_8__mutmut_6': x_x_check_daily_budget__mutmut_8__mutmut_6, 
    'x_x_check_daily_budget__mutmut_8__mutmut_7': x_x_check_daily_budget__mutmut_8__mutmut_7, 
    'x_x_check_daily_budget__mutmut_8__mutmut_8': x_x_check_daily_budget__mutmut_8__mutmut_8
}
x_x_check_daily_budget__mutmut_8__mutmut_orig.__name__ = 'x_x_check_daily_budget__mutmut_8'

x_check_daily_budget__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_daily_budget__mutmut_1': x_check_daily_budget__mutmut_1, 
    'x_check_daily_budget__mutmut_2': x_check_daily_budget__mutmut_2, 
    'x_check_daily_budget__mutmut_3': x_check_daily_budget__mutmut_3, 
    'x_check_daily_budget__mutmut_4': x_check_daily_budget__mutmut_4, 
    'x_check_daily_budget__mutmut_5': x_check_daily_budget__mutmut_5, 
    'x_check_daily_budget__mutmut_6': x_check_daily_budget__mutmut_6, 
    'x_check_daily_budget__mutmut_7': x_check_daily_budget__mutmut_7, 
    'x_check_daily_budget__mutmut_8': x_check_daily_budget__mutmut_8
}
x_check_daily_budget__mutmut_orig.__name__ = 'x_check_daily_budget'


def estimate_cost(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, kwargs, None)


def x_estimate_cost__mutmut_orig(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, kwargs, None)


def x_estimate_cost__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, kwargs, None)


def x_estimate_cost__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, kwargs, None)


def x_estimate_cost__mutmut_3(tokens: int, model: str = "default") -> float:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, kwargs, None)


def x_estimate_cost__mutmut_4(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, kwargs, None)


def x_estimate_cost__mutmut_5(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_estimate_cost__mutmut_mutants, args, kwargs, None)


def x_estimate_cost__mutmut_6(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, None, args, kwargs, None)


def x_estimate_cost__mutmut_7(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, None, kwargs, None)


def x_estimate_cost__mutmut_8(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, None, None)


def x_estimate_cost__mutmut_9(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_mutants, args, kwargs, None)


def x_estimate_cost__mutmut_10(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, args, kwargs, None)


def x_estimate_cost__mutmut_11(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, kwargs, None)


def x_estimate_cost__mutmut_12(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, None)


def x_estimate_cost__mutmut_13(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_estimate_cost__mutmut_orig, x_estimate_cost__mutmut_mutants, args, kwargs, )

x_estimate_cost__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_estimate_cost__mutmut_1': x_estimate_cost__mutmut_1, 
    'x_estimate_cost__mutmut_2': x_estimate_cost__mutmut_2, 
    'x_estimate_cost__mutmut_3': x_estimate_cost__mutmut_3, 
    'x_estimate_cost__mutmut_4': x_estimate_cost__mutmut_4, 
    'x_estimate_cost__mutmut_5': x_estimate_cost__mutmut_5, 
    'x_estimate_cost__mutmut_6': x_estimate_cost__mutmut_6, 
    'x_estimate_cost__mutmut_7': x_estimate_cost__mutmut_7, 
    'x_estimate_cost__mutmut_8': x_estimate_cost__mutmut_8, 
    'x_estimate_cost__mutmut_9': x_estimate_cost__mutmut_9, 
    'x_estimate_cost__mutmut_10': x_estimate_cost__mutmut_10, 
    'x_estimate_cost__mutmut_11': x_estimate_cost__mutmut_11, 
    'x_estimate_cost__mutmut_12': x_estimate_cost__mutmut_12, 
    'x_estimate_cost__mutmut_13': x_estimate_cost__mutmut_13
}
x_estimate_cost__mutmut_orig.__name__ = 'x_estimate_cost'


def x_estimate_cost__mutmut_orig(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_orig__mutmut_orig, x_x_estimate_cost__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_orig__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_10(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_orig__mutmut_11(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_orig__mutmut_12(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_orig__mutmut_1': x_x_estimate_cost__mutmut_orig__mutmut_1, 
    'x_x_estimate_cost__mutmut_orig__mutmut_2': x_x_estimate_cost__mutmut_orig__mutmut_2, 
    'x_x_estimate_cost__mutmut_orig__mutmut_3': x_x_estimate_cost__mutmut_orig__mutmut_3, 
    'x_x_estimate_cost__mutmut_orig__mutmut_4': x_x_estimate_cost__mutmut_orig__mutmut_4, 
    'x_x_estimate_cost__mutmut_orig__mutmut_5': x_x_estimate_cost__mutmut_orig__mutmut_5, 
    'x_x_estimate_cost__mutmut_orig__mutmut_6': x_x_estimate_cost__mutmut_orig__mutmut_6, 
    'x_x_estimate_cost__mutmut_orig__mutmut_7': x_x_estimate_cost__mutmut_orig__mutmut_7, 
    'x_x_estimate_cost__mutmut_orig__mutmut_8': x_x_estimate_cost__mutmut_orig__mutmut_8, 
    'x_x_estimate_cost__mutmut_orig__mutmut_9': x_x_estimate_cost__mutmut_orig__mutmut_9, 
    'x_x_estimate_cost__mutmut_orig__mutmut_10': x_x_estimate_cost__mutmut_orig__mutmut_10, 
    'x_x_estimate_cost__mutmut_orig__mutmut_11': x_x_estimate_cost__mutmut_orig__mutmut_11, 
    'x_x_estimate_cost__mutmut_orig__mutmut_12': x_x_estimate_cost__mutmut_orig__mutmut_12
}
x_x_estimate_cost__mutmut_orig__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_orig'


def x_estimate_cost__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_1__mutmut_orig, x_x_estimate_cost__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_1__mutmut_orig(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_1(tokens: int, model: str = "XXXXdefaultXXXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_2(tokens: int, model: str = "xxdefaultxx") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_3(tokens: int, model: str = "XXDEFAULTXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_4(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_5(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_6(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_7(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_8(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_9(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_10(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_11(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_1__mutmut_12(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_1__mutmut_13(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_1__mutmut_1': x_x_estimate_cost__mutmut_1__mutmut_1, 
    'x_x_estimate_cost__mutmut_1__mutmut_2': x_x_estimate_cost__mutmut_1__mutmut_2, 
    'x_x_estimate_cost__mutmut_1__mutmut_3': x_x_estimate_cost__mutmut_1__mutmut_3, 
    'x_x_estimate_cost__mutmut_1__mutmut_4': x_x_estimate_cost__mutmut_1__mutmut_4, 
    'x_x_estimate_cost__mutmut_1__mutmut_5': x_x_estimate_cost__mutmut_1__mutmut_5, 
    'x_x_estimate_cost__mutmut_1__mutmut_6': x_x_estimate_cost__mutmut_1__mutmut_6, 
    'x_x_estimate_cost__mutmut_1__mutmut_7': x_x_estimate_cost__mutmut_1__mutmut_7, 
    'x_x_estimate_cost__mutmut_1__mutmut_8': x_x_estimate_cost__mutmut_1__mutmut_8, 
    'x_x_estimate_cost__mutmut_1__mutmut_9': x_x_estimate_cost__mutmut_1__mutmut_9, 
    'x_x_estimate_cost__mutmut_1__mutmut_10': x_x_estimate_cost__mutmut_1__mutmut_10, 
    'x_x_estimate_cost__mutmut_1__mutmut_11': x_x_estimate_cost__mutmut_1__mutmut_11, 
    'x_x_estimate_cost__mutmut_1__mutmut_12': x_x_estimate_cost__mutmut_1__mutmut_12, 
    'x_x_estimate_cost__mutmut_1__mutmut_13': x_x_estimate_cost__mutmut_1__mutmut_13
}
x_x_estimate_cost__mutmut_1__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_1'


def x_estimate_cost__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_2__mutmut_orig, x_x_estimate_cost__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_2__mutmut_orig(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_1(tokens: int, model: str = "XXDEFAULTXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_2(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_3(tokens: int, model: str = "DEFAULT") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_4(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_5(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_6(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_7(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_8(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_9(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_10(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_2__mutmut_11(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_2__mutmut_12(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_2__mutmut_1': x_x_estimate_cost__mutmut_2__mutmut_1, 
    'x_x_estimate_cost__mutmut_2__mutmut_2': x_x_estimate_cost__mutmut_2__mutmut_2, 
    'x_x_estimate_cost__mutmut_2__mutmut_3': x_x_estimate_cost__mutmut_2__mutmut_3, 
    'x_x_estimate_cost__mutmut_2__mutmut_4': x_x_estimate_cost__mutmut_2__mutmut_4, 
    'x_x_estimate_cost__mutmut_2__mutmut_5': x_x_estimate_cost__mutmut_2__mutmut_5, 
    'x_x_estimate_cost__mutmut_2__mutmut_6': x_x_estimate_cost__mutmut_2__mutmut_6, 
    'x_x_estimate_cost__mutmut_2__mutmut_7': x_x_estimate_cost__mutmut_2__mutmut_7, 
    'x_x_estimate_cost__mutmut_2__mutmut_8': x_x_estimate_cost__mutmut_2__mutmut_8, 
    'x_x_estimate_cost__mutmut_2__mutmut_9': x_x_estimate_cost__mutmut_2__mutmut_9, 
    'x_x_estimate_cost__mutmut_2__mutmut_10': x_x_estimate_cost__mutmut_2__mutmut_10, 
    'x_x_estimate_cost__mutmut_2__mutmut_11': x_x_estimate_cost__mutmut_2__mutmut_11, 
    'x_x_estimate_cost__mutmut_2__mutmut_12': x_x_estimate_cost__mutmut_2__mutmut_12
}
x_x_estimate_cost__mutmut_2__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_2'


def x_estimate_cost__mutmut_3(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_3__mutmut_orig, x_x_estimate_cost__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_3__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_3__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_3__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_3__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = ""
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_3__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_3__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_3__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_3__mutmut_1': x_x_estimate_cost__mutmut_3__mutmut_1, 
    'x_x_estimate_cost__mutmut_3__mutmut_2': x_x_estimate_cost__mutmut_3__mutmut_2, 
    'x_x_estimate_cost__mutmut_3__mutmut_3': x_x_estimate_cost__mutmut_3__mutmut_3, 
    'x_x_estimate_cost__mutmut_3__mutmut_4': x_x_estimate_cost__mutmut_3__mutmut_4, 
    'x_x_estimate_cost__mutmut_3__mutmut_5': x_x_estimate_cost__mutmut_3__mutmut_5, 
    'x_x_estimate_cost__mutmut_3__mutmut_6': x_x_estimate_cost__mutmut_3__mutmut_6
}
x_x_estimate_cost__mutmut_3__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_3'


def x_estimate_cost__mutmut_4(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_4__mutmut_orig, x_x_estimate_cost__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_4__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_4__mutmut_10(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_4__mutmut_11(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_4__mutmut_1': x_x_estimate_cost__mutmut_4__mutmut_1, 
    'x_x_estimate_cost__mutmut_4__mutmut_2': x_x_estimate_cost__mutmut_4__mutmut_2, 
    'x_x_estimate_cost__mutmut_4__mutmut_3': x_x_estimate_cost__mutmut_4__mutmut_3, 
    'x_x_estimate_cost__mutmut_4__mutmut_4': x_x_estimate_cost__mutmut_4__mutmut_4, 
    'x_x_estimate_cost__mutmut_4__mutmut_5': x_x_estimate_cost__mutmut_4__mutmut_5, 
    'x_x_estimate_cost__mutmut_4__mutmut_6': x_x_estimate_cost__mutmut_4__mutmut_6, 
    'x_x_estimate_cost__mutmut_4__mutmut_7': x_x_estimate_cost__mutmut_4__mutmut_7, 
    'x_x_estimate_cost__mutmut_4__mutmut_8': x_x_estimate_cost__mutmut_4__mutmut_8, 
    'x_x_estimate_cost__mutmut_4__mutmut_9': x_x_estimate_cost__mutmut_4__mutmut_9, 
    'x_x_estimate_cost__mutmut_4__mutmut_10': x_x_estimate_cost__mutmut_4__mutmut_10, 
    'x_x_estimate_cost__mutmut_4__mutmut_11': x_x_estimate_cost__mutmut_4__mutmut_11
}
x_x_estimate_cost__mutmut_4__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_4'


def x_estimate_cost__mutmut_5(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_5__mutmut_orig, x_x_estimate_cost__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_5__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_5__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_5__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_5__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_5__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_5__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_5__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_5__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_5__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_5__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_5__mutmut_1': x_x_estimate_cost__mutmut_5__mutmut_1, 
    'x_x_estimate_cost__mutmut_5__mutmut_2': x_x_estimate_cost__mutmut_5__mutmut_2, 
    'x_x_estimate_cost__mutmut_5__mutmut_3': x_x_estimate_cost__mutmut_5__mutmut_3, 
    'x_x_estimate_cost__mutmut_5__mutmut_4': x_x_estimate_cost__mutmut_5__mutmut_4, 
    'x_x_estimate_cost__mutmut_5__mutmut_5': x_x_estimate_cost__mutmut_5__mutmut_5, 
    'x_x_estimate_cost__mutmut_5__mutmut_6': x_x_estimate_cost__mutmut_5__mutmut_6, 
    'x_x_estimate_cost__mutmut_5__mutmut_7': x_x_estimate_cost__mutmut_5__mutmut_7, 
    'x_x_estimate_cost__mutmut_5__mutmut_8': x_x_estimate_cost__mutmut_5__mutmut_8, 
    'x_x_estimate_cost__mutmut_5__mutmut_9': x_x_estimate_cost__mutmut_5__mutmut_9
}
x_x_estimate_cost__mutmut_5__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_5'


def x_estimate_cost__mutmut_6(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_6__mutmut_orig, x_x_estimate_cost__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_6__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_6__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_6__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_6__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_6__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_6__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_6__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_6__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_6__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_6__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_6__mutmut_1': x_x_estimate_cost__mutmut_6__mutmut_1, 
    'x_x_estimate_cost__mutmut_6__mutmut_2': x_x_estimate_cost__mutmut_6__mutmut_2, 
    'x_x_estimate_cost__mutmut_6__mutmut_3': x_x_estimate_cost__mutmut_6__mutmut_3, 
    'x_x_estimate_cost__mutmut_6__mutmut_4': x_x_estimate_cost__mutmut_6__mutmut_4, 
    'x_x_estimate_cost__mutmut_6__mutmut_5': x_x_estimate_cost__mutmut_6__mutmut_5, 
    'x_x_estimate_cost__mutmut_6__mutmut_6': x_x_estimate_cost__mutmut_6__mutmut_6, 
    'x_x_estimate_cost__mutmut_6__mutmut_7': x_x_estimate_cost__mutmut_6__mutmut_7, 
    'x_x_estimate_cost__mutmut_6__mutmut_8': x_x_estimate_cost__mutmut_6__mutmut_8, 
    'x_x_estimate_cost__mutmut_6__mutmut_9': x_x_estimate_cost__mutmut_6__mutmut_9
}
x_x_estimate_cost__mutmut_6__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_6'


def x_estimate_cost__mutmut_7(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_7__mutmut_orig, x_x_estimate_cost__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_7__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_7__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_7__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_7__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_7__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_7__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_7__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_7__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_7__mutmut_1': x_x_estimate_cost__mutmut_7__mutmut_1, 
    'x_x_estimate_cost__mutmut_7__mutmut_2': x_x_estimate_cost__mutmut_7__mutmut_2, 
    'x_x_estimate_cost__mutmut_7__mutmut_3': x_x_estimate_cost__mutmut_7__mutmut_3, 
    'x_x_estimate_cost__mutmut_7__mutmut_4': x_x_estimate_cost__mutmut_7__mutmut_4, 
    'x_x_estimate_cost__mutmut_7__mutmut_5': x_x_estimate_cost__mutmut_7__mutmut_5, 
    'x_x_estimate_cost__mutmut_7__mutmut_6': x_x_estimate_cost__mutmut_7__mutmut_6, 
    'x_x_estimate_cost__mutmut_7__mutmut_7': x_x_estimate_cost__mutmut_7__mutmut_7
}
x_x_estimate_cost__mutmut_7__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_7'


def x_estimate_cost__mutmut_8(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_8__mutmut_orig, x_x_estimate_cost__mutmut_8__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_8__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXXXdefaultXXXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["xxdefaultxx"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_10(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXDEFAULTXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_11(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_8__mutmut_12(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_8__mutmut_13(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_8__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_8__mutmut_1': x_x_estimate_cost__mutmut_8__mutmut_1, 
    'x_x_estimate_cost__mutmut_8__mutmut_2': x_x_estimate_cost__mutmut_8__mutmut_2, 
    'x_x_estimate_cost__mutmut_8__mutmut_3': x_x_estimate_cost__mutmut_8__mutmut_3, 
    'x_x_estimate_cost__mutmut_8__mutmut_4': x_x_estimate_cost__mutmut_8__mutmut_4, 
    'x_x_estimate_cost__mutmut_8__mutmut_5': x_x_estimate_cost__mutmut_8__mutmut_5, 
    'x_x_estimate_cost__mutmut_8__mutmut_6': x_x_estimate_cost__mutmut_8__mutmut_6, 
    'x_x_estimate_cost__mutmut_8__mutmut_7': x_x_estimate_cost__mutmut_8__mutmut_7, 
    'x_x_estimate_cost__mutmut_8__mutmut_8': x_x_estimate_cost__mutmut_8__mutmut_8, 
    'x_x_estimate_cost__mutmut_8__mutmut_9': x_x_estimate_cost__mutmut_8__mutmut_9, 
    'x_x_estimate_cost__mutmut_8__mutmut_10': x_x_estimate_cost__mutmut_8__mutmut_10, 
    'x_x_estimate_cost__mutmut_8__mutmut_11': x_x_estimate_cost__mutmut_8__mutmut_11, 
    'x_x_estimate_cost__mutmut_8__mutmut_12': x_x_estimate_cost__mutmut_8__mutmut_12, 
    'x_x_estimate_cost__mutmut_8__mutmut_13': x_x_estimate_cost__mutmut_8__mutmut_13
}
x_x_estimate_cost__mutmut_8__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_8'


def x_estimate_cost__mutmut_9(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_9__mutmut_orig, x_x_estimate_cost__mutmut_9__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_9__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXDEFAULTXX"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_10(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_9__mutmut_11(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_9__mutmut_12(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1001) * rate

x_x_estimate_cost__mutmut_9__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_9__mutmut_1': x_x_estimate_cost__mutmut_9__mutmut_1, 
    'x_x_estimate_cost__mutmut_9__mutmut_2': x_x_estimate_cost__mutmut_9__mutmut_2, 
    'x_x_estimate_cost__mutmut_9__mutmut_3': x_x_estimate_cost__mutmut_9__mutmut_3, 
    'x_x_estimate_cost__mutmut_9__mutmut_4': x_x_estimate_cost__mutmut_9__mutmut_4, 
    'x_x_estimate_cost__mutmut_9__mutmut_5': x_x_estimate_cost__mutmut_9__mutmut_5, 
    'x_x_estimate_cost__mutmut_9__mutmut_6': x_x_estimate_cost__mutmut_9__mutmut_6, 
    'x_x_estimate_cost__mutmut_9__mutmut_7': x_x_estimate_cost__mutmut_9__mutmut_7, 
    'x_x_estimate_cost__mutmut_9__mutmut_8': x_x_estimate_cost__mutmut_9__mutmut_8, 
    'x_x_estimate_cost__mutmut_9__mutmut_9': x_x_estimate_cost__mutmut_9__mutmut_9, 
    'x_x_estimate_cost__mutmut_9__mutmut_10': x_x_estimate_cost__mutmut_9__mutmut_10, 
    'x_x_estimate_cost__mutmut_9__mutmut_11': x_x_estimate_cost__mutmut_9__mutmut_11, 
    'x_x_estimate_cost__mutmut_9__mutmut_12': x_x_estimate_cost__mutmut_9__mutmut_12
}
x_x_estimate_cost__mutmut_9__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_9'


def x_estimate_cost__mutmut_10(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_10__mutmut_orig, x_x_estimate_cost__mutmut_10__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_10__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_10(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_10__mutmut_11(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) / rate


def x_x_estimate_cost__mutmut_10__mutmut_12(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) / rate

x_x_estimate_cost__mutmut_10__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_10__mutmut_1': x_x_estimate_cost__mutmut_10__mutmut_1, 
    'x_x_estimate_cost__mutmut_10__mutmut_2': x_x_estimate_cost__mutmut_10__mutmut_2, 
    'x_x_estimate_cost__mutmut_10__mutmut_3': x_x_estimate_cost__mutmut_10__mutmut_3, 
    'x_x_estimate_cost__mutmut_10__mutmut_4': x_x_estimate_cost__mutmut_10__mutmut_4, 
    'x_x_estimate_cost__mutmut_10__mutmut_5': x_x_estimate_cost__mutmut_10__mutmut_5, 
    'x_x_estimate_cost__mutmut_10__mutmut_6': x_x_estimate_cost__mutmut_10__mutmut_6, 
    'x_x_estimate_cost__mutmut_10__mutmut_7': x_x_estimate_cost__mutmut_10__mutmut_7, 
    'x_x_estimate_cost__mutmut_10__mutmut_8': x_x_estimate_cost__mutmut_10__mutmut_8, 
    'x_x_estimate_cost__mutmut_10__mutmut_9': x_x_estimate_cost__mutmut_10__mutmut_9, 
    'x_x_estimate_cost__mutmut_10__mutmut_10': x_x_estimate_cost__mutmut_10__mutmut_10, 
    'x_x_estimate_cost__mutmut_10__mutmut_11': x_x_estimate_cost__mutmut_10__mutmut_11, 
    'x_x_estimate_cost__mutmut_10__mutmut_12': x_x_estimate_cost__mutmut_10__mutmut_12
}
x_x_estimate_cost__mutmut_10__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_10'


def x_estimate_cost__mutmut_11(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_11__mutmut_orig, x_x_estimate_cost__mutmut_11__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_11__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens * 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_10(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1000) / rate


def x_x_estimate_cost__mutmut_11__mutmut_11(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1000) * rate


def x_x_estimate_cost__mutmut_11__mutmut_12(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1001) * rate

x_x_estimate_cost__mutmut_11__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_11__mutmut_1': x_x_estimate_cost__mutmut_11__mutmut_1, 
    'x_x_estimate_cost__mutmut_11__mutmut_2': x_x_estimate_cost__mutmut_11__mutmut_2, 
    'x_x_estimate_cost__mutmut_11__mutmut_3': x_x_estimate_cost__mutmut_11__mutmut_3, 
    'x_x_estimate_cost__mutmut_11__mutmut_4': x_x_estimate_cost__mutmut_11__mutmut_4, 
    'x_x_estimate_cost__mutmut_11__mutmut_5': x_x_estimate_cost__mutmut_11__mutmut_5, 
    'x_x_estimate_cost__mutmut_11__mutmut_6': x_x_estimate_cost__mutmut_11__mutmut_6, 
    'x_x_estimate_cost__mutmut_11__mutmut_7': x_x_estimate_cost__mutmut_11__mutmut_7, 
    'x_x_estimate_cost__mutmut_11__mutmut_8': x_x_estimate_cost__mutmut_11__mutmut_8, 
    'x_x_estimate_cost__mutmut_11__mutmut_9': x_x_estimate_cost__mutmut_11__mutmut_9, 
    'x_x_estimate_cost__mutmut_11__mutmut_10': x_x_estimate_cost__mutmut_11__mutmut_10, 
    'x_x_estimate_cost__mutmut_11__mutmut_11': x_x_estimate_cost__mutmut_11__mutmut_11, 
    'x_x_estimate_cost__mutmut_11__mutmut_12': x_x_estimate_cost__mutmut_11__mutmut_12
}
x_x_estimate_cost__mutmut_11__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_11'


def x_estimate_cost__mutmut_12(tokens: int, model: str = "default") -> float:
    args = [tokens, model]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_estimate_cost__mutmut_12__mutmut_orig, x_x_estimate_cost__mutmut_12__mutmut_mutants, args, kwargs, None)


def x_x_estimate_cost__mutmut_12__mutmut_orig(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_1(tokens: int, model: str = "XXdefaultXX") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_2(tokens: int, model: str = "DEFAULT") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_3(tokens: int, model: str = "default") -> float:
    rate = None
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_4(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(None, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_5(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, None)
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_6(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(_DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_7(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, )
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_8(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["XXdefaultXX"])
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_9(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["DEFAULT"])
    return (tokens / 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_10(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1001) / rate


def x_x_estimate_cost__mutmut_12__mutmut_11(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens * 1001) * rate


def x_x_estimate_cost__mutmut_12__mutmut_12(tokens: int, model: str = "default") -> float:
    rate = _DEFAULT_COST_PER_1K_TOKENS.get(model, _DEFAULT_COST_PER_1K_TOKENS["default"])
    return (tokens / 1002) * rate

x_x_estimate_cost__mutmut_12__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_estimate_cost__mutmut_12__mutmut_1': x_x_estimate_cost__mutmut_12__mutmut_1, 
    'x_x_estimate_cost__mutmut_12__mutmut_2': x_x_estimate_cost__mutmut_12__mutmut_2, 
    'x_x_estimate_cost__mutmut_12__mutmut_3': x_x_estimate_cost__mutmut_12__mutmut_3, 
    'x_x_estimate_cost__mutmut_12__mutmut_4': x_x_estimate_cost__mutmut_12__mutmut_4, 
    'x_x_estimate_cost__mutmut_12__mutmut_5': x_x_estimate_cost__mutmut_12__mutmut_5, 
    'x_x_estimate_cost__mutmut_12__mutmut_6': x_x_estimate_cost__mutmut_12__mutmut_6, 
    'x_x_estimate_cost__mutmut_12__mutmut_7': x_x_estimate_cost__mutmut_12__mutmut_7, 
    'x_x_estimate_cost__mutmut_12__mutmut_8': x_x_estimate_cost__mutmut_12__mutmut_8, 
    'x_x_estimate_cost__mutmut_12__mutmut_9': x_x_estimate_cost__mutmut_12__mutmut_9, 
    'x_x_estimate_cost__mutmut_12__mutmut_10': x_x_estimate_cost__mutmut_12__mutmut_10, 
    'x_x_estimate_cost__mutmut_12__mutmut_11': x_x_estimate_cost__mutmut_12__mutmut_11, 
    'x_x_estimate_cost__mutmut_12__mutmut_12': x_x_estimate_cost__mutmut_12__mutmut_12
}
x_x_estimate_cost__mutmut_12__mutmut_orig.__name__ = 'x_x_estimate_cost__mutmut_12'

x_estimate_cost__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_estimate_cost__mutmut_1': x_estimate_cost__mutmut_1, 
    'x_estimate_cost__mutmut_2': x_estimate_cost__mutmut_2, 
    'x_estimate_cost__mutmut_3': x_estimate_cost__mutmut_3, 
    'x_estimate_cost__mutmut_4': x_estimate_cost__mutmut_4, 
    'x_estimate_cost__mutmut_5': x_estimate_cost__mutmut_5, 
    'x_estimate_cost__mutmut_6': x_estimate_cost__mutmut_6, 
    'x_estimate_cost__mutmut_7': x_estimate_cost__mutmut_7, 
    'x_estimate_cost__mutmut_8': x_estimate_cost__mutmut_8, 
    'x_estimate_cost__mutmut_9': x_estimate_cost__mutmut_9, 
    'x_estimate_cost__mutmut_10': x_estimate_cost__mutmut_10, 
    'x_estimate_cost__mutmut_11': x_estimate_cost__mutmut_11, 
    'x_estimate_cost__mutmut_12': x_estimate_cost__mutmut_12
}
x_estimate_cost__mutmut_orig.__name__ = 'x_estimate_cost'
