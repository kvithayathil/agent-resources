import time
import uuid

from security_layer.models import DESTRUCTIVE_ACTIONS, HITLRequest

_requests: dict[str, dict] = {}
_action_index: dict[tuple[str, str], list[str]] = {}


def _index_insert(request_id: str, request: HITLRequest) -> None:
    key = (request.action, request.target)
    if key not in _action_index:
        _action_index[key] = []
    _action_index[key].append(request_id)


def is_destructive(action: str) -> bool:
    return action in DESTRUCTIVE_ACTIONS


def request_approval(request: HITLRequest) -> str:
    request_id = str(uuid.uuid4())
    _requests[request_id] = {
        "request": request,
        "status": "pending",
        "created_at": time.time(),
    }
    _index_insert(request_id, request)
    return request_id


def check_approval(request_id: str) -> str:
    entry = _requests.get(request_id)
    if entry is None:
        return "not_found"
    return entry["status"]


def approve(request_id: str) -> bool:
    entry = _requests.get(request_id)
    if entry is None:
        return False
    entry["status"] = "approved"
    return True


def deny(request_id: str) -> bool:
    entry = _requests.get(request_id)
    if entry is None:
        return False
    entry["status"] = "denied"
    return True


def check_timeout(request: HITLRequest, created_at: float, current_time: float | None = None) -> bool:
    if current_time is None:
        current_time = time.time()
    elapsed = current_time - created_at
    return elapsed > request.timeout_minutes * 60


def process_destructive_action(action: str, target: str, reason: str) -> tuple[bool, str]:
    if not is_destructive(action):
        return True, "Non-destructive action allowed"
    key = (action, target)
    request_ids = _action_index.get(key)
    if not request_ids:
        return False, "Action not approved or not requested"
    latest_id = request_ids[-1]
    entry = _requests.get(latest_id)
    if entry is None:
        return False, "Action not approved or not requested"
    status = entry["status"]
    if status == "approved":
        return True, "Action approved"
    if status == "denied":
        return False, "Action denied"
    return False, "Action pending approval"


def reset() -> None:
    _requests.clear()
    _action_index.clear()
