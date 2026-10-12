"""Run submission-ready solutions against JSON fixtures.

Node types belong to the platform adapter, keeping submitted source files free
of local test definitions. Calls copy their inputs so in-place solutions cannot
change shared fixtures or later invocations.
"""

import importlib.util
import json
import math
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


class GraphNode:
    def __init__(self, val: int = 0, neighbors: "list[GraphNode] | None" = None):
        self.val = val
        self.neighbors = list(neighbors) if neighbors is not None else []


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
    module.GraphNode = GraphNode
    module.Node = GraphNode
    spec.loader.exec_module(module)
    return module


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def build_list_array(values: list[list[int]]) -> list[ListNode | None]:
    if not isinstance(values, list) or any(
        not isinstance(row, list) or any(type(value) is not int for value in row) for row in values
    ):
        raise ValueError("List-node arrays require an outer array of integer arrays")
    return [build_list(row) for row in values]


def build_list_cycle(value: dict[str, Any]) -> ListNode | None:
    """Build the platform's cyclic-list fixture without losing node identities."""
    if not isinstance(value, dict) or set(value) != {"values", "pos"}:
        raise ValueError("Cyclic-list input requires values and pos only")
    values, position = value["values"], value["pos"]
    if not isinstance(values, list) or any(type(item) is not int for item in values):
        raise ValueError("Cyclic-list values must be an integer array")
    if type(position) is not int or not (-1 <= position < len(values)):
        raise ValueError("Cyclic-list pos must be -1 or a valid node index")
    nodes = [ListNode(item) for item in values]
    for first, second in zip(nodes[:-1], nodes[1:], strict=True):
        first.next = second
    if nodes and position >= 0:
        nodes[-1].next = nodes[position]
    return nodes[0] if nodes else None


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


def _tree_nodes(root: TreeNode | None) -> list[TreeNode]:
    nodes = []
    seen: set[int] = set()
    pending = [root] if root is not None else []
    while pending:
        node = pending.pop()
        if not isinstance(node, TreeNode) or type(node.val) is not int:
            raise ValueError("Tree references require integer-valued platform nodes")
        if id(node) in seen:
            raise ValueError("Tree references cannot use a cycle or shared child")
        seen.add(id(node))
        nodes.append(node)
        for child in (node.left, node.right):
            if child is not None:
                pending.append(child)
    return nodes


def resolve_tree_ref(root: TreeNode | None, value: int) -> TreeNode:
    """Resolve a fixture value to the unique existing node in the original tree."""
    if type(value) is not int:
        raise ValueError("Tree reference values must be integers")
    matches = [node for node in _tree_nodes(root) if node.val == value]
    if len(matches) != 1:
        raise ValueError("Tree reference must identify exactly one existing node")
    return matches[0]


def build_graph(adjacency: list[list[int]]) -> GraphNode | None:
    """Decode 1-based adjacency labels; graph cycles are ordinary edges."""
    if not isinstance(adjacency, list) or any(not isinstance(row, list) for row in adjacency):
        raise ValueError("Graph adjacency must be an array of neighbor arrays")
    count = len(adjacency)
    if any(type(label) is not int or not 1 <= label <= count for row in adjacency for label in row):
        raise ValueError("Graph neighbor labels must be integers in 1..n")
    nodes = [GraphNode(index + 1) for index in range(count)]
    for node, labels in zip(nodes, adjacency, strict=True):
        node.neighbors = [nodes[label - 1] for label in labels]
    return nodes[0] if nodes else None


def graph_to_json(root: GraphNode | None) -> list[list[int]]:
    """Serialize root-reachable nodes by label, preserving edge multiplicity."""
    if root is None:
        return []
    nodes: dict[int, GraphNode] = {}
    seen: set[int] = set()
    pending = deque([root])
    while pending:
        node = pending.popleft()
        if not isinstance(node, GraphNode):
            raise ValueError("Graph neighbors must be graph nodes")
        if id(node) in seen:
            continue
        seen.add(id(node))
        if type(node.val) is not int or node.val < 1:
            raise ValueError("Graph node labels must be positive integers")
        if node.val in nodes:
            raise ValueError("Distinct graph nodes cannot share a label")
        if not isinstance(node.neighbors, list):
            raise ValueError("Graph neighbors must be a list")
        nodes[node.val] = node
        pending.extend(node.neighbors)
    result: list[list[int]] = [[] for _ in range(max(nodes))]
    for label, node in nodes.items():
        result[label - 1] = sorted(neighbor.val for neighbor in node.neighbors)
    return result


