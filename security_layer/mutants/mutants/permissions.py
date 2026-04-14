import os
import re
from enum import Enum

from security_layer.state_machine import StateMachine
from security_layer.models import AgentCapabilities, TaintFlag, ToolPermission
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


class CapabilityState(str, Enum):
    FULL = "FULL"
    STANDARD = "STANDARD"
    READ_ONLY = "READ_ONLY"
    LOCKED = "LOCKED"


class CapabilityEvent(str, Enum):
    RESTRICT_STANDARD = "RESTRICT_STANDARD"
    RESTRICT_READ_ONLY = "RESTRICT_READ_ONLY"
    LOCK = "LOCK"
    FULL = "FULL"
    STANDARD = "STANDARD"
    READ_ONLY = "READ_ONLY"


def _noop(context):
    pass


capability_sm = StateMachine[CapabilityState, CapabilityEvent, dict]()
capability_sm.add_transition(CapabilityState.FULL, CapabilityEvent.RESTRICT_STANDARD, CapabilityState.STANDARD, _noop)
capability_sm.add_transition(
    CapabilityState.STANDARD, CapabilityEvent.RESTRICT_READ_ONLY, CapabilityState.READ_ONLY, _noop
)
capability_sm.add_transition(CapabilityState.READ_ONLY, CapabilityEvent.LOCK, CapabilityState.LOCKED, _noop)


def resolve_path(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, args, kwargs, None)


def x_resolve_path__mutmut_orig(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, args, kwargs, None)


def x_resolve_path__mutmut_1(path: str, workspace_root: str) -> str:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, args, kwargs, None)


def x_resolve_path__mutmut_2(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, args, kwargs, None)


def x_resolve_path__mutmut_3(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_resolve_path__mutmut_mutants, args, kwargs, None)


def x_resolve_path__mutmut_4(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, None, args, kwargs, None)


def x_resolve_path__mutmut_5(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, None, kwargs, None)


def x_resolve_path__mutmut_6(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, args, None, None)


def x_resolve_path__mutmut_7(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_mutants, args, kwargs, None)


def x_resolve_path__mutmut_8(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, args, kwargs, None)


def x_resolve_path__mutmut_9(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, kwargs, None)


def x_resolve_path__mutmut_10(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, args, None)


def x_resolve_path__mutmut_11(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_path__mutmut_orig, x_resolve_path__mutmut_mutants, args, kwargs, )

x_resolve_path__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_resolve_path__mutmut_1': x_resolve_path__mutmut_1, 
    'x_resolve_path__mutmut_2': x_resolve_path__mutmut_2, 
    'x_resolve_path__mutmut_3': x_resolve_path__mutmut_3, 
    'x_resolve_path__mutmut_4': x_resolve_path__mutmut_4, 
    'x_resolve_path__mutmut_5': x_resolve_path__mutmut_5, 
    'x_resolve_path__mutmut_6': x_resolve_path__mutmut_6, 
    'x_resolve_path__mutmut_7': x_resolve_path__mutmut_7, 
    'x_resolve_path__mutmut_8': x_resolve_path__mutmut_8, 
    'x_resolve_path__mutmut_9': x_resolve_path__mutmut_9, 
    'x_resolve_path__mutmut_10': x_resolve_path__mutmut_10, 
    'x_resolve_path__mutmut_11': x_resolve_path__mutmut_11
}
x_resolve_path__mutmut_orig.__name__ = 'x_resolve_path'


def x_resolve_path__mutmut_orig(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_resolve_path__mutmut_orig__mutmut_orig, x_x_resolve_path__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_resolve_path__mutmut_orig__mutmut_orig(path: str, workspace_root: str) -> str:
    return os.path.normpath(path)


def x_x_resolve_path__mutmut_orig__mutmut_1(path: str, workspace_root: str) -> str:
    return os.path.normpath(None)

x_x_resolve_path__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_resolve_path__mutmut_orig__mutmut_1': x_x_resolve_path__mutmut_orig__mutmut_1
}
x_x_resolve_path__mutmut_orig__mutmut_orig.__name__ = 'x_x_resolve_path__mutmut_orig'


def x_resolve_path__mutmut_1(path: str, workspace_root: str) -> str:
    return os.path.normpath(None)

x_resolve_path__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_resolve_path__mutmut_1': x_resolve_path__mutmut_1
}
x_resolve_path__mutmut_orig.__name__ = 'x_resolve_path'


def is_path_allowed(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, args, kwargs, None)


def x_is_path_allowed__mutmut_orig(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, args, kwargs, None)


def x_is_path_allowed__mutmut_1(path: str, workspace_root: str) -> str:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, args, kwargs, None)


def x_is_path_allowed__mutmut_2(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, args, kwargs, None)


def x_is_path_allowed__mutmut_3(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_is_path_allowed__mutmut_mutants, args, kwargs, None)


def x_is_path_allowed__mutmut_4(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, None, args, kwargs, None)


def x_is_path_allowed__mutmut_5(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, None, kwargs, None)


def x_is_path_allowed__mutmut_6(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, args, None, None)


def x_is_path_allowed__mutmut_7(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_mutants, args, kwargs, None)


def x_is_path_allowed__mutmut_8(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, args, kwargs, None)


def x_is_path_allowed__mutmut_9(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, kwargs, None)


def x_is_path_allowed__mutmut_10(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, args, None)


def x_is_path_allowed__mutmut_11(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_path_allowed__mutmut_orig, x_is_path_allowed__mutmut_mutants, args, kwargs, )

x_is_path_allowed__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_is_path_allowed__mutmut_1': x_is_path_allowed__mutmut_1, 
    'x_is_path_allowed__mutmut_2': x_is_path_allowed__mutmut_2, 
    'x_is_path_allowed__mutmut_3': x_is_path_allowed__mutmut_3, 
    'x_is_path_allowed__mutmut_4': x_is_path_allowed__mutmut_4, 
    'x_is_path_allowed__mutmut_5': x_is_path_allowed__mutmut_5, 
    'x_is_path_allowed__mutmut_6': x_is_path_allowed__mutmut_6, 
    'x_is_path_allowed__mutmut_7': x_is_path_allowed__mutmut_7, 
    'x_is_path_allowed__mutmut_8': x_is_path_allowed__mutmut_8, 
    'x_is_path_allowed__mutmut_9': x_is_path_allowed__mutmut_9, 
    'x_is_path_allowed__mutmut_10': x_is_path_allowed__mutmut_10, 
    'x_is_path_allowed__mutmut_11': x_is_path_allowed__mutmut_11
}
x_is_path_allowed__mutmut_orig.__name__ = 'x_is_path_allowed'


