"""Run submission-ready solutions against JSON fixtures.

Node types belong to the platform adapter, keeping submitted source files free
of local test definitions. Calls copy their inputs so in-place solutions cannot
change shared fixtures or later invocations.
"""

import importlib.util
import json
from collections import deque
from copy import deepcopy
from pathlib import Path
from types import ModuleType
from typing import Any
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = ROOT / "problems"


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def _folder_path(folder: str | Path) -> Path:
    candidate = Path(folder)
    path = candidate if candidate.is_absolute() else PROBLEMS / candidate
    path = path.resolve()
    if path.parent != PROBLEMS.resolve() or not path.is_dir():
        raise ValueError(f"Not a problem folder: {folder}")
    return path


def metadata(folder: str | Path) -> dict[str, Any]:
    return json.loads((_folder_path(folder) / "meta.json").read_text())


def problem_dirs() -> list[Path]:
    return sorted(
        (path for path in PROBLEMS.iterdir() if path.is_dir() and (path / "meta.json").is_file()),
        key=lambda path: metadata(path)["id"],
    )


def load_module(folder: str | Path) -> ModuleType:
    """Load a fresh solution namespace with platform node globals injected."""
    path = _folder_path(folder) / "solution.py"
    name = f"atlas_solution_{path.parent.name.replace('-', '_')}_{uuid4().hex}"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load solution: {path}")
    module = importlib.util.module_from_spec(spec)
    module.ListNode = ListNode
    module.TreeNode = TreeNode
    spec.loader.exec_module(module)
    return module


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def list_to_json(head: ListNode | None) -> list[int]:
    values = []
    seen: set[int] = set()
    while head is not None:
        if id(head) in seen:
            raise ValueError("Linked-list result contains a cycle")
        seen.add(id(head))
        values.append(head.val)
        head = head.next
    return values


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Decode LeetCode's queue-based level order, including sparse children."""
    if not values:
        return None
    if values[0] is None:
        if any(value is not None for value in values[1:]):
            raise ValueError("Tree values cannot follow an absent root")
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        parent = queue.popleft()
        for field in ("left", "right"):
            if index == len(values):
                break
            value = values[index]
            index += 1
            if value is not None:
                child = TreeNode(value)
                setattr(parent, field, child)
                queue.append(child)
    if any(value is not None for value in values[index:]):
        raise ValueError("Tree fixture contains unreachable node values")
    return root


def tree_to_json(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []
    values = []
    queue = deque([root])
    seen: set[int] = set()
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        if id(node) in seen:
            raise ValueError("Tree result contains a cycle or a shared child")
        seen.add(id(node))
        values.append(node.val)
        queue.extend((node.left, node.right))
    while values and values[-1] is None:
        values.pop()
    return values


def _adapt(value: Any, kind: str) -> Any:
    if kind == "value":
        return value
    if kind == "listnode":
        return build_list(value)
    if kind == "treenode":
        return build_tree(value)
    raise ValueError(f"Unknown argument type: {kind}")


def _serialize(value: Any, kind: str) -> Any:
    if kind == "value":
        return value
    if kind == "listnode":
        return list_to_json(value)
    if kind == "treenode":
        return tree_to_json(value)
    raise ValueError(f"Unknown return type: {kind}")


def evaluate(
    folder: str | Path,
    args: list[Any] | None = None,
    operations: list[str] | None = None,
    arguments: list[list[Any]] | None = None,
) -> Any:
    meta = metadata(folder)
    module = load_module(folder)
    if meta["kind"] == "method":
        if args is None or operations is not None or arguments is not None:
            raise ValueError("Method cases require args only")
        kinds = meta["args_types"]
        if len(args) != len(kinds):
            raise ValueError("Argument count does not match metadata")
        adapted = [_adapt(value, kind) for value, kind in zip(deepcopy(args), kinds, strict=True)]
        method = getattr(module.Solution(), meta["method"])
        return _serialize(method(*adapted), meta["return_type"])
    if meta["kind"] == "design":
        if args is not None or operations is None or arguments is None:
            raise ValueError("Design cases require operations and arguments only")
        if (
            not operations
            or len(operations) != len(arguments)
            or any(not isinstance(operation, str) for operation in operations)
        ):
            raise ValueError("Design operation and argument lengths must match and be nonempty")
        class_name = meta["class_name"]
        if operations[0] != class_name:
            raise ValueError(f"First design operation must construct {class_name}")
        if any(not isinstance(item, list) for item in arguments):
            raise ValueError("Each design argument entry must be a list")
        copied = deepcopy(arguments)
        instance = getattr(module, class_name)(*copied[0])
        results = [None]
        for operation, operation_args in zip(operations[1:], copied[1:], strict=True):
            if operation.startswith("_") or operation == class_name:
                raise ValueError(f"Invalid design operation: {operation}")
            results.append(getattr(instance, operation)(*operation_args))
        return results
    raise ValueError(f"Unknown problem kind: {meta['kind']}")


def _json_key(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def normalize(meta: dict[str, Any], result: Any) -> Any:
    """Apply only the ordering freedom declared by a problem's checker.

    unordered ignores flat item order; unordered_rows ignores outer row order;
    unordered_groups ignores both member and group order. Duplicates survive.
    """
    checker = meta.get("checker", "exact")
    if checker == "exact":
        return result
    if not isinstance(result, list):
        raise ValueError(f"{checker} checker requires a list result")
    if checker == "unordered":
        if any(isinstance(value, (list, dict)) for value in result):
            raise ValueError("unordered checker requires a flat list")
        return sorted(result, key=_json_key)
    if checker == "unordered_rows":
        if any(not isinstance(row, list) for row in result):
            raise ValueError("unordered_rows checker requires a list of rows")
        return sorted(result, key=_json_key)
    if checker == "unordered_groups":
        if any(not isinstance(group, list) for group in result):
            raise ValueError("unordered_groups checker requires a list of groups")
        if any(isinstance(value, (list, dict)) for group in result for value in group):
            raise ValueError("unordered_groups checker requires flat groups")
        return sorted((sorted(group, key=_json_key) for group in result), key=_json_key)
    raise ValueError(f"Unknown checker: {checker}")


def check_result(meta: dict[str, Any], actual: Any, expected: Any) -> bool:
    """Compare JSON values with explicit ordering rules and scalar types."""
    return _json_key(normalize(meta, actual)) == _json_key(normalize(meta, expected))