def _adapt(value: Any, kind: str) -> Any:
    if kind == "value":
        return value
    if kind == "listnode":
        return build_list(value)
    if kind == "listnode_array":
        return build_list_array(value)
    if kind == "listnode_cycle":
        return build_list_cycle(value)
    if kind == "treenode":
        return build_tree(value)
    if kind == "graphnode":
        return build_graph(value)
    raise ValueError(f"Unknown argument type: {kind}")


def _serialize(
    value: Any, kind: str, original_tree_nodes: dict[TreeNode, int] | None = None
) -> Any:
    if kind == "value":
        return value
    if kind == "listnode":
        return list_to_json(value)
    if kind == "treenode":
        return tree_to_json(value)
    if kind == "tree_ref":
        if value is None:
            return None
        if (
            not isinstance(value, TreeNode)
            or original_tree_nodes is None
            or value not in original_tree_nodes
        ):
            raise ValueError("Returned tree reference must belong to the original tree")
        original_value = original_tree_nodes[value]
        if type(value.val) is not int or value.val != original_value:
            raise ValueError("Returned tree reference changed its original value")
        return original_value
    if kind == "graphnode":
        return graph_to_json(value)
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
        adapted = []
        for value, kind in zip(deepcopy(args), kinds, strict=True):
            if kind == "tree_ref":
                if not adapted or kinds[0] != "treenode":
                    raise ValueError("Tree reference arguments require an original tree first")
                adapted.append(resolve_tree_ref(adapted[0], value))
            else:
                adapted.append(_adapt(value, kind))
        original_tree_nodes = None
        if meta["return_type"] == "tree_ref":
            if not kinds or kinds[0] != "treenode":
                raise ValueError("Tree reference results require an original tree first")
            original_tree_nodes = {node: node.val for node in _tree_nodes(adapted[0])}
        method = getattr(module.Solution(), meta["method"])
        result = method(*adapted)
        if "result_from_arg" in meta:
            index = meta["result_from_arg"]
            if type(index) is not int or not 0 <= index < len(adapted):
                raise ValueError("In-place result index does not match arguments")
            result = adapted[index]
        return _serialize(result, meta["return_type"], original_tree_nodes)
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
    if checker == "graph_adjacency":
        if any(not isinstance(row, list) for row in result) or any(
            type(label) is not int or not 1 <= label <= len(result)
            for row in result
            for label in row
        ):
            raise ValueError("graph_adjacency checker requires 1-based integer neighbor rows")
        return [sorted(row) for row in result]
    raise ValueError(f"Unknown checker: {checker}")


def _finite_number(value: Any) -> bool:
    if type(value) not in {int, float}:
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def _numeric_list_tolerance(meta: dict[str, Any]) -> tuple[float, float]:
    policy = meta.get("numeric_tolerance", {"relative": 1e-9, "absolute": 1e-12})
    if (
        not isinstance(policy, dict)
        or set(policy) != {"relative", "absolute"}
        or any(not _finite_number(value) or value < 0 for value in policy.values())
    ):
        raise ValueError(
            "Numeric tolerance requires finite nonnegative relative and absolute values"
        )
    return float(policy["relative"]), float(policy["absolute"])


