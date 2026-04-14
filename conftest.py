import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent / "security_layer"))


@pytest.fixture(autouse=True)
def _reset_hitl_state():
    yield
    from security_layer.hitl import reset

    reset()