def x_is_path_allowed__mutmut_orig(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_path_allowed__mutmut_orig__mutmut_orig, x_x_is_path_allowed__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_is_path_allowed__mutmut_orig__mutmut_orig(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_orig__mutmut_1(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_orig__mutmut_2(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_orig__mutmut_3(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_orig__mutmut_4(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_orig__mutmut_5(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_orig__mutmut_6(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_orig__mutmut_7(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)

x_x_is_path_allowed__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_path_allowed__mutmut_orig__mutmut_1': x_x_is_path_allowed__mutmut_orig__mutmut_1, 
    'x_x_is_path_allowed__mutmut_orig__mutmut_2': x_x_is_path_allowed__mutmut_orig__mutmut_2, 
    'x_x_is_path_allowed__mutmut_orig__mutmut_3': x_x_is_path_allowed__mutmut_orig__mutmut_3, 
    'x_x_is_path_allowed__mutmut_orig__mutmut_4': x_x_is_path_allowed__mutmut_orig__mutmut_4, 
    'x_x_is_path_allowed__mutmut_orig__mutmut_5': x_x_is_path_allowed__mutmut_orig__mutmut_5, 
    'x_x_is_path_allowed__mutmut_orig__mutmut_6': x_x_is_path_allowed__mutmut_orig__mutmut_6, 
    'x_x_is_path_allowed__mutmut_orig__mutmut_7': x_x_is_path_allowed__mutmut_orig__mutmut_7
}
x_x_is_path_allowed__mutmut_orig__mutmut_orig.__name__ = 'x_x_is_path_allowed__mutmut_orig'


def x_is_path_allowed__mutmut_1(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_path_allowed__mutmut_1__mutmut_orig, x_x_is_path_allowed__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_is_path_allowed__mutmut_1__mutmut_orig(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_1__mutmut_1(path: str, workspace_root: str) -> str:
    resolved = ""
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_1__mutmut_2(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_1__mutmut_3(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_1__mutmut_4(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_1__mutmut_5(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_1__mutmut_6(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)

x_x_is_path_allowed__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_path_allowed__mutmut_1__mutmut_1': x_x_is_path_allowed__mutmut_1__mutmut_1, 
    'x_x_is_path_allowed__mutmut_1__mutmut_2': x_x_is_path_allowed__mutmut_1__mutmut_2, 
    'x_x_is_path_allowed__mutmut_1__mutmut_3': x_x_is_path_allowed__mutmut_1__mutmut_3, 
    'x_x_is_path_allowed__mutmut_1__mutmut_4': x_x_is_path_allowed__mutmut_1__mutmut_4, 
    'x_x_is_path_allowed__mutmut_1__mutmut_5': x_x_is_path_allowed__mutmut_1__mutmut_5, 
    'x_x_is_path_allowed__mutmut_1__mutmut_6': x_x_is_path_allowed__mutmut_1__mutmut_6
}
x_x_is_path_allowed__mutmut_1__mutmut_orig.__name__ = 'x_x_is_path_allowed__mutmut_1'


def x_is_path_allowed__mutmut_2(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_path_allowed__mutmut_2__mutmut_orig, x_x_is_path_allowed__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_is_path_allowed__mutmut_2__mutmut_orig(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_2__mutmut_1(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_2__mutmut_2(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_2__mutmut_3(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_2__mutmut_4(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_2__mutmut_5(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_2__mutmut_6(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)

x_x_is_path_allowed__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_path_allowed__mutmut_2__mutmut_1': x_x_is_path_allowed__mutmut_2__mutmut_1, 
    'x_x_is_path_allowed__mutmut_2__mutmut_2': x_x_is_path_allowed__mutmut_2__mutmut_2, 
    'x_x_is_path_allowed__mutmut_2__mutmut_3': x_x_is_path_allowed__mutmut_2__mutmut_3, 
    'x_x_is_path_allowed__mutmut_2__mutmut_4': x_x_is_path_allowed__mutmut_2__mutmut_4, 
    'x_x_is_path_allowed__mutmut_2__mutmut_5': x_x_is_path_allowed__mutmut_2__mutmut_5, 
    'x_x_is_path_allowed__mutmut_2__mutmut_6': x_x_is_path_allowed__mutmut_2__mutmut_6
}
x_x_is_path_allowed__mutmut_2__mutmut_orig.__name__ = 'x_x_is_path_allowed__mutmut_2'


def x_is_path_allowed__mutmut_3(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_path_allowed__mutmut_3__mutmut_orig, x_x_is_path_allowed__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_is_path_allowed__mutmut_3__mutmut_orig(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_3__mutmut_1(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_3__mutmut_2(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_3__mutmut_3(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = ""
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_3__mutmut_4(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_3__mutmut_5(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_3__mutmut_6(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)

x_x_is_path_allowed__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_path_allowed__mutmut_3__mutmut_1': x_x_is_path_allowed__mutmut_3__mutmut_1, 
    'x_x_is_path_allowed__mutmut_3__mutmut_2': x_x_is_path_allowed__mutmut_3__mutmut_2, 
    'x_x_is_path_allowed__mutmut_3__mutmut_3': x_x_is_path_allowed__mutmut_3__mutmut_3, 
    'x_x_is_path_allowed__mutmut_3__mutmut_4': x_x_is_path_allowed__mutmut_3__mutmut_4, 
    'x_x_is_path_allowed__mutmut_3__mutmut_5': x_x_is_path_allowed__mutmut_3__mutmut_5, 
    'x_x_is_path_allowed__mutmut_3__mutmut_6': x_x_is_path_allowed__mutmut_3__mutmut_6
}
x_x_is_path_allowed__mutmut_3__mutmut_orig.__name__ = 'x_x_is_path_allowed__mutmut_3'


def x_is_path_allowed__mutmut_4(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_path_allowed__mutmut_4__mutmut_orig, x_x_is_path_allowed__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_is_path_allowed__mutmut_4__mutmut_orig(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_4__mutmut_1(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_4__mutmut_2(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_4__mutmut_3(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_4__mutmut_4(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(None)
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_4__mutmut_5(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_4__mutmut_6(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)

x_x_is_path_allowed__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_path_allowed__mutmut_4__mutmut_1': x_x_is_path_allowed__mutmut_4__mutmut_1, 
    'x_x_is_path_allowed__mutmut_4__mutmut_2': x_x_is_path_allowed__mutmut_4__mutmut_2, 
    'x_x_is_path_allowed__mutmut_4__mutmut_3': x_x_is_path_allowed__mutmut_4__mutmut_3, 
    'x_x_is_path_allowed__mutmut_4__mutmut_4': x_x_is_path_allowed__mutmut_4__mutmut_4, 
    'x_x_is_path_allowed__mutmut_4__mutmut_5': x_x_is_path_allowed__mutmut_4__mutmut_5, 
    'x_x_is_path_allowed__mutmut_4__mutmut_6': x_x_is_path_allowed__mutmut_4__mutmut_6
}
x_x_is_path_allowed__mutmut_4__mutmut_orig.__name__ = 'x_x_is_path_allowed__mutmut_4'


def x_is_path_allowed__mutmut_5(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_path_allowed__mutmut_5__mutmut_orig, x_x_is_path_allowed__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_is_path_allowed__mutmut_5__mutmut_orig(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_5__mutmut_1(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_5__mutmut_2(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_5__mutmut_3(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_5__mutmut_4(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(None)
    if check_path_traversal(None):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_5__mutmut_5(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_5__mutmut_6(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return False
    return resolved.startswith(None)

x_x_is_path_allowed__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_path_allowed__mutmut_5__mutmut_1': x_x_is_path_allowed__mutmut_5__mutmut_1, 
    'x_x_is_path_allowed__mutmut_5__mutmut_2': x_x_is_path_allowed__mutmut_5__mutmut_2, 
    'x_x_is_path_allowed__mutmut_5__mutmut_3': x_x_is_path_allowed__mutmut_5__mutmut_3, 
    'x_x_is_path_allowed__mutmut_5__mutmut_4': x_x_is_path_allowed__mutmut_5__mutmut_4, 
    'x_x_is_path_allowed__mutmut_5__mutmut_5': x_x_is_path_allowed__mutmut_5__mutmut_5, 
    'x_x_is_path_allowed__mutmut_5__mutmut_6': x_x_is_path_allowed__mutmut_5__mutmut_6
}
x_x_is_path_allowed__mutmut_5__mutmut_orig.__name__ = 'x_x_is_path_allowed__mutmut_5'


def x_is_path_allowed__mutmut_6(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_path_allowed__mutmut_6__mutmut_orig, x_x_is_path_allowed__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_is_path_allowed__mutmut_6__mutmut_orig(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_6__mutmut_1(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_6__mutmut_2(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_6__mutmut_3(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_6__mutmut_4(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_6__mutmut_5(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return True
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_6__mutmut_6(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(workspace)


def x_x_is_path_allowed__mutmut_6__mutmut_7(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return True
    return resolved.startswith(None)

x_x_is_path_allowed__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_path_allowed__mutmut_6__mutmut_1': x_x_is_path_allowed__mutmut_6__mutmut_1, 
    'x_x_is_path_allowed__mutmut_6__mutmut_2': x_x_is_path_allowed__mutmut_6__mutmut_2, 
    'x_x_is_path_allowed__mutmut_6__mutmut_3': x_x_is_path_allowed__mutmut_6__mutmut_3, 
    'x_x_is_path_allowed__mutmut_6__mutmut_4': x_x_is_path_allowed__mutmut_6__mutmut_4, 
    'x_x_is_path_allowed__mutmut_6__mutmut_5': x_x_is_path_allowed__mutmut_6__mutmut_5, 
    'x_x_is_path_allowed__mutmut_6__mutmut_6': x_x_is_path_allowed__mutmut_6__mutmut_6, 
    'x_x_is_path_allowed__mutmut_6__mutmut_7': x_x_is_path_allowed__mutmut_6__mutmut_7
}
x_x_is_path_allowed__mutmut_6__mutmut_orig.__name__ = 'x_x_is_path_allowed__mutmut_6'


def x_is_path_allowed__mutmut_7(path: str, workspace_root: str) -> str:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_path_allowed__mutmut_7__mutmut_orig, x_x_is_path_allowed__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_is_path_allowed__mutmut_7__mutmut_orig(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)


def x_x_is_path_allowed__mutmut_7__mutmut_1(path: str, workspace_root: str) -> str:
    resolved = None
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)


def x_x_is_path_allowed__mutmut_7__mutmut_2(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(None)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)


def x_x_is_path_allowed__mutmut_7__mutmut_3(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = None
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)


def x_x_is_path_allowed__mutmut_7__mutmut_4(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(None)
    if check_path_traversal(path):
        return False
    return resolved.startswith(None)


def x_x_is_path_allowed__mutmut_7__mutmut_5(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(None):
        return False
    return resolved.startswith(None)


def x_x_is_path_allowed__mutmut_7__mutmut_6(path: str, workspace_root: str) -> str:
    resolved = os.path.normpath(path)
    workspace = os.path.normpath(workspace_root)
    if check_path_traversal(path):
        return True
    return resolved.startswith(None)

x_x_is_path_allowed__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_path_allowed__mutmut_7__mutmut_1': x_x_is_path_allowed__mutmut_7__mutmut_1, 
    'x_x_is_path_allowed__mutmut_7__mutmut_2': x_x_is_path_allowed__mutmut_7__mutmut_2, 
    'x_x_is_path_allowed__mutmut_7__mutmut_3': x_x_is_path_allowed__mutmut_7__mutmut_3, 
    'x_x_is_path_allowed__mutmut_7__mutmut_4': x_x_is_path_allowed__mutmut_7__mutmut_4, 
    'x_x_is_path_allowed__mutmut_7__mutmut_5': x_x_is_path_allowed__mutmut_7__mutmut_5, 
    'x_x_is_path_allowed__mutmut_7__mutmut_6': x_x_is_path_allowed__mutmut_7__mutmut_6
}
x_x_is_path_allowed__mutmut_7__mutmut_orig.__name__ = 'x_x_is_path_allowed__mutmut_7'

x_is_path_allowed__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_is_path_allowed__mutmut_1': x_is_path_allowed__mutmut_1, 
    'x_is_path_allowed__mutmut_2': x_is_path_allowed__mutmut_2, 
    'x_is_path_allowed__mutmut_3': x_is_path_allowed__mutmut_3, 
    'x_is_path_allowed__mutmut_4': x_is_path_allowed__mutmut_4, 
    'x_is_path_allowed__mutmut_5': x_is_path_allowed__mutmut_5, 
    'x_is_path_allowed__mutmut_6': x_is_path_allowed__mutmut_6, 
    'x_is_path_allowed__mutmut_7': x_is_path_allowed__mutmut_7
}
x_is_path_allowed__mutmut_orig.__name__ = 'x_is_path_allowed'


def check_path_traversal(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, args, kwargs, None)


def x_check_path_traversal__mutmut_orig(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, args, kwargs, None)


def x_check_path_traversal__mutmut_1(path: str) -> bool:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, args, kwargs, None)


def x_check_path_traversal__mutmut_2(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, args, kwargs, None)


def x_check_path_traversal__mutmut_3(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_check_path_traversal__mutmut_mutants, args, kwargs, None)


def x_check_path_traversal__mutmut_4(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, None, args, kwargs, None)


def x_check_path_traversal__mutmut_5(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, None, kwargs, None)


def x_check_path_traversal__mutmut_6(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, args, None, None)


def x_check_path_traversal__mutmut_7(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_mutants, args, kwargs, None)


def x_check_path_traversal__mutmut_8(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, args, kwargs, None)


def x_check_path_traversal__mutmut_9(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, kwargs, None)


def x_check_path_traversal__mutmut_10(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, args, None)


def x_check_path_traversal__mutmut_11(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_path_traversal__mutmut_orig, x_check_path_traversal__mutmut_mutants, args, kwargs, )

x_check_path_traversal__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_path_traversal__mutmut_1': x_check_path_traversal__mutmut_1, 
    'x_check_path_traversal__mutmut_2': x_check_path_traversal__mutmut_2, 
    'x_check_path_traversal__mutmut_3': x_check_path_traversal__mutmut_3, 
    'x_check_path_traversal__mutmut_4': x_check_path_traversal__mutmut_4, 
    'x_check_path_traversal__mutmut_5': x_check_path_traversal__mutmut_5, 
    'x_check_path_traversal__mutmut_6': x_check_path_traversal__mutmut_6, 
    'x_check_path_traversal__mutmut_7': x_check_path_traversal__mutmut_7, 
    'x_check_path_traversal__mutmut_8': x_check_path_traversal__mutmut_8, 
    'x_check_path_traversal__mutmut_9': x_check_path_traversal__mutmut_9, 
    'x_check_path_traversal__mutmut_10': x_check_path_traversal__mutmut_10, 
    'x_check_path_traversal__mutmut_11': x_check_path_traversal__mutmut_11
}
x_check_path_traversal__mutmut_orig.__name__ = 'x_check_path_traversal'


def x_check_path_traversal__mutmut_orig(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_orig__mutmut_orig, x_x_check_path_traversal__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_orig__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_orig__mutmut_12(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_orig__mutmut_1': x_x_check_path_traversal__mutmut_orig__mutmut_1, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_2': x_x_check_path_traversal__mutmut_orig__mutmut_2, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_3': x_x_check_path_traversal__mutmut_orig__mutmut_3, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_4': x_x_check_path_traversal__mutmut_orig__mutmut_4, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_5': x_x_check_path_traversal__mutmut_orig__mutmut_5, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_6': x_x_check_path_traversal__mutmut_orig__mutmut_6, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_7': x_x_check_path_traversal__mutmut_orig__mutmut_7, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_8': x_x_check_path_traversal__mutmut_orig__mutmut_8, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_9': x_x_check_path_traversal__mutmut_orig__mutmut_9, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_10': x_x_check_path_traversal__mutmut_orig__mutmut_10, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_11': x_x_check_path_traversal__mutmut_orig__mutmut_11, 
    'x_x_check_path_traversal__mutmut_orig__mutmut_12': x_x_check_path_traversal__mutmut_orig__mutmut_12
}
x_x_check_path_traversal__mutmut_orig__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_orig'


def x_check_path_traversal__mutmut_1(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_1__mutmut_orig, x_x_check_path_traversal__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_1__mutmut_orig(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_1(path: str) -> bool:
    normalized = ""
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_2(path: str) -> bool:
    normalized = None
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_3(path: str) -> bool:
    normalized = None
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_4(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_5(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_6(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_7(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_8(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_9(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_10(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_1__mutmut_11(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_1__mutmut_1': x_x_check_path_traversal__mutmut_1__mutmut_1, 
    'x_x_check_path_traversal__mutmut_1__mutmut_2': x_x_check_path_traversal__mutmut_1__mutmut_2, 
    'x_x_check_path_traversal__mutmut_1__mutmut_3': x_x_check_path_traversal__mutmut_1__mutmut_3, 
    'x_x_check_path_traversal__mutmut_1__mutmut_4': x_x_check_path_traversal__mutmut_1__mutmut_4, 
    'x_x_check_path_traversal__mutmut_1__mutmut_5': x_x_check_path_traversal__mutmut_1__mutmut_5, 
    'x_x_check_path_traversal__mutmut_1__mutmut_6': x_x_check_path_traversal__mutmut_1__mutmut_6, 
    'x_x_check_path_traversal__mutmut_1__mutmut_7': x_x_check_path_traversal__mutmut_1__mutmut_7, 
    'x_x_check_path_traversal__mutmut_1__mutmut_8': x_x_check_path_traversal__mutmut_1__mutmut_8, 
    'x_x_check_path_traversal__mutmut_1__mutmut_9': x_x_check_path_traversal__mutmut_1__mutmut_9, 
    'x_x_check_path_traversal__mutmut_1__mutmut_10': x_x_check_path_traversal__mutmut_1__mutmut_10, 
    'x_x_check_path_traversal__mutmut_1__mutmut_11': x_x_check_path_traversal__mutmut_1__mutmut_11
}
x_x_check_path_traversal__mutmut_1__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_1'


def x_check_path_traversal__mutmut_2(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_2__mutmut_orig, x_x_check_path_traversal__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_2__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_2__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_2__mutmut_1': x_x_check_path_traversal__mutmut_2__mutmut_1, 
    'x_x_check_path_traversal__mutmut_2__mutmut_2': x_x_check_path_traversal__mutmut_2__mutmut_2, 
    'x_x_check_path_traversal__mutmut_2__mutmut_3': x_x_check_path_traversal__mutmut_2__mutmut_3, 
    'x_x_check_path_traversal__mutmut_2__mutmut_4': x_x_check_path_traversal__mutmut_2__mutmut_4, 
    'x_x_check_path_traversal__mutmut_2__mutmut_5': x_x_check_path_traversal__mutmut_2__mutmut_5, 
    'x_x_check_path_traversal__mutmut_2__mutmut_6': x_x_check_path_traversal__mutmut_2__mutmut_6, 
    'x_x_check_path_traversal__mutmut_2__mutmut_7': x_x_check_path_traversal__mutmut_2__mutmut_7, 
    'x_x_check_path_traversal__mutmut_2__mutmut_8': x_x_check_path_traversal__mutmut_2__mutmut_8, 
    'x_x_check_path_traversal__mutmut_2__mutmut_9': x_x_check_path_traversal__mutmut_2__mutmut_9, 
    'x_x_check_path_traversal__mutmut_2__mutmut_10': x_x_check_path_traversal__mutmut_2__mutmut_10, 
    'x_x_check_path_traversal__mutmut_2__mutmut_11': x_x_check_path_traversal__mutmut_2__mutmut_11
}
x_x_check_path_traversal__mutmut_2__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_2'


def x_check_path_traversal__mutmut_3(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_3__mutmut_orig, x_x_check_path_traversal__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_3__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_1(path: str) -> bool:
    normalized = None
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = ""
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_3__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_3__mutmut_1': x_x_check_path_traversal__mutmut_3__mutmut_1, 
    'x_x_check_path_traversal__mutmut_3__mutmut_2': x_x_check_path_traversal__mutmut_3__mutmut_2, 
    'x_x_check_path_traversal__mutmut_3__mutmut_3': x_x_check_path_traversal__mutmut_3__mutmut_3, 
    'x_x_check_path_traversal__mutmut_3__mutmut_4': x_x_check_path_traversal__mutmut_3__mutmut_4, 
    'x_x_check_path_traversal__mutmut_3__mutmut_5': x_x_check_path_traversal__mutmut_3__mutmut_5, 
    'x_x_check_path_traversal__mutmut_3__mutmut_6': x_x_check_path_traversal__mutmut_3__mutmut_6, 
    'x_x_check_path_traversal__mutmut_3__mutmut_7': x_x_check_path_traversal__mutmut_3__mutmut_7, 
    'x_x_check_path_traversal__mutmut_3__mutmut_8': x_x_check_path_traversal__mutmut_3__mutmut_8, 
    'x_x_check_path_traversal__mutmut_3__mutmut_9': x_x_check_path_traversal__mutmut_3__mutmut_9, 
    'x_x_check_path_traversal__mutmut_3__mutmut_10': x_x_check_path_traversal__mutmut_3__mutmut_10, 
    'x_x_check_path_traversal__mutmut_3__mutmut_11': x_x_check_path_traversal__mutmut_3__mutmut_11
}
x_x_check_path_traversal__mutmut_3__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_3'


def x_check_path_traversal__mutmut_4(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_4__mutmut_orig, x_x_check_path_traversal__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_4__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_4__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_4__mutmut_1': x_x_check_path_traversal__mutmut_4__mutmut_1, 
    'x_x_check_path_traversal__mutmut_4__mutmut_2': x_x_check_path_traversal__mutmut_4__mutmut_2, 
    'x_x_check_path_traversal__mutmut_4__mutmut_3': x_x_check_path_traversal__mutmut_4__mutmut_3, 
    'x_x_check_path_traversal__mutmut_4__mutmut_4': x_x_check_path_traversal__mutmut_4__mutmut_4, 
    'x_x_check_path_traversal__mutmut_4__mutmut_5': x_x_check_path_traversal__mutmut_4__mutmut_5, 
    'x_x_check_path_traversal__mutmut_4__mutmut_6': x_x_check_path_traversal__mutmut_4__mutmut_6, 
    'x_x_check_path_traversal__mutmut_4__mutmut_7': x_x_check_path_traversal__mutmut_4__mutmut_7, 
    'x_x_check_path_traversal__mutmut_4__mutmut_8': x_x_check_path_traversal__mutmut_4__mutmut_8, 
    'x_x_check_path_traversal__mutmut_4__mutmut_9': x_x_check_path_traversal__mutmut_4__mutmut_9, 
    'x_x_check_path_traversal__mutmut_4__mutmut_10': x_x_check_path_traversal__mutmut_4__mutmut_10, 
    'x_x_check_path_traversal__mutmut_4__mutmut_11': x_x_check_path_traversal__mutmut_4__mutmut_11
}
x_x_check_path_traversal__mutmut_4__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_4'


def x_check_path_traversal__mutmut_5(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_5__mutmut_orig, x_x_check_path_traversal__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_5__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_5__mutmut_12(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_5__mutmut_1': x_x_check_path_traversal__mutmut_5__mutmut_1, 
    'x_x_check_path_traversal__mutmut_5__mutmut_2': x_x_check_path_traversal__mutmut_5__mutmut_2, 
    'x_x_check_path_traversal__mutmut_5__mutmut_3': x_x_check_path_traversal__mutmut_5__mutmut_3, 
    'x_x_check_path_traversal__mutmut_5__mutmut_4': x_x_check_path_traversal__mutmut_5__mutmut_4, 
    'x_x_check_path_traversal__mutmut_5__mutmut_5': x_x_check_path_traversal__mutmut_5__mutmut_5, 
    'x_x_check_path_traversal__mutmut_5__mutmut_6': x_x_check_path_traversal__mutmut_5__mutmut_6, 
    'x_x_check_path_traversal__mutmut_5__mutmut_7': x_x_check_path_traversal__mutmut_5__mutmut_7, 
    'x_x_check_path_traversal__mutmut_5__mutmut_8': x_x_check_path_traversal__mutmut_5__mutmut_8, 
    'x_x_check_path_traversal__mutmut_5__mutmut_9': x_x_check_path_traversal__mutmut_5__mutmut_9, 
    'x_x_check_path_traversal__mutmut_5__mutmut_10': x_x_check_path_traversal__mutmut_5__mutmut_10, 
    'x_x_check_path_traversal__mutmut_5__mutmut_11': x_x_check_path_traversal__mutmut_5__mutmut_11, 
    'x_x_check_path_traversal__mutmut_5__mutmut_12': x_x_check_path_traversal__mutmut_5__mutmut_12
}
x_x_check_path_traversal__mutmut_5__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_5'


def x_check_path_traversal__mutmut_6(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_6__mutmut_orig, x_x_check_path_traversal__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_6__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XXXX..XXXX" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "xx..xx" in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_12(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_6__mutmut_13(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_6__mutmut_1': x_x_check_path_traversal__mutmut_6__mutmut_1, 
    'x_x_check_path_traversal__mutmut_6__mutmut_2': x_x_check_path_traversal__mutmut_6__mutmut_2, 
    'x_x_check_path_traversal__mutmut_6__mutmut_3': x_x_check_path_traversal__mutmut_6__mutmut_3, 
    'x_x_check_path_traversal__mutmut_6__mutmut_4': x_x_check_path_traversal__mutmut_6__mutmut_4, 
    'x_x_check_path_traversal__mutmut_6__mutmut_5': x_x_check_path_traversal__mutmut_6__mutmut_5, 
    'x_x_check_path_traversal__mutmut_6__mutmut_6': x_x_check_path_traversal__mutmut_6__mutmut_6, 
    'x_x_check_path_traversal__mutmut_6__mutmut_7': x_x_check_path_traversal__mutmut_6__mutmut_7, 
    'x_x_check_path_traversal__mutmut_6__mutmut_8': x_x_check_path_traversal__mutmut_6__mutmut_8, 
    'x_x_check_path_traversal__mutmut_6__mutmut_9': x_x_check_path_traversal__mutmut_6__mutmut_9, 
    'x_x_check_path_traversal__mutmut_6__mutmut_10': x_x_check_path_traversal__mutmut_6__mutmut_10, 
    'x_x_check_path_traversal__mutmut_6__mutmut_11': x_x_check_path_traversal__mutmut_6__mutmut_11, 
    'x_x_check_path_traversal__mutmut_6__mutmut_12': x_x_check_path_traversal__mutmut_6__mutmut_12, 
    'x_x_check_path_traversal__mutmut_6__mutmut_13': x_x_check_path_traversal__mutmut_6__mutmut_13
}
x_x_check_path_traversal__mutmut_6__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_6'


def x_check_path_traversal__mutmut_7(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_7__mutmut_orig, x_x_check_path_traversal__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_7__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts and (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" not in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_7__mutmut_12(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_7__mutmut_1': x_x_check_path_traversal__mutmut_7__mutmut_1, 
    'x_x_check_path_traversal__mutmut_7__mutmut_2': x_x_check_path_traversal__mutmut_7__mutmut_2, 
    'x_x_check_path_traversal__mutmut_7__mutmut_3': x_x_check_path_traversal__mutmut_7__mutmut_3, 
    'x_x_check_path_traversal__mutmut_7__mutmut_4': x_x_check_path_traversal__mutmut_7__mutmut_4, 
    'x_x_check_path_traversal__mutmut_7__mutmut_5': x_x_check_path_traversal__mutmut_7__mutmut_5, 
    'x_x_check_path_traversal__mutmut_7__mutmut_6': x_x_check_path_traversal__mutmut_7__mutmut_6, 
    'x_x_check_path_traversal__mutmut_7__mutmut_7': x_x_check_path_traversal__mutmut_7__mutmut_7, 
    'x_x_check_path_traversal__mutmut_7__mutmut_8': x_x_check_path_traversal__mutmut_7__mutmut_8, 
    'x_x_check_path_traversal__mutmut_7__mutmut_9': x_x_check_path_traversal__mutmut_7__mutmut_9, 
    'x_x_check_path_traversal__mutmut_7__mutmut_10': x_x_check_path_traversal__mutmut_7__mutmut_10, 
    'x_x_check_path_traversal__mutmut_7__mutmut_11': x_x_check_path_traversal__mutmut_7__mutmut_11, 
    'x_x_check_path_traversal__mutmut_7__mutmut_12': x_x_check_path_traversal__mutmut_7__mutmut_12
}
x_x_check_path_traversal__mutmut_7__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_7'


def x_check_path_traversal__mutmut_8(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_8__mutmut_orig, x_x_check_path_traversal__mutmut_8__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_8__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_8__mutmut_12(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_8__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_8__mutmut_1': x_x_check_path_traversal__mutmut_8__mutmut_1, 
    'x_x_check_path_traversal__mutmut_8__mutmut_2': x_x_check_path_traversal__mutmut_8__mutmut_2, 
    'x_x_check_path_traversal__mutmut_8__mutmut_3': x_x_check_path_traversal__mutmut_8__mutmut_3, 
    'x_x_check_path_traversal__mutmut_8__mutmut_4': x_x_check_path_traversal__mutmut_8__mutmut_4, 
    'x_x_check_path_traversal__mutmut_8__mutmut_5': x_x_check_path_traversal__mutmut_8__mutmut_5, 
    'x_x_check_path_traversal__mutmut_8__mutmut_6': x_x_check_path_traversal__mutmut_8__mutmut_6, 
    'x_x_check_path_traversal__mutmut_8__mutmut_7': x_x_check_path_traversal__mutmut_8__mutmut_7, 
    'x_x_check_path_traversal__mutmut_8__mutmut_8': x_x_check_path_traversal__mutmut_8__mutmut_8, 
    'x_x_check_path_traversal__mutmut_8__mutmut_9': x_x_check_path_traversal__mutmut_8__mutmut_9, 
    'x_x_check_path_traversal__mutmut_8__mutmut_10': x_x_check_path_traversal__mutmut_8__mutmut_10, 
    'x_x_check_path_traversal__mutmut_8__mutmut_11': x_x_check_path_traversal__mutmut_8__mutmut_11, 
    'x_x_check_path_traversal__mutmut_8__mutmut_12': x_x_check_path_traversal__mutmut_8__mutmut_12
}
x_x_check_path_traversal__mutmut_8__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_8'


def x_check_path_traversal__mutmut_9(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_9__mutmut_orig, x_x_check_path_traversal__mutmut_9__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_9__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized == path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path or ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_9__mutmut_12(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." in normalized.split(None))

x_x_check_path_traversal__mutmut_9__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_9__mutmut_1': x_x_check_path_traversal__mutmut_9__mutmut_1, 
    'x_x_check_path_traversal__mutmut_9__mutmut_2': x_x_check_path_traversal__mutmut_9__mutmut_2, 
    'x_x_check_path_traversal__mutmut_9__mutmut_3': x_x_check_path_traversal__mutmut_9__mutmut_3, 
    'x_x_check_path_traversal__mutmut_9__mutmut_4': x_x_check_path_traversal__mutmut_9__mutmut_4, 
    'x_x_check_path_traversal__mutmut_9__mutmut_5': x_x_check_path_traversal__mutmut_9__mutmut_5, 
    'x_x_check_path_traversal__mutmut_9__mutmut_6': x_x_check_path_traversal__mutmut_9__mutmut_6, 
    'x_x_check_path_traversal__mutmut_9__mutmut_7': x_x_check_path_traversal__mutmut_9__mutmut_7, 
    'x_x_check_path_traversal__mutmut_9__mutmut_8': x_x_check_path_traversal__mutmut_9__mutmut_8, 
    'x_x_check_path_traversal__mutmut_9__mutmut_9': x_x_check_path_traversal__mutmut_9__mutmut_9, 
    'x_x_check_path_traversal__mutmut_9__mutmut_10': x_x_check_path_traversal__mutmut_9__mutmut_10, 
    'x_x_check_path_traversal__mutmut_9__mutmut_11': x_x_check_path_traversal__mutmut_9__mutmut_11, 
    'x_x_check_path_traversal__mutmut_9__mutmut_12': x_x_check_path_traversal__mutmut_9__mutmut_12
}
x_x_check_path_traversal__mutmut_9__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_9'


def x_check_path_traversal__mutmut_10(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_10__mutmut_orig, x_x_check_path_traversal__mutmut_10__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_10__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and "XX..XX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XXXX..XXXX" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "xx..xx" in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_12(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_10__mutmut_13(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(None))

x_x_check_path_traversal__mutmut_10__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_10__mutmut_1': x_x_check_path_traversal__mutmut_10__mutmut_1, 
    'x_x_check_path_traversal__mutmut_10__mutmut_2': x_x_check_path_traversal__mutmut_10__mutmut_2, 
    'x_x_check_path_traversal__mutmut_10__mutmut_3': x_x_check_path_traversal__mutmut_10__mutmut_3, 
    'x_x_check_path_traversal__mutmut_10__mutmut_4': x_x_check_path_traversal__mutmut_10__mutmut_4, 
    'x_x_check_path_traversal__mutmut_10__mutmut_5': x_x_check_path_traversal__mutmut_10__mutmut_5, 
    'x_x_check_path_traversal__mutmut_10__mutmut_6': x_x_check_path_traversal__mutmut_10__mutmut_6, 
    'x_x_check_path_traversal__mutmut_10__mutmut_7': x_x_check_path_traversal__mutmut_10__mutmut_7, 
    'x_x_check_path_traversal__mutmut_10__mutmut_8': x_x_check_path_traversal__mutmut_10__mutmut_8, 
    'x_x_check_path_traversal__mutmut_10__mutmut_9': x_x_check_path_traversal__mutmut_10__mutmut_9, 
    'x_x_check_path_traversal__mutmut_10__mutmut_10': x_x_check_path_traversal__mutmut_10__mutmut_10, 
    'x_x_check_path_traversal__mutmut_10__mutmut_11': x_x_check_path_traversal__mutmut_10__mutmut_11, 
    'x_x_check_path_traversal__mutmut_10__mutmut_12': x_x_check_path_traversal__mutmut_10__mutmut_12, 
    'x_x_check_path_traversal__mutmut_10__mutmut_13': x_x_check_path_traversal__mutmut_10__mutmut_13
}
x_x_check_path_traversal__mutmut_10__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_10'


def x_check_path_traversal__mutmut_11(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_11__mutmut_orig, x_x_check_path_traversal__mutmut_11__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_11__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" not in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(os.sep))


def x_x_check_path_traversal__mutmut_11__mutmut_12(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." not in normalized.split(None))

x_x_check_path_traversal__mutmut_11__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_11__mutmut_1': x_x_check_path_traversal__mutmut_11__mutmut_1, 
    'x_x_check_path_traversal__mutmut_11__mutmut_2': x_x_check_path_traversal__mutmut_11__mutmut_2, 
    'x_x_check_path_traversal__mutmut_11__mutmut_3': x_x_check_path_traversal__mutmut_11__mutmut_3, 
    'x_x_check_path_traversal__mutmut_11__mutmut_4': x_x_check_path_traversal__mutmut_11__mutmut_4, 
    'x_x_check_path_traversal__mutmut_11__mutmut_5': x_x_check_path_traversal__mutmut_11__mutmut_5, 
    'x_x_check_path_traversal__mutmut_11__mutmut_6': x_x_check_path_traversal__mutmut_11__mutmut_6, 
    'x_x_check_path_traversal__mutmut_11__mutmut_7': x_x_check_path_traversal__mutmut_11__mutmut_7, 
    'x_x_check_path_traversal__mutmut_11__mutmut_8': x_x_check_path_traversal__mutmut_11__mutmut_8, 
    'x_x_check_path_traversal__mutmut_11__mutmut_9': x_x_check_path_traversal__mutmut_11__mutmut_9, 
    'x_x_check_path_traversal__mutmut_11__mutmut_10': x_x_check_path_traversal__mutmut_11__mutmut_10, 
    'x_x_check_path_traversal__mutmut_11__mutmut_11': x_x_check_path_traversal__mutmut_11__mutmut_11, 
    'x_x_check_path_traversal__mutmut_11__mutmut_12': x_x_check_path_traversal__mutmut_11__mutmut_12
}
x_x_check_path_traversal__mutmut_11__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_11'


def x_check_path_traversal__mutmut_12(path: str) -> bool:
    args = [path]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_check_path_traversal__mutmut_12__mutmut_orig, x_x_check_path_traversal__mutmut_12__mutmut_mutants, args, kwargs, None)


def x_x_check_path_traversal__mutmut_12__mutmut_orig(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_1(path: str) -> bool:
    normalized = None
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_2(path: str) -> bool:
    normalized = os.path.normpath(None)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_3(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = None
    return ".." in parts or (normalized != path and ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_4(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(None)
    return ".." in parts or (normalized != path and ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_5(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts and (normalized != path and ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_6(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return "XX..XX" in parts or (normalized != path and ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_7(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." not in parts or (normalized != path and ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_8(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path or ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_9(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized == path and ".." in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_10(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and "XX..XX" in normalized.split(None))


def x_x_check_path_traversal__mutmut_12__mutmut_11(path: str) -> bool:
    normalized = os.path.normpath(path)
    parts = path.split(os.sep)
    return ".." in parts or (normalized != path and ".." not in normalized.split(None))

x_x_check_path_traversal__mutmut_12__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_check_path_traversal__mutmut_12__mutmut_1': x_x_check_path_traversal__mutmut_12__mutmut_1, 
    'x_x_check_path_traversal__mutmut_12__mutmut_2': x_x_check_path_traversal__mutmut_12__mutmut_2, 
    'x_x_check_path_traversal__mutmut_12__mutmut_3': x_x_check_path_traversal__mutmut_12__mutmut_3, 
    'x_x_check_path_traversal__mutmut_12__mutmut_4': x_x_check_path_traversal__mutmut_12__mutmut_4, 
    'x_x_check_path_traversal__mutmut_12__mutmut_5': x_x_check_path_traversal__mutmut_12__mutmut_5, 
    'x_x_check_path_traversal__mutmut_12__mutmut_6': x_x_check_path_traversal__mutmut_12__mutmut_6, 
    'x_x_check_path_traversal__mutmut_12__mutmut_7': x_x_check_path_traversal__mutmut_12__mutmut_7, 
    'x_x_check_path_traversal__mutmut_12__mutmut_8': x_x_check_path_traversal__mutmut_12__mutmut_8, 
    'x_x_check_path_traversal__mutmut_12__mutmut_9': x_x_check_path_traversal__mutmut_12__mutmut_9, 
    'x_x_check_path_traversal__mutmut_12__mutmut_10': x_x_check_path_traversal__mutmut_12__mutmut_10, 
    'x_x_check_path_traversal__mutmut_12__mutmut_11': x_x_check_path_traversal__mutmut_12__mutmut_11
}
x_x_check_path_traversal__mutmut_12__mutmut_orig.__name__ = 'x_x_check_path_traversal__mutmut_12'

x_check_path_traversal__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_path_traversal__mutmut_1': x_check_path_traversal__mutmut_1, 
    'x_check_path_traversal__mutmut_2': x_check_path_traversal__mutmut_2, 
    'x_check_path_traversal__mutmut_3': x_check_path_traversal__mutmut_3, 
    'x_check_path_traversal__mutmut_4': x_check_path_traversal__mutmut_4, 
    'x_check_path_traversal__mutmut_5': x_check_path_traversal__mutmut_5, 
    'x_check_path_traversal__mutmut_6': x_check_path_traversal__mutmut_6, 
    'x_check_path_traversal__mutmut_7': x_check_path_traversal__mutmut_7, 
    'x_check_path_traversal__mutmut_8': x_check_path_traversal__mutmut_8, 
    'x_check_path_traversal__mutmut_9': x_check_path_traversal__mutmut_9, 
    'x_check_path_traversal__mutmut_10': x_check_path_traversal__mutmut_10, 
    'x_check_path_traversal__mutmut_11': x_check_path_traversal__mutmut_11, 
    'x_check_path_traversal__mutmut_12': x_check_path_traversal__mutmut_12
}
x_check_path_traversal__mutmut_orig.__name__ = 'x_check_path_traversal'


def is_symlink_escape(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, args, kwargs, None)


def x_is_symlink_escape__mutmut_orig(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, args, kwargs, None)


def x_is_symlink_escape__mutmut_1(path: str, workspace_root: str) -> bool:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, args, kwargs, None)


def x_is_symlink_escape__mutmut_2(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, args, kwargs, None)


def x_is_symlink_escape__mutmut_3(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_is_symlink_escape__mutmut_mutants, args, kwargs, None)


def x_is_symlink_escape__mutmut_4(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, None, args, kwargs, None)


def x_is_symlink_escape__mutmut_5(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, None, kwargs, None)


def x_is_symlink_escape__mutmut_6(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, args, None, None)


def x_is_symlink_escape__mutmut_7(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_mutants, args, kwargs, None)


def x_is_symlink_escape__mutmut_8(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, args, kwargs, None)


def x_is_symlink_escape__mutmut_9(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, kwargs, None)


def x_is_symlink_escape__mutmut_10(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, args, None)


def x_is_symlink_escape__mutmut_11(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_symlink_escape__mutmut_orig, x_is_symlink_escape__mutmut_mutants, args, kwargs, )

x_is_symlink_escape__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_is_symlink_escape__mutmut_1': x_is_symlink_escape__mutmut_1, 
    'x_is_symlink_escape__mutmut_2': x_is_symlink_escape__mutmut_2, 
    'x_is_symlink_escape__mutmut_3': x_is_symlink_escape__mutmut_3, 
    'x_is_symlink_escape__mutmut_4': x_is_symlink_escape__mutmut_4, 
    'x_is_symlink_escape__mutmut_5': x_is_symlink_escape__mutmut_5, 
    'x_is_symlink_escape__mutmut_6': x_is_symlink_escape__mutmut_6, 
    'x_is_symlink_escape__mutmut_7': x_is_symlink_escape__mutmut_7, 
    'x_is_symlink_escape__mutmut_8': x_is_symlink_escape__mutmut_8, 
    'x_is_symlink_escape__mutmut_9': x_is_symlink_escape__mutmut_9, 
    'x_is_symlink_escape__mutmut_10': x_is_symlink_escape__mutmut_10, 
    'x_is_symlink_escape__mutmut_11': x_is_symlink_escape__mutmut_11
}
x_is_symlink_escape__mutmut_orig.__name__ = 'x_is_symlink_escape'


def x_is_symlink_escape__mutmut_orig(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_symlink_escape__mutmut_orig__mutmut_orig, x_x_is_symlink_escape__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_is_symlink_escape__mutmut_orig__mutmut_orig(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_orig__mutmut_1(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_orig__mutmut_2(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_orig__mutmut_3(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = None
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_orig__mutmut_4(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(None)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_orig__mutmut_5(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_orig__mutmut_6(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(None)

x_x_is_symlink_escape__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_symlink_escape__mutmut_orig__mutmut_1': x_x_is_symlink_escape__mutmut_orig__mutmut_1, 
    'x_x_is_symlink_escape__mutmut_orig__mutmut_2': x_x_is_symlink_escape__mutmut_orig__mutmut_2, 
    'x_x_is_symlink_escape__mutmut_orig__mutmut_3': x_x_is_symlink_escape__mutmut_orig__mutmut_3, 
    'x_x_is_symlink_escape__mutmut_orig__mutmut_4': x_x_is_symlink_escape__mutmut_orig__mutmut_4, 
    'x_x_is_symlink_escape__mutmut_orig__mutmut_5': x_x_is_symlink_escape__mutmut_orig__mutmut_5, 
    'x_x_is_symlink_escape__mutmut_orig__mutmut_6': x_x_is_symlink_escape__mutmut_orig__mutmut_6
}
x_x_is_symlink_escape__mutmut_orig__mutmut_orig.__name__ = 'x_x_is_symlink_escape__mutmut_orig'


def x_is_symlink_escape__mutmut_1(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_symlink_escape__mutmut_1__mutmut_orig, x_x_is_symlink_escape__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_is_symlink_escape__mutmut_1__mutmut_orig(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_1__mutmut_1(path: str, workspace_root: str) -> bool:
    resolved = ""
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_1__mutmut_2(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = None
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_1__mutmut_3(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(None)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_1__mutmut_4(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(workspace_root)
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_1__mutmut_5(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(None)

x_x_is_symlink_escape__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_symlink_escape__mutmut_1__mutmut_1': x_x_is_symlink_escape__mutmut_1__mutmut_1, 
    'x_x_is_symlink_escape__mutmut_1__mutmut_2': x_x_is_symlink_escape__mutmut_1__mutmut_2, 
    'x_x_is_symlink_escape__mutmut_1__mutmut_3': x_x_is_symlink_escape__mutmut_1__mutmut_3, 
    'x_x_is_symlink_escape__mutmut_1__mutmut_4': x_x_is_symlink_escape__mutmut_1__mutmut_4, 
    'x_x_is_symlink_escape__mutmut_1__mutmut_5': x_x_is_symlink_escape__mutmut_1__mutmut_5
}
x_x_is_symlink_escape__mutmut_1__mutmut_orig.__name__ = 'x_x_is_symlink_escape__mutmut_1'


def x_is_symlink_escape__mutmut_2(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_symlink_escape__mutmut_2__mutmut_orig, x_x_is_symlink_escape__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_is_symlink_escape__mutmut_2__mutmut_orig(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_2__mutmut_1(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_2__mutmut_2(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = None
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_2__mutmut_3(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = os.path.realpath(None)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_2__mutmut_4(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = os.path.realpath(workspace_root)
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_2__mutmut_5(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(None)

x_x_is_symlink_escape__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_symlink_escape__mutmut_2__mutmut_1': x_x_is_symlink_escape__mutmut_2__mutmut_1, 
    'x_x_is_symlink_escape__mutmut_2__mutmut_2': x_x_is_symlink_escape__mutmut_2__mutmut_2, 
    'x_x_is_symlink_escape__mutmut_2__mutmut_3': x_x_is_symlink_escape__mutmut_2__mutmut_3, 
    'x_x_is_symlink_escape__mutmut_2__mutmut_4': x_x_is_symlink_escape__mutmut_2__mutmut_4, 
    'x_x_is_symlink_escape__mutmut_2__mutmut_5': x_x_is_symlink_escape__mutmut_2__mutmut_5
}
x_x_is_symlink_escape__mutmut_2__mutmut_orig.__name__ = 'x_x_is_symlink_escape__mutmut_2'


def x_is_symlink_escape__mutmut_3(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_symlink_escape__mutmut_3__mutmut_orig, x_x_is_symlink_escape__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_is_symlink_escape__mutmut_3__mutmut_orig(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = None
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_3__mutmut_1(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = None
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_3__mutmut_2(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = None
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_3__mutmut_3(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = ""
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_3__mutmut_4(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = None
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_3__mutmut_5(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = None
    return not resolved.startswith(None)

x_x_is_symlink_escape__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_symlink_escape__mutmut_3__mutmut_1': x_x_is_symlink_escape__mutmut_3__mutmut_1, 
    'x_x_is_symlink_escape__mutmut_3__mutmut_2': x_x_is_symlink_escape__mutmut_3__mutmut_2, 
    'x_x_is_symlink_escape__mutmut_3__mutmut_3': x_x_is_symlink_escape__mutmut_3__mutmut_3, 
    'x_x_is_symlink_escape__mutmut_3__mutmut_4': x_x_is_symlink_escape__mutmut_3__mutmut_4, 
    'x_x_is_symlink_escape__mutmut_3__mutmut_5': x_x_is_symlink_escape__mutmut_3__mutmut_5
}
x_x_is_symlink_escape__mutmut_3__mutmut_orig.__name__ = 'x_x_is_symlink_escape__mutmut_3'


def x_is_symlink_escape__mutmut_4(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_symlink_escape__mutmut_4__mutmut_orig, x_x_is_symlink_escape__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_is_symlink_escape__mutmut_4__mutmut_orig(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(None)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_4__mutmut_1(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(None)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_4__mutmut_2(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = os.path.realpath(None)
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_4__mutmut_3(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = None
    return not resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_4__mutmut_4(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(None)
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_4__mutmut_5(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(None)
    return not resolved.startswith(None)

x_x_is_symlink_escape__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_symlink_escape__mutmut_4__mutmut_1': x_x_is_symlink_escape__mutmut_4__mutmut_1, 
    'x_x_is_symlink_escape__mutmut_4__mutmut_2': x_x_is_symlink_escape__mutmut_4__mutmut_2, 
    'x_x_is_symlink_escape__mutmut_4__mutmut_3': x_x_is_symlink_escape__mutmut_4__mutmut_3, 
    'x_x_is_symlink_escape__mutmut_4__mutmut_4': x_x_is_symlink_escape__mutmut_4__mutmut_4, 
    'x_x_is_symlink_escape__mutmut_4__mutmut_5': x_x_is_symlink_escape__mutmut_4__mutmut_5
}
x_x_is_symlink_escape__mutmut_4__mutmut_orig.__name__ = 'x_x_is_symlink_escape__mutmut_4'


def x_is_symlink_escape__mutmut_5(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_symlink_escape__mutmut_5__mutmut_orig, x_x_is_symlink_escape__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_is_symlink_escape__mutmut_5__mutmut_orig(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_5__mutmut_1(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(workspace_root)
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_5__mutmut_2(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = os.path.realpath(workspace_root)
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_5__mutmut_3(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = None
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_5__mutmut_4(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(None)
    return resolved.startswith(workspace)


def x_x_is_symlink_escape__mutmut_5__mutmut_5(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return resolved.startswith(None)

x_x_is_symlink_escape__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_symlink_escape__mutmut_5__mutmut_1': x_x_is_symlink_escape__mutmut_5__mutmut_1, 
    'x_x_is_symlink_escape__mutmut_5__mutmut_2': x_x_is_symlink_escape__mutmut_5__mutmut_2, 
    'x_x_is_symlink_escape__mutmut_5__mutmut_3': x_x_is_symlink_escape__mutmut_5__mutmut_3, 
    'x_x_is_symlink_escape__mutmut_5__mutmut_4': x_x_is_symlink_escape__mutmut_5__mutmut_4, 
    'x_x_is_symlink_escape__mutmut_5__mutmut_5': x_x_is_symlink_escape__mutmut_5__mutmut_5
}
x_x_is_symlink_escape__mutmut_5__mutmut_orig.__name__ = 'x_x_is_symlink_escape__mutmut_5'


def x_is_symlink_escape__mutmut_6(path: str, workspace_root: str) -> bool:
    args = [path, workspace_root]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_is_symlink_escape__mutmut_6__mutmut_orig, x_x_is_symlink_escape__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_is_symlink_escape__mutmut_6__mutmut_orig(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(None)


def x_x_is_symlink_escape__mutmut_6__mutmut_1(path: str, workspace_root: str) -> bool:
    resolved = None
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(None)


def x_x_is_symlink_escape__mutmut_6__mutmut_2(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(None)
    workspace = os.path.realpath(workspace_root)
    return not resolved.startswith(None)


def x_x_is_symlink_escape__mutmut_6__mutmut_3(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = None
    return not resolved.startswith(None)


def x_x_is_symlink_escape__mutmut_6__mutmut_4(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(None)
    return not resolved.startswith(None)


def x_x_is_symlink_escape__mutmut_6__mutmut_5(path: str, workspace_root: str) -> bool:
    resolved = os.path.realpath(path)
    workspace = os.path.realpath(workspace_root)
    return resolved.startswith(None)

x_x_is_symlink_escape__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_is_symlink_escape__mutmut_6__mutmut_1': x_x_is_symlink_escape__mutmut_6__mutmut_1, 
    'x_x_is_symlink_escape__mutmut_6__mutmut_2': x_x_is_symlink_escape__mutmut_6__mutmut_2, 
    'x_x_is_symlink_escape__mutmut_6__mutmut_3': x_x_is_symlink_escape__mutmut_6__mutmut_3, 
    'x_x_is_symlink_escape__mutmut_6__mutmut_4': x_x_is_symlink_escape__mutmut_6__mutmut_4, 
    'x_x_is_symlink_escape__mutmut_6__mutmut_5': x_x_is_symlink_escape__mutmut_6__mutmut_5
}
x_x_is_symlink_escape__mutmut_6__mutmut_orig.__name__ = 'x_x_is_symlink_escape__mutmut_6'

x_is_symlink_escape__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_is_symlink_escape__mutmut_1': x_is_symlink_escape__mutmut_1, 
    'x_is_symlink_escape__mutmut_2': x_is_symlink_escape__mutmut_2, 
    'x_is_symlink_escape__mutmut_3': x_is_symlink_escape__mutmut_3, 
    'x_is_symlink_escape__mutmut_4': x_is_symlink_escape__mutmut_4, 
    'x_is_symlink_escape__mutmut_5': x_is_symlink_escape__mutmut_5, 
    'x_is_symlink_escape__mutmut_6': x_is_symlink_escape__mutmut_6
}
x_is_symlink_escape__mutmut_orig.__name__ = 'x_is_symlink_escape'


def can_flow_to_destructive(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, args, kwargs, None)


def x_can_flow_to_destructive__mutmut_orig(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, args, kwargs, None)


def x_can_flow_to_destructive__mutmut_1(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, args, kwargs, None)


def x_can_flow_to_destructive__mutmut_2(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, args, kwargs, None)


def x_can_flow_to_destructive__mutmut_3(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_can_flow_to_destructive__mutmut_mutants, args, kwargs, None)


def x_can_flow_to_destructive__mutmut_4(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, None, args, kwargs, None)


def x_can_flow_to_destructive__mutmut_5(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, None, kwargs, None)


def x_can_flow_to_destructive__mutmut_6(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, args, None, None)


def x_can_flow_to_destructive__mutmut_7(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_mutants, args, kwargs, None)


def x_can_flow_to_destructive__mutmut_8(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, args, kwargs, None)


def x_can_flow_to_destructive__mutmut_9(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, kwargs, None)


def x_can_flow_to_destructive__mutmut_10(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, args, None)


def x_can_flow_to_destructive__mutmut_11(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_can_flow_to_destructive__mutmut_orig, x_can_flow_to_destructive__mutmut_mutants, args, kwargs, )

x_can_flow_to_destructive__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_can_flow_to_destructive__mutmut_1': x_can_flow_to_destructive__mutmut_1, 
    'x_can_flow_to_destructive__mutmut_2': x_can_flow_to_destructive__mutmut_2, 
    'x_can_flow_to_destructive__mutmut_3': x_can_flow_to_destructive__mutmut_3, 
    'x_can_flow_to_destructive__mutmut_4': x_can_flow_to_destructive__mutmut_4, 
    'x_can_flow_to_destructive__mutmut_5': x_can_flow_to_destructive__mutmut_5, 
    'x_can_flow_to_destructive__mutmut_6': x_can_flow_to_destructive__mutmut_6, 
    'x_can_flow_to_destructive__mutmut_7': x_can_flow_to_destructive__mutmut_7, 
    'x_can_flow_to_destructive__mutmut_8': x_can_flow_to_destructive__mutmut_8, 
    'x_can_flow_to_destructive__mutmut_9': x_can_flow_to_destructive__mutmut_9, 
    'x_can_flow_to_destructive__mutmut_10': x_can_flow_to_destructive__mutmut_10, 
    'x_can_flow_to_destructive__mutmut_11': x_can_flow_to_destructive__mutmut_11
}
x_can_flow_to_destructive__mutmut_orig.__name__ = 'x_can_flow_to_destructive'


def x_can_flow_to_destructive__mutmut_orig(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_can_flow_to_destructive__mutmut_orig__mutmut_orig, x_x_can_flow_to_destructive__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_can_flow_to_destructive__mutmut_orig__mutmut_orig(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_orig__mutmut_1(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_orig__mutmut_2(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return False
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_orig__mutmut_3(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_orig__mutmut_4(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return True


def x_x_can_flow_to_destructive__mutmut_orig__mutmut_5(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return False

x_x_can_flow_to_destructive__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_can_flow_to_destructive__mutmut_orig__mutmut_1': x_x_can_flow_to_destructive__mutmut_orig__mutmut_1, 
    'x_x_can_flow_to_destructive__mutmut_orig__mutmut_2': x_x_can_flow_to_destructive__mutmut_orig__mutmut_2, 
    'x_x_can_flow_to_destructive__mutmut_orig__mutmut_3': x_x_can_flow_to_destructive__mutmut_orig__mutmut_3, 
    'x_x_can_flow_to_destructive__mutmut_orig__mutmut_4': x_x_can_flow_to_destructive__mutmut_orig__mutmut_4, 
    'x_x_can_flow_to_destructive__mutmut_orig__mutmut_5': x_x_can_flow_to_destructive__mutmut_orig__mutmut_5
}
x_x_can_flow_to_destructive__mutmut_orig__mutmut_orig.__name__ = 'x_x_can_flow_to_destructive__mutmut_orig'


def x_can_flow_to_destructive__mutmut_1(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_can_flow_to_destructive__mutmut_1__mutmut_orig, x_x_can_flow_to_destructive__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_can_flow_to_destructive__mutmut_1__mutmut_orig(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_1__mutmut_1(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_1__mutmut_2(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return False
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_1__mutmut_3(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return True
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_1__mutmut_4(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return True


def x_x_can_flow_to_destructive__mutmut_1__mutmut_5(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return False

x_x_can_flow_to_destructive__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_can_flow_to_destructive__mutmut_1__mutmut_1': x_x_can_flow_to_destructive__mutmut_1__mutmut_1, 
    'x_x_can_flow_to_destructive__mutmut_1__mutmut_2': x_x_can_flow_to_destructive__mutmut_1__mutmut_2, 
    'x_x_can_flow_to_destructive__mutmut_1__mutmut_3': x_x_can_flow_to_destructive__mutmut_1__mutmut_3, 
    'x_x_can_flow_to_destructive__mutmut_1__mutmut_4': x_x_can_flow_to_destructive__mutmut_1__mutmut_4, 
    'x_x_can_flow_to_destructive__mutmut_1__mutmut_5': x_x_can_flow_to_destructive__mutmut_1__mutmut_5
}
x_x_can_flow_to_destructive__mutmut_1__mutmut_orig.__name__ = 'x_x_can_flow_to_destructive__mutmut_1'


def x_can_flow_to_destructive__mutmut_2(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_can_flow_to_destructive__mutmut_2__mutmut_orig, x_x_can_flow_to_destructive__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_can_flow_to_destructive__mutmut_2__mutmut_orig(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return False
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_2__mutmut_1(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return False
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_2__mutmut_2(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_2__mutmut_3(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return False
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_2__mutmut_4(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return False
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return True


def x_x_can_flow_to_destructive__mutmut_2__mutmut_5(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return False
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return False

x_x_can_flow_to_destructive__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_can_flow_to_destructive__mutmut_2__mutmut_1': x_x_can_flow_to_destructive__mutmut_2__mutmut_1, 
    'x_x_can_flow_to_destructive__mutmut_2__mutmut_2': x_x_can_flow_to_destructive__mutmut_2__mutmut_2, 
    'x_x_can_flow_to_destructive__mutmut_2__mutmut_3': x_x_can_flow_to_destructive__mutmut_2__mutmut_3, 
    'x_x_can_flow_to_destructive__mutmut_2__mutmut_4': x_x_can_flow_to_destructive__mutmut_2__mutmut_4, 
    'x_x_can_flow_to_destructive__mutmut_2__mutmut_5': x_x_can_flow_to_destructive__mutmut_2__mutmut_5
}
x_x_can_flow_to_destructive__mutmut_2__mutmut_orig.__name__ = 'x_x_can_flow_to_destructive__mutmut_2'


def x_can_flow_to_destructive__mutmut_3(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_can_flow_to_destructive__mutmut_3__mutmut_orig, x_x_can_flow_to_destructive__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_can_flow_to_destructive__mutmut_3__mutmut_orig(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_3__mutmut_1(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return True
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_3__mutmut_2(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return False
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_3__mutmut_3(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_3__mutmut_4(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return True


def x_x_can_flow_to_destructive__mutmut_3__mutmut_5(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return False

x_x_can_flow_to_destructive__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_can_flow_to_destructive__mutmut_3__mutmut_1': x_x_can_flow_to_destructive__mutmut_3__mutmut_1, 
    'x_x_can_flow_to_destructive__mutmut_3__mutmut_2': x_x_can_flow_to_destructive__mutmut_3__mutmut_2, 
    'x_x_can_flow_to_destructive__mutmut_3__mutmut_3': x_x_can_flow_to_destructive__mutmut_3__mutmut_3, 
    'x_x_can_flow_to_destructive__mutmut_3__mutmut_4': x_x_can_flow_to_destructive__mutmut_3__mutmut_4, 
    'x_x_can_flow_to_destructive__mutmut_3__mutmut_5': x_x_can_flow_to_destructive__mutmut_3__mutmut_5
}
x_x_can_flow_to_destructive__mutmut_3__mutmut_orig.__name__ = 'x_x_can_flow_to_destructive__mutmut_3'


def x_can_flow_to_destructive__mutmut_4(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_can_flow_to_destructive__mutmut_4__mutmut_orig, x_x_can_flow_to_destructive__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_can_flow_to_destructive__mutmut_4__mutmut_orig(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return True


def x_x_can_flow_to_destructive__mutmut_4__mutmut_1(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return True


def x_x_can_flow_to_destructive__mutmut_4__mutmut_2(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return False
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return True


def x_x_can_flow_to_destructive__mutmut_4__mutmut_3(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return True


def x_x_can_flow_to_destructive__mutmut_4__mutmut_4(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True


def x_x_can_flow_to_destructive__mutmut_4__mutmut_5(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return False

x_x_can_flow_to_destructive__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_can_flow_to_destructive__mutmut_4__mutmut_1': x_x_can_flow_to_destructive__mutmut_4__mutmut_1, 
    'x_x_can_flow_to_destructive__mutmut_4__mutmut_2': x_x_can_flow_to_destructive__mutmut_4__mutmut_2, 
    'x_x_can_flow_to_destructive__mutmut_4__mutmut_3': x_x_can_flow_to_destructive__mutmut_4__mutmut_3, 
    'x_x_can_flow_to_destructive__mutmut_4__mutmut_4': x_x_can_flow_to_destructive__mutmut_4__mutmut_4, 
    'x_x_can_flow_to_destructive__mutmut_4__mutmut_5': x_x_can_flow_to_destructive__mutmut_4__mutmut_5
}
x_x_can_flow_to_destructive__mutmut_4__mutmut_orig.__name__ = 'x_x_can_flow_to_destructive__mutmut_4'


def x_can_flow_to_destructive__mutmut_5(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    args = [taint, target_tool]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_can_flow_to_destructive__mutmut_5__mutmut_orig, x_x_can_flow_to_destructive__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_can_flow_to_destructive__mutmut_5__mutmut_orig(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return False


def x_x_can_flow_to_destructive__mutmut_5__mutmut_1(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint != TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return False


def x_x_can_flow_to_destructive__mutmut_5__mutmut_2(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return False
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return False


def x_x_can_flow_to_destructive__mutmut_5__mutmut_3(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool not in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return False


def x_x_can_flow_to_destructive__mutmut_5__mutmut_4(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return True
    return False


def x_x_can_flow_to_destructive__mutmut_5__mutmut_5(taint: TaintFlag, target_tool: ToolPermission) -> bool:
    if taint == TaintFlag.CLEAN:
        return True
    if target_tool in (ToolPermission.WRITE, ToolPermission.BASH):
        return False
    return True

x_x_can_flow_to_destructive__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_can_flow_to_destructive__mutmut_5__mutmut_1': x_x_can_flow_to_destructive__mutmut_5__mutmut_1, 
    'x_x_can_flow_to_destructive__mutmut_5__mutmut_2': x_x_can_flow_to_destructive__mutmut_5__mutmut_2, 
    'x_x_can_flow_to_destructive__mutmut_5__mutmut_3': x_x_can_flow_to_destructive__mutmut_5__mutmut_3, 
    'x_x_can_flow_to_destructive__mutmut_5__mutmut_4': x_x_can_flow_to_destructive__mutmut_5__mutmut_4, 
    'x_x_can_flow_to_destructive__mutmut_5__mutmut_5': x_x_can_flow_to_destructive__mutmut_5__mutmut_5
}
x_x_can_flow_to_destructive__mutmut_5__mutmut_orig.__name__ = 'x_x_can_flow_to_destructive__mutmut_5'

x_can_flow_to_destructive__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_can_flow_to_destructive__mutmut_1': x_can_flow_to_destructive__mutmut_1, 
    'x_can_flow_to_destructive__mutmut_2': x_can_flow_to_destructive__mutmut_2, 
    'x_can_flow_to_destructive__mutmut_3': x_can_flow_to_destructive__mutmut_3, 
    'x_can_flow_to_destructive__mutmut_4': x_can_flow_to_destructive__mutmut_4, 
    'x_can_flow_to_destructive__mutmut_5': x_can_flow_to_destructive__mutmut_5
}
x_can_flow_to_destructive__mutmut_orig.__name__ = 'x_can_flow_to_destructive'


def escalate_capabilities(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, args, kwargs, None)


def x_escalate_capabilities__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, args, kwargs, None)


def x_escalate_capabilities__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = None# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, args, kwargs, None)


def x_escalate_capabilities__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = None# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, args, kwargs, None)


def x_escalate_capabilities__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(None, x_escalate_capabilities__mutmut_mutants, args, kwargs, None)


def x_escalate_capabilities__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, None, args, kwargs, None)


def x_escalate_capabilities__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, None, kwargs, None)


def x_escalate_capabilities__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, args, None, None)


def x_escalate_capabilities__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_mutants, args, kwargs, None)


def x_escalate_capabilities__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, args, kwargs, None)


def x_escalate_capabilities__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, kwargs, None)


def x_escalate_capabilities__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, args, None)


def x_escalate_capabilities__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_escalate_capabilities__mutmut_orig, x_escalate_capabilities__mutmut_mutants, args, kwargs, )

x_escalate_capabilities__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_escalate_capabilities__mutmut_1': x_escalate_capabilities__mutmut_1, 
    'x_escalate_capabilities__mutmut_2': x_escalate_capabilities__mutmut_2, 
    'x_escalate_capabilities__mutmut_3': x_escalate_capabilities__mutmut_3, 
    'x_escalate_capabilities__mutmut_4': x_escalate_capabilities__mutmut_4, 
    'x_escalate_capabilities__mutmut_5': x_escalate_capabilities__mutmut_5, 
    'x_escalate_capabilities__mutmut_6': x_escalate_capabilities__mutmut_6, 
    'x_escalate_capabilities__mutmut_7': x_escalate_capabilities__mutmut_7, 
    'x_escalate_capabilities__mutmut_8': x_escalate_capabilities__mutmut_8, 
    'x_escalate_capabilities__mutmut_9': x_escalate_capabilities__mutmut_9, 
    'x_escalate_capabilities__mutmut_10': x_escalate_capabilities__mutmut_10, 
    'x_escalate_capabilities__mutmut_11': x_escalate_capabilities__mutmut_11
}
x_escalate_capabilities__mutmut_orig.__name__ = 'x_escalate_capabilities'


def x_escalate_capabilities__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_orig__mutmut_orig, x_x_escalate_capabilities__mutmut_orig__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_orig__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_orig__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_orig__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_orig__mutmut_1': x_x_escalate_capabilities__mutmut_orig__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_2': x_x_escalate_capabilities__mutmut_orig__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_3': x_x_escalate_capabilities__mutmut_orig__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_4': x_x_escalate_capabilities__mutmut_orig__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_5': x_x_escalate_capabilities__mutmut_orig__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_6': x_x_escalate_capabilities__mutmut_orig__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_7': x_x_escalate_capabilities__mutmut_orig__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_8': x_x_escalate_capabilities__mutmut_orig__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_9': x_x_escalate_capabilities__mutmut_orig__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_10': x_x_escalate_capabilities__mutmut_orig__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_11': x_x_escalate_capabilities__mutmut_orig__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_12': x_x_escalate_capabilities__mutmut_orig__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_13': x_x_escalate_capabilities__mutmut_orig__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_14': x_x_escalate_capabilities__mutmut_orig__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_orig__mutmut_15': x_x_escalate_capabilities__mutmut_orig__mutmut_15
}
x_x_escalate_capabilities__mutmut_orig__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_orig'


def x_escalate_capabilities__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_1__mutmut_orig, x_x_escalate_capabilities__mutmut_1__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_1__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = ""
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_1__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_1__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_1__mutmut_1': x_x_escalate_capabilities__mutmut_1__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_2': x_x_escalate_capabilities__mutmut_1__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_3': x_x_escalate_capabilities__mutmut_1__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_4': x_x_escalate_capabilities__mutmut_1__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_5': x_x_escalate_capabilities__mutmut_1__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_6': x_x_escalate_capabilities__mutmut_1__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_7': x_x_escalate_capabilities__mutmut_1__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_8': x_x_escalate_capabilities__mutmut_1__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_9': x_x_escalate_capabilities__mutmut_1__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_10': x_x_escalate_capabilities__mutmut_1__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_11': x_x_escalate_capabilities__mutmut_1__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_12': x_x_escalate_capabilities__mutmut_1__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_13': x_x_escalate_capabilities__mutmut_1__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_14': x_x_escalate_capabilities__mutmut_1__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_1__mutmut_15': x_x_escalate_capabilities__mutmut_1__mutmut_15
}
x_x_escalate_capabilities__mutmut_1__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_1'


def x_escalate_capabilities__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_2__mutmut_orig, x_x_escalate_capabilities__mutmut_2__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_2__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = ""
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_2__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_2__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_2__mutmut_1': x_x_escalate_capabilities__mutmut_2__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_2': x_x_escalate_capabilities__mutmut_2__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_3': x_x_escalate_capabilities__mutmut_2__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_4': x_x_escalate_capabilities__mutmut_2__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_5': x_x_escalate_capabilities__mutmut_2__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_6': x_x_escalate_capabilities__mutmut_2__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_7': x_x_escalate_capabilities__mutmut_2__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_8': x_x_escalate_capabilities__mutmut_2__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_9': x_x_escalate_capabilities__mutmut_2__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_10': x_x_escalate_capabilities__mutmut_2__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_11': x_x_escalate_capabilities__mutmut_2__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_12': x_x_escalate_capabilities__mutmut_2__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_13': x_x_escalate_capabilities__mutmut_2__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_14': x_x_escalate_capabilities__mutmut_2__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_2__mutmut_15': x_x_escalate_capabilities__mutmut_2__mutmut_15
}
x_x_escalate_capabilities__mutmut_2__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_2'


def x_escalate_capabilities__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_3__mutmut_orig, x_x_escalate_capabilities__mutmut_3__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_3__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_3__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_3__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_3__mutmut_1': x_x_escalate_capabilities__mutmut_3__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_2': x_x_escalate_capabilities__mutmut_3__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_3': x_x_escalate_capabilities__mutmut_3__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_4': x_x_escalate_capabilities__mutmut_3__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_5': x_x_escalate_capabilities__mutmut_3__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_6': x_x_escalate_capabilities__mutmut_3__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_7': x_x_escalate_capabilities__mutmut_3__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_8': x_x_escalate_capabilities__mutmut_3__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_9': x_x_escalate_capabilities__mutmut_3__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_10': x_x_escalate_capabilities__mutmut_3__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_11': x_x_escalate_capabilities__mutmut_3__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_12': x_x_escalate_capabilities__mutmut_3__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_13': x_x_escalate_capabilities__mutmut_3__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_3__mutmut_14': x_x_escalate_capabilities__mutmut_3__mutmut_14
}
x_x_escalate_capabilities__mutmut_3__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_3'


def x_escalate_capabilities__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_4__mutmut_orig, x_x_escalate_capabilities__mutmut_4__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_4__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_4__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_4__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_4__mutmut_1': x_x_escalate_capabilities__mutmut_4__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_2': x_x_escalate_capabilities__mutmut_4__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_3': x_x_escalate_capabilities__mutmut_4__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_4': x_x_escalate_capabilities__mutmut_4__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_5': x_x_escalate_capabilities__mutmut_4__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_6': x_x_escalate_capabilities__mutmut_4__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_7': x_x_escalate_capabilities__mutmut_4__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_8': x_x_escalate_capabilities__mutmut_4__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_9': x_x_escalate_capabilities__mutmut_4__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_10': x_x_escalate_capabilities__mutmut_4__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_11': x_x_escalate_capabilities__mutmut_4__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_12': x_x_escalate_capabilities__mutmut_4__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_13': x_x_escalate_capabilities__mutmut_4__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_4__mutmut_14': x_x_escalate_capabilities__mutmut_4__mutmut_14
}
x_x_escalate_capabilities__mutmut_4__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_4'


def x_escalate_capabilities__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_5__mutmut_orig, x_x_escalate_capabilities__mutmut_5__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_5__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_5__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_5__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_5__mutmut_1': x_x_escalate_capabilities__mutmut_5__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_2': x_x_escalate_capabilities__mutmut_5__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_3': x_x_escalate_capabilities__mutmut_5__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_4': x_x_escalate_capabilities__mutmut_5__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_5': x_x_escalate_capabilities__mutmut_5__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_6': x_x_escalate_capabilities__mutmut_5__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_7': x_x_escalate_capabilities__mutmut_5__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_8': x_x_escalate_capabilities__mutmut_5__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_9': x_x_escalate_capabilities__mutmut_5__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_10': x_x_escalate_capabilities__mutmut_5__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_11': x_x_escalate_capabilities__mutmut_5__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_12': x_x_escalate_capabilities__mutmut_5__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_13': x_x_escalate_capabilities__mutmut_5__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_14': x_x_escalate_capabilities__mutmut_5__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_5__mutmut_15': x_x_escalate_capabilities__mutmut_5__mutmut_15
}
x_x_escalate_capabilities__mutmut_5__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_5'


def x_escalate_capabilities__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_6__mutmut_orig, x_x_escalate_capabilities__mutmut_6__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_6__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_6__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_6__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_6__mutmut_1': x_x_escalate_capabilities__mutmut_6__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_2': x_x_escalate_capabilities__mutmut_6__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_3': x_x_escalate_capabilities__mutmut_6__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_4': x_x_escalate_capabilities__mutmut_6__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_5': x_x_escalate_capabilities__mutmut_6__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_6': x_x_escalate_capabilities__mutmut_6__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_7': x_x_escalate_capabilities__mutmut_6__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_8': x_x_escalate_capabilities__mutmut_6__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_9': x_x_escalate_capabilities__mutmut_6__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_10': x_x_escalate_capabilities__mutmut_6__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_11': x_x_escalate_capabilities__mutmut_6__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_12': x_x_escalate_capabilities__mutmut_6__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_13': x_x_escalate_capabilities__mutmut_6__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_14': x_x_escalate_capabilities__mutmut_6__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_6__mutmut_15': x_x_escalate_capabilities__mutmut_6__mutmut_15
}
x_x_escalate_capabilities__mutmut_6__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_6'


def x_escalate_capabilities__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_7__mutmut_orig, x_x_escalate_capabilities__mutmut_7__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_7__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_7__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_7__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_7__mutmut_1': x_x_escalate_capabilities__mutmut_7__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_2': x_x_escalate_capabilities__mutmut_7__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_3': x_x_escalate_capabilities__mutmut_7__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_4': x_x_escalate_capabilities__mutmut_7__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_5': x_x_escalate_capabilities__mutmut_7__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_6': x_x_escalate_capabilities__mutmut_7__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_7': x_x_escalate_capabilities__mutmut_7__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_8': x_x_escalate_capabilities__mutmut_7__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_9': x_x_escalate_capabilities__mutmut_7__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_10': x_x_escalate_capabilities__mutmut_7__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_11': x_x_escalate_capabilities__mutmut_7__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_12': x_x_escalate_capabilities__mutmut_7__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_13': x_x_escalate_capabilities__mutmut_7__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_7__mutmut_14': x_x_escalate_capabilities__mutmut_7__mutmut_14
}
x_x_escalate_capabilities__mutmut_7__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_7'


def x_escalate_capabilities__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_8__mutmut_orig, x_x_escalate_capabilities__mutmut_8__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_8__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_8__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_8__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_8__mutmut_1': x_x_escalate_capabilities__mutmut_8__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_2': x_x_escalate_capabilities__mutmut_8__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_3': x_x_escalate_capabilities__mutmut_8__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_4': x_x_escalate_capabilities__mutmut_8__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_5': x_x_escalate_capabilities__mutmut_8__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_6': x_x_escalate_capabilities__mutmut_8__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_7': x_x_escalate_capabilities__mutmut_8__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_8': x_x_escalate_capabilities__mutmut_8__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_9': x_x_escalate_capabilities__mutmut_8__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_10': x_x_escalate_capabilities__mutmut_8__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_11': x_x_escalate_capabilities__mutmut_8__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_12': x_x_escalate_capabilities__mutmut_8__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_13': x_x_escalate_capabilities__mutmut_8__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_14': x_x_escalate_capabilities__mutmut_8__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_8__mutmut_15': x_x_escalate_capabilities__mutmut_8__mutmut_15
}
x_x_escalate_capabilities__mutmut_8__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_8'


def x_escalate_capabilities__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_9__mutmut_orig, x_x_escalate_capabilities__mutmut_9__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_9__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_9__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_9__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_9__mutmut_1': x_x_escalate_capabilities__mutmut_9__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_2': x_x_escalate_capabilities__mutmut_9__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_3': x_x_escalate_capabilities__mutmut_9__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_4': x_x_escalate_capabilities__mutmut_9__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_5': x_x_escalate_capabilities__mutmut_9__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_6': x_x_escalate_capabilities__mutmut_9__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_7': x_x_escalate_capabilities__mutmut_9__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_8': x_x_escalate_capabilities__mutmut_9__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_9': x_x_escalate_capabilities__mutmut_9__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_10': x_x_escalate_capabilities__mutmut_9__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_11': x_x_escalate_capabilities__mutmut_9__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_12': x_x_escalate_capabilities__mutmut_9__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_13': x_x_escalate_capabilities__mutmut_9__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_14': x_x_escalate_capabilities__mutmut_9__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_9__mutmut_15': x_x_escalate_capabilities__mutmut_9__mutmut_15
}
x_x_escalate_capabilities__mutmut_9__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_9'


def x_escalate_capabilities__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_10__mutmut_orig, x_x_escalate_capabilities__mutmut_10__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_10__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_10__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_10__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_10__mutmut_1': x_x_escalate_capabilities__mutmut_10__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_2': x_x_escalate_capabilities__mutmut_10__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_3': x_x_escalate_capabilities__mutmut_10__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_4': x_x_escalate_capabilities__mutmut_10__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_5': x_x_escalate_capabilities__mutmut_10__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_6': x_x_escalate_capabilities__mutmut_10__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_7': x_x_escalate_capabilities__mutmut_10__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_8': x_x_escalate_capabilities__mutmut_10__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_9': x_x_escalate_capabilities__mutmut_10__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_10': x_x_escalate_capabilities__mutmut_10__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_11': x_x_escalate_capabilities__mutmut_10__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_12': x_x_escalate_capabilities__mutmut_10__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_13': x_x_escalate_capabilities__mutmut_10__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_10__mutmut_14': x_x_escalate_capabilities__mutmut_10__mutmut_14
}
x_x_escalate_capabilities__mutmut_10__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_10'


def x_escalate_capabilities__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_11__mutmut_orig, x_x_escalate_capabilities__mutmut_11__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_11__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_11__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_11__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_11__mutmut_1': x_x_escalate_capabilities__mutmut_11__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_2': x_x_escalate_capabilities__mutmut_11__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_3': x_x_escalate_capabilities__mutmut_11__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_4': x_x_escalate_capabilities__mutmut_11__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_5': x_x_escalate_capabilities__mutmut_11__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_6': x_x_escalate_capabilities__mutmut_11__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_7': x_x_escalate_capabilities__mutmut_11__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_8': x_x_escalate_capabilities__mutmut_11__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_9': x_x_escalate_capabilities__mutmut_11__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_10': x_x_escalate_capabilities__mutmut_11__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_11': x_x_escalate_capabilities__mutmut_11__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_12': x_x_escalate_capabilities__mutmut_11__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_13': x_x_escalate_capabilities__mutmut_11__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_14': x_x_escalate_capabilities__mutmut_11__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_11__mutmut_15': x_x_escalate_capabilities__mutmut_11__mutmut_15
}
x_x_escalate_capabilities__mutmut_11__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_11'


def x_escalate_capabilities__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_12__mutmut_orig, x_x_escalate_capabilities__mutmut_12__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_12__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_12__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_12__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_12__mutmut_1': x_x_escalate_capabilities__mutmut_12__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_2': x_x_escalate_capabilities__mutmut_12__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_3': x_x_escalate_capabilities__mutmut_12__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_4': x_x_escalate_capabilities__mutmut_12__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_5': x_x_escalate_capabilities__mutmut_12__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_6': x_x_escalate_capabilities__mutmut_12__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_7': x_x_escalate_capabilities__mutmut_12__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_8': x_x_escalate_capabilities__mutmut_12__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_9': x_x_escalate_capabilities__mutmut_12__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_10': x_x_escalate_capabilities__mutmut_12__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_11': x_x_escalate_capabilities__mutmut_12__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_12': x_x_escalate_capabilities__mutmut_12__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_13': x_x_escalate_capabilities__mutmut_12__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_12__mutmut_14': x_x_escalate_capabilities__mutmut_12__mutmut_14
}
x_x_escalate_capabilities__mutmut_12__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_12'


def x_escalate_capabilities__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_13__mutmut_orig, x_x_escalate_capabilities__mutmut_13__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_13__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(None):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_13__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, False

x_x_escalate_capabilities__mutmut_13__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_13__mutmut_1': x_x_escalate_capabilities__mutmut_13__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_2': x_x_escalate_capabilities__mutmut_13__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_3': x_x_escalate_capabilities__mutmut_13__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_4': x_x_escalate_capabilities__mutmut_13__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_5': x_x_escalate_capabilities__mutmut_13__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_6': x_x_escalate_capabilities__mutmut_13__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_7': x_x_escalate_capabilities__mutmut_13__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_8': x_x_escalate_capabilities__mutmut_13__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_9': x_x_escalate_capabilities__mutmut_13__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_10': x_x_escalate_capabilities__mutmut_13__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_11': x_x_escalate_capabilities__mutmut_13__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_12': x_x_escalate_capabilities__mutmut_13__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_13': x_x_escalate_capabilities__mutmut_13__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_13__mutmut_14': x_x_escalate_capabilities__mutmut_13__mutmut_14
}
x_x_escalate_capabilities__mutmut_13__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_13'


def x_escalate_capabilities__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_14__mutmut_orig, x_x_escalate_capabilities__mutmut_14__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_14__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, True
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True


def x_x_escalate_capabilities__mutmut_14__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, False

x_x_escalate_capabilities__mutmut_14__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_14__mutmut_1': x_x_escalate_capabilities__mutmut_14__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_2': x_x_escalate_capabilities__mutmut_14__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_3': x_x_escalate_capabilities__mutmut_14__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_4': x_x_escalate_capabilities__mutmut_14__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_5': x_x_escalate_capabilities__mutmut_14__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_6': x_x_escalate_capabilities__mutmut_14__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_7': x_x_escalate_capabilities__mutmut_14__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_8': x_x_escalate_capabilities__mutmut_14__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_9': x_x_escalate_capabilities__mutmut_14__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_10': x_x_escalate_capabilities__mutmut_14__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_11': x_x_escalate_capabilities__mutmut_14__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_12': x_x_escalate_capabilities__mutmut_14__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_13': x_x_escalate_capabilities__mutmut_14__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_14': x_x_escalate_capabilities__mutmut_14__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_14__mutmut_15': x_x_escalate_capabilities__mutmut_14__mutmut_15
}
x_x_escalate_capabilities__mutmut_14__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_14'


def x_escalate_capabilities__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    args = [current, requested]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_x_escalate_capabilities__mutmut_15__mutmut_orig, x_x_escalate_capabilities__mutmut_15__mutmut_mutants, args, kwargs, None)


def x_x_escalate_capabilities__mutmut_15__mutmut_orig(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_1(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = None
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_2(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = None
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_3(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_4(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(None):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_5(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, True
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_6(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network or not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_7(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_8(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, True
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_9(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write or not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_10(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_11(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, True
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_12(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_13(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(None):
        return current, False
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_14(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, True
    return requested, False


def x_x_escalate_capabilities__mutmut_15__mutmut_15(current: AgentCapabilities, requested: AgentCapabilities) -> tuple[AgentCapabilities, bool]:
    current_tools = current.allowed_tools
    requested_tools = requested.allowed_tools
    if not requested_tools.issubset(current_tools):
        return current, False
    if requested.can_network and not current.can_network:
        return current, False
    if requested.can_write and not current.can_write:
        return current, False
    if not requested.allowed_paths.issubset(current.allowed_paths):
        return current, False
    return requested, True

x_x_escalate_capabilities__mutmut_15__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_x_escalate_capabilities__mutmut_15__mutmut_1': x_x_escalate_capabilities__mutmut_15__mutmut_1, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_2': x_x_escalate_capabilities__mutmut_15__mutmut_2, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_3': x_x_escalate_capabilities__mutmut_15__mutmut_3, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_4': x_x_escalate_capabilities__mutmut_15__mutmut_4, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_5': x_x_escalate_capabilities__mutmut_15__mutmut_5, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_6': x_x_escalate_capabilities__mutmut_15__mutmut_6, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_7': x_x_escalate_capabilities__mutmut_15__mutmut_7, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_8': x_x_escalate_capabilities__mutmut_15__mutmut_8, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_9': x_x_escalate_capabilities__mutmut_15__mutmut_9, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_10': x_x_escalate_capabilities__mutmut_15__mutmut_10, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_11': x_x_escalate_capabilities__mutmut_15__mutmut_11, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_12': x_x_escalate_capabilities__mutmut_15__mutmut_12, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_13': x_x_escalate_capabilities__mutmut_15__mutmut_13, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_14': x_x_escalate_capabilities__mutmut_15__mutmut_14, 
    'x_x_escalate_capabilities__mutmut_15__mutmut_15': x_x_escalate_capabilities__mutmut_15__mutmut_15
}
x_x_escalate_capabilities__mutmut_15__mutmut_orig.__name__ = 'x_x_escalate_capabilities__mutmut_15'

x_escalate_capabilities__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_escalate_capabilities__mutmut_1': x_escalate_capabilities__mutmut_1, 
    'x_escalate_capabilities__mutmut_2': x_escalate_capabilities__mutmut_2, 
    'x_escalate_capabilities__mutmut_3': x_escalate_capabilities__mutmut_3, 
    'x_escalate_capabilities__mutmut_4': x_escalate_capabilities__mutmut_4, 
    'x_escalate_capabilities__mutmut_5': x_escalate_capabilities__mutmut_5, 
    'x_escalate_capabilities__mutmut_6': x_escalate_capabilities__mutmut_6, 
    'x_escalate_capabilities__mutmut_7': x_escalate_capabilities__mutmut_7, 
    'x_escalate_capabilities__mutmut_8': x_escalate_capabilities__mutmut_8, 
    'x_escalate_capabilities__mutmut_9': x_escalate_capabilities__mutmut_9, 
    'x_escalate_capabilities__mutmut_10': x_escalate_capabilities__mutmut_10, 
    'x_escalate_capabilities__mutmut_11': x_escalate_capabilities__mutmut_11, 
    'x_escalate_capabilities__mutmut_12': x_escalate_capabilities__mutmut_12, 
    'x_escalate_capabilities__mutmut_13': x_escalate_capabilities__mutmut_13, 
    'x_escalate_capabilities__mutmut_14': x_escalate_capabilities__mutmut_14, 
    'x_escalate_capabilities__mutmut_15': x_escalate_capabilities__mutmut_15
}
x_escalate_capabilities__mutmut_orig.__name__ = 'x_escalate_capabilities'
