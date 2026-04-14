from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from enum import Enum
from typing import Generic, TypeVar

S = TypeVar("S", bound=Enum)
E = TypeVar("E", bound=Enum)
C = TypeVar("C")

Action = Callable[[C], None]


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