def check_result(
    meta: dict[str, Any], actual: Any, expected: Any, args: list[Any] | None = None
) -> bool:
    """Compare JSON values with explicit ordering rules and scalar types."""
    checker = meta.get("checker", "exact")
    if checker == "approx_list":
        relative, absolute = _numeric_list_tolerance(meta)
        return (
            isinstance(actual, list)
            and isinstance(expected, list)
            and len(actual) == len(expected)
            and all(
                _finite_number(found)
                and _finite_number(reference)
                and math.isclose(found, reference, rel_tol=relative, abs_tol=absolute)
                for found, reference in zip(actual, expected, strict=True)
            )
        )
    if checker == "peak_index":
        if (
            args is None
            or len(args) != 1
            or not isinstance(args[0], list)
            or not args[0]
            or any(type(value) is not int for value in args[0])
        ):
            raise ValueError("Peak checker requires the original nonempty integer array")
        nums = args[0]
        return (
            type(actual) is int
            and 0 <= actual < len(nums)
            and (actual == 0 or nums[actual] > nums[actual - 1])
            and (actual == len(nums) - 1 or nums[actual] > nums[actual + 1])
        )
    if checker in {"balanced_bst", "bst_inorder"}:
        if checker == "balanced_bst":
            if args is None or len(args) != 1 or not isinstance(args[0], list):
                raise ValueError("Balanced-BST checker requires the original sorted array")
            wanted = args[0]
        else:
            wanted = expected
        if (
            not isinstance(wanted, list)
            or any(type(value) is not int for value in wanted)
            or any(first >= second for first, second in zip(wanted[:-1], wanted[1:], strict=True))
        ):
            raise ValueError("BST reference requires sorted unique integer values")
        if not isinstance(actual, list) or any(
            value is not None and type(value) is not int for value in actual
        ):
            return False
        try:
            root = build_tree(actual)
            nodes = _tree_nodes(root)
        except ValueError:
            return False
        inorder = []
        stack = []
        current = root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            inorder.append(current.val)
            current = current.right
        if inorder != wanted:
            return False
        if checker == "bst_inorder":
            return True
        heights: dict[TreeNode, int] = {}
        for node in reversed(nodes):
            left, right = heights.get(node.left, 0), heights.get(node.right, 0)
            if abs(left - right) > 1:
                return False
            heights[node] = 1 + max(left, right)
        return True
    if checker == "approx":
        return (
            _finite_number(actual)
            and _finite_number(expected)
            and math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-12)
        )
    if checker == "longest_palindrome":
        if args is None or len(args) != 1 or not isinstance(args[0], str):
            raise ValueError("Longest-palindrome checker requires the original string")
        if isinstance(expected, str):
            maximum_length = len(expected)
        elif type(expected) is int and expected >= 0:
            maximum_length = expected
        else:
            raise ValueError("Longest-palindrome reference must be a substring or length")
        return (
            isinstance(actual, str)
            and actual in args[0]
            and actual == actual[::-1]
            and len(actual) == maximum_length
        )
    if checker == "gas_station":
        if (
            args is None
            or len(args) != 2
            or any(not isinstance(values, list) for values in args)
            or not args[0]
            or len(args[0]) != len(args[1])
            or any(type(value) is not int or value < 0 for values in args for value in values)
        ):
            raise ValueError("Gas-station checker requires equal nonempty gas and cost arrays")
        if type(expected) is not int or not -1 <= expected < len(args[0]):
            raise ValueError("Gas-station reference must be -1 or a station index")
        if type(actual) is not int:
            return False
        gas, cost = args
        if expected == -1:
            return actual == -1 and sum(gas) < sum(cost)
        if not 0 <= actual < len(gas):
            return False
        fuel = 0
        for offset in range(len(gas)):
            station = (actual + offset) % len(gas)
            fuel += gas[station] - cost[station]
            if fuel < 0:
                return False
        return True
    if meta.get("checker") == "topological_order":
        if args is None or len(args) != 2:
            raise ValueError("Topological checker requires course count and prerequisites")
        if expected == []:
            return _json_key(actual) == "[]"
        count, prerequisites = args
        if (
            not isinstance(actual, list)
            or len(actual) != count
            or any(type(course) is not int for course in actual)
            or set(actual) != set(range(count))
        ):
            return False
        positions = {course: index for index, course in enumerate(actual)}
        return all(positions[before] < positions[after] for after, before in prerequisites)
    return _json_key(normalize(meta, actual)) == _json_key(normalize(meta, expected))
