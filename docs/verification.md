# Verification

[CI workflow](https://github.com/michaelbawuah/LeetCode_Atlas/actions/workflows/ci.yml) · [Problem catalog](problems.md) · [Repository](../README.md)

The repository checks problems from several directions: named cases, independently computed results on generated inputs, structural properties, and shared Python/C++ fixtures. These checks have separate purposes and separate evidence.

## Milestone records

The historical [foundation record](../verification/foundation.json) covers **25 Python problems and 10 C++23 counterparts**: 255 pytest tests passed, including 180 named fixtures and 1,500 generated Python/C++ comparisons, plus the CTest adapter suite. AddressSanitizer and UndefinedBehaviorSanitizer were enabled. LeakSanitizer was disabled locally because the container runs under ptrace; the Linux Clang CI configuration enables it.

The [75-problem milestone report](../verification/milestone75.json) records **75 Python implementations and 25 C++23 counterparts**, with 720 pytest checks and 3,750 generated comparisons. The separate [150-problem report](../verification/milestone150.json) covers **150 Python implementations and 75 C++23 counterparts**: 1,456 pytest checks passed, including 1,106 named fixtures and **11,250 generated comparisons: 150 for each counterpart**. The CTest adapter suite also passed. Earlier totals remain historical records.

The [300-problem report](../verification/milestone300.json) records the main target: **300 Python implementations and 150 C++23 counterparts**, including **22,500 generated comparison cases**. All 2,598 pytest checks passed, with 1,975 named fixtures and the 66-assertion CTest adapter suite. Its command outcomes, focused follow-up, and source digest identify the verified milestone.

The [C++ expansion report](../verification/cpp225.json) records **300 Python implementations and 225 C++23 counterparts**, including **33,750 generated comparison cases**. All **2,690 pytest checks** passed without skips, covering 1,986 named Python fixtures, 1,510 shared C++ fixtures, and six persistent C++ stress checks. The sanitizer adapter suite passed 20 cases with 129 assertions. Earlier milestone records remain intact; the expansion report identifies its source digest and command outcomes.

## Run the Python checks

From the repository root, with Python 3.11 or newer:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest
python tools/catalog.py --check
```

On Windows, use the virtual environment activation script for your shell. To run one problem's generated checks:

```bash
python -m pytest problems/0143-reorder-list
```

## What each check answers

| Check | Evidence it provides | Its limit |
|---|---|---|
| Named fixtures | Examples, boundaries, and known failure cases produce the expected result. | A finite list does not cover every input. |
| Independent generated-input oracle | An optimized result agrees with a simpler calculation over bounded generated inputs. | Generated domains remain small enough for the oracle to run. |
| Structural properties | Outputs obey node identity, shape, valid-index, and cycle constraints. | A structural property alone may not establish the numerical answer. |
| Python/C++ shared fixtures and generated inputs | Both implementations satisfy the same checker or witness conditions. | The implementations can share an algorithmic mistake. |
| Catalog checks | Metadata and generated navigation stay synchronized. | Metadata is not a correctness proof. |
| Compiler and sanitizer checks | Tested C++ paths compile and receive memory/undefined-behavior instrumentation. | Instrumentation does not establish correctness on all inputs. |

Examples of independent checks include [House Robber](../problems/0198-house-robber/test_properties.py)'s enumeration of legal subsets, [Number of Islands](../problems/0200-number-of-islands/test_properties.py)'s disjoint-set reference, and [Right Side View](../problems/0199-binary-tree-right-side-view/test_properties.py)'s BFS oracle for a DFS implementation. [Reorder List](../problems/0143-reorder-list/test_properties.py) also checks that the exact existing nodes appear once in the required order.

Hypothesis generates and shrinks counterexamples when a property fails. A useful failure should become a named regression fixture when it demonstrates a boundary or mistake worth retaining.

## Shared fixtures and semantic checkers

`cases.json` stores inputs and expected results. Method problems use argument arrays; design problems store legal constructor and operation histories. Runtime adapters construct list/tree/graph nodes, isolate calls by copying JSON inputs, and serialize outputs. C++ design runners accept `[operations, arguments]` and return one result for every operation, including `null` for construction and void methods.

[Reorder List](../problems/0143-reorder-list/meta.json) and [Move Zeroes](../problems/0283-move-zeroes/meta.json) retain their in-place, `None`-returning submission methods. Metadata `result_from_arg: 0` asks the local runner to compare the changed first argument instead of that return value. Input isolation protects fixtures while still exposing the actual mutation result.

| Checker | Permitted difference |
|---|---|
| `exact` | No value, scalar-type, or ordering differences. |
| `unordered` | Flat item order may vary; duplicate counts still matter. |
| `unordered_rows` | Outer row order may vary; positions within each row remain meaningful. |
| `unordered_groups` | Group order and flat member order may vary; multiplicity remains meaningful. |
| `topological_order` | Any complete, duplicate-free course ordering respecting every prerequisite is valid. A cyclic fixture requires an empty result. |
| `longest_palindrome` | Any source substring that is a palindrome with the expected maximum length. |
| `gas_station` | Any returned index completing the full circuit; `-1` requires total gas below total cost. |
| `graph_adjacency` | Neighbor order within each labeled node may vary; node labels, edges, and multiplicity remain meaningful. |
| `approx` | Numeric results may differ within relative tolerance 1e-9 and absolute tolerance 1e-12; booleans are rejected. |
| `approx_list` | Each finite numeric element follows its declared `numeric_tolerance`, or the default scalar tolerance; length and order remain meaningful. |
| `peak_index` | Any in-range index strictly above its existing neighbors is valid. |
| `balanced_bst` | Any height-balanced strict BST containing the original sorted input values in inorder is valid. |
| `bst_inorder` | Any strict BST whose inorder values equal the expected values is valid. |

[Course Schedule II](../problems/0210-course-schedule-ii/README.md) uses the semantic topological checker with its original course count and edges. Comparing it to one expected ordering would reject other correct witnesses; sorting the result would erase the dependency evidence.

Named fixtures honor the official input contracts, including unique-answer conditions. Generated Two Sum inputs deliberately allow several valid pairs and check index bounds, distinctness, and the target sum. Generated Minimum Window inputs deliberately allow tied shortest windows and check returned length and character coverage. These extensions test valid witnesses rather than requiring one incidental choice. Reverse Bits also has a separately labeled robustness property over the full unsigned 32-bit domain. Each problem's notes identify any broader test domain.

Average of Levels uses absolute tolerance 1e-5 with zero relative tolerance. Evaluate Division uses relative and absolute tolerances 1e-5. These explicit local comparison policies are separate from recorded official judge evidence.

## Node representation and ownership

Sparse trees use LeetCode's queue-based level order with null children, not heap-array positions. `[1,null,2,3]` places 3 below the right child 2. List serialization detects cycles, and tree serialization rejects cycles or shared children.

Linked List Cycle accepts `{"values": [3,2,0,-4], "pos": 1}`: `pos` identifies the node to which the final link returns, or is `-1` for an acyclic list. Graph fixtures use adjacency rows for labels 1 through n. Graph-clone properties inspect pointer identity separately from serialized adjacency so returning the original graph cannot pass on values alone.

The C++ [adapter arenas](../cpp/atlas_adapter.hpp) retain ownership of every allocated node, including nodes detached from a returned list. Submission methods borrow pointers and can rewire links without assuming responsibility for deleting those nodes. Adapter tests cover decoding, serialization, and lifetime-sensitive behavior.

Newly constructed tree outputs use `TreeResultOwner` rather than an input arena. The construction submission stages allocations for exception safety; the local owner releases the returned tree after serialization. This ownership path is tested independently of tree values.

List-array fixtures build each list independently. Tree-reference fixtures resolve integer query values inside a single original tree and require returned references to belong to it. The C++ reference adapter snapshots the original labels and links, rejecting copied output nodes and mutations to the query tree. Its cycle-list builder retains ownership independently of cyclic links. C++ fresh-list results use `ListResultOwner`; borrowed lists remain owned by their input arena. Negative adapter regressions check incorrect references, malformed witnesses, and invalid numeric values.

## Run the C++23 checks

Install CMake 3.24 or newer and a C++23-capable compiler. The first configuration fetches pinned nlohmann JSON and Catch2 dependencies when matching versions are not installed:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --parallel
ctest --test-dir build --output-on-failure
ATLAS_CPP_BIN_DIR=build/bin python -m pytest tests/test_cases.py tests/test_cpp_properties.py
```

`ATLAS_CPP_BIN_DIR` selects the compiled runners. Shared-fixture checks require the configured counterpart set, and generated coverage checks require a strategy for every C++ implementation. Missing runners and incorrect JSON output lengths fail the checks.

For AddressSanitizer and UndefinedBehaviorSanitizer with GCC or Clang, use a separate build:

```bash
cmake -S . -B build-sanitized -DCMAKE_BUILD_TYPE=Debug -DATLAS_SANITIZERS=ON
cmake --build build-sanitized --parallel
ctest --test-dir build-sanitized --output-on-failure
ATLAS_CPP_BIN_DIR=build-sanitized/bin python -m pytest tests/test_cases.py tests/test_cpp_properties.py
```

If a container's ptrace environment prevents LeakSanitizer from starting, run its local commands with `ASAN_OPTIONS=detect_leaks=0` and record that limitation. The maintained Linux Clang CI configuration enables leak detection. A configured workflow is distinct from an observed successful run.

## Complexity review

Read time/space bounds alongside the invariant. Review hidden costs such as copied slices, sorting, signature construction, retained traversal state, and output storage. Qualify expected hash-table costs and amortized stack operations. Python and C++ can use different algorithms; Kth Largest's heap and partition implementations illustrate why one language's metadata cannot imply the other's bound.

The notes describe algorithmic bounds. Recorded command results establish the verification performed for a particular milestone.

## Local verification and official judge results

The badge links to the actual workflow status. Use the workflow's run details to check its commit and observed result.

Official LeetCode submission results are a separate metadata field. Current entries use `judge_status: "not_recorded"`. Local passes do not change that field; a recorded official result needs dated submission evidence.
