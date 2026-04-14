from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from enum import Enum
from typing import Generic, TypeVar

S = TypeVar("S", bound=Enum)
E = TypeVar("E", bound=Enum)
C = TypeVar("C")

Action = Callable[[C], None]
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


class InvalidTransition(Exception):
    pass


@dataclass
class StateMachine(Generic[S, E, C]):
    transitions: dict[tuple[S, E], tuple[S, Action[C]]] = field(default_factory=dict)

    def add_transition(
        self, from_state: S, event: E, to_state: S, action: Action[C]
    ) -> None:
        self.transitions[(from_state, event)] = (to_state, action)

    def next_transition(self, state: S, event: E) -> tuple[S, Action[C]]:
        if (transition := self.transitions.get((state, event))) is None:
            raise InvalidTransition(
                f"Invalid transition from {state!r} on event {event!r}"
            )
        return transition

    def handle(self, context: C, state: S, event: E) -> S:
        next_state, action = self.next_transition(state, event)
        action(context)
        return next_state

    def transition(
        self, from_state: S | Iterable[S], event: E, to_state: S
    ) -> Callable[[Action[C]], Action[C]]:
        if isinstance(from_state, Enum) or not isinstance(from_state, Iterable):
            from_state = (from_state,)

        def decorator(action: Action[C]) -> Action[C]:
            for s in from_state:
                self.add_transition(s, event, to_state, action)
            return action

        return decorator
