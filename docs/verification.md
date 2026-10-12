# Verification

[CI workflow](https://github.com/michaelbawuah/LeetCode_Atlas/actions/workflows/ci.yml) · [Problem catalog](problems.md) · [Repository](../README.md)

The repository checks each problem from several directions: readable named cases, independently computed results on generated inputs, structural properties, and shared fixtures for Python/C++ counterparts.

The [foundation verification record](../verification/foundation.json) contains the local environment, commands, and results: **255 pytest tests passed**, including **180 named fixtures** and **1,500 generated Python/C++ comparisons**, plus the CTest adapter suite. AddressSanitizer and UndefinedBehaviorSanitizer were enabled. LeakSanitizer was disabled locally because the test container runs under ptrace; Linux Clang CI enables it.

## Run the Python checks

From the repository root, with Python 3.11 or newer:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest
python tools/catalog.py --check
```

On Windows, activate the virtual environment with the activation script appropriate to your shell. The remaining Python commands are the same.

To run one problem's generated checks, point pytest at its folder:

```bash
python -m pytest problems/0424-longest-repeating-character-replacement
```

## What each check answers

| Check | Evidence it provides | Its limit |
|---|---|---|
| Named fixtures | Examples, boundaries, and known failure cases produce the expected result. | A finite case list does not cover every input. |
| Independent generated-input oracle | The optimized result agrees with a simpler calculation over many bounded inputs. | Generated domains are deliberately small enough for the oracle to run. |
| Structural properties | Outputs obey constraints such as list shape, valid indexes, or absence of cycles. | A structural property alone may not prove the numerical answer. |
| Python/C++ shared fixtures | Both implementations satisfy the same problem-specific checker. | Shared algorithm mistakes can survive language agreement. |
| Catalog checks | Structured metadata and generated navigation stay synchronized. | Metadata is not a correctness proof. |
| Compiler and sanitizer checks | Tested C++ paths compile and are checked for selected memory and undefined-behavior errors. | They do not establish algorithmic correctness on all inputs. |

For example, [stock profit](../problems/0121-best-time-to-buy-and-sell-stock/test_properties.py) is compared with every legal buy/sell pair on small generated price lists. [Character replacement](../problems/0424-longest-repeating-character-replacement/test_properties.py) is compared with enumerated substrings, and [Min Stack](../problems/0155-min-stack/test_properties.py) is compared with a plain list and direct minimum queries.

Hypothesis generates and shrinks counterexamples when a property fails. A small failing example should become a named regression case when it demonstrates a useful boundary or failure mode.

## Shared fixtures and checkers

`cases.json` stores the inputs and expected results. Method-style problems use argument lists; design problems store legal operation sequences. Adapters construct linked lists or trees for interfaces that need node objects.

The checker is part of `meta.json`. Exact-output problems compare values directly. Order-insensitive outputs use the declared comparison so permitted reorderings are accepted. Generated oracles can additionally validate a result's semantics directly. Compare the meaning of a result without sorting away a distinction the problem requires.

Generated tests largely follow the official input contract. Min Stack's `pop`, `top`, and `getMin` are only called while nonempty, and rotated-array search receives distinct values. Two Sum's generators additionally permit multiple valid pairs to check that any returned pair is valid; named fixtures retain the problem's unique-pair contract.

## Run the C++23 checks

Install CMake 3.24 or newer and a C++23-capable compiler. The first configuration fetches pinned nlohmann JSON and Catch2 dependencies when matching versions are not already installed. Then build the adapters and run the configured CTest suite:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --parallel
ctest --test-dir build --output-on-failure
ATLAS_CPP_BIN_DIR=build/bin python -m pytest tests/test_cases.py
ATLAS_CPP_BIN_DIR=build/bin python -m pytest tests/test_cpp_properties.py
```

`ATLAS_CPP_BIN_DIR` tells the fixture runner where to find compiled counterparts. Use the directory matching your current build configuration.

For AddressSanitizer and UndefinedBehaviorSanitizer with a supported GCC or Clang toolchain, configure a separate build:

```bash
cmake -S . -B build-sanitized -DCMAKE_BUILD_TYPE=Debug -DATLAS_SANITIZERS=ON
cmake --build build-sanitized --parallel
ctest --test-dir build-sanitized --output-on-failure
ATLAS_CPP_BIN_DIR=build-sanitized/bin python -m pytest tests/test_cases.py tests/test_cpp_properties.py
```

Keeping instrumented and ordinary binaries in different directories makes the selected test path explicit. The CI workflow contains the maintained compiler configuration.

## Complexity review

Each problem explains its time and space cost alongside the invariant. Review hidden costs such as copied slices, sorting, hash-signature construction, recursion depth, and output storage. Qualify expected hash-table costs and amortized stack operations where appropriate.

The complexity notes describe algorithmic bounds; this foundation does not publish performance benchmark rankings.

## Local verification and judge results

The CI badge links to the actual workflow's status. Its current result belongs to the workflow, rather than a manually maintained success claim in this document.

Official LeetCode submission results are a separate metadata field. Current entries use `judge_status: "not_recorded"`. A local test pass does not change that field; a recorded official result should have submission evidence and a date.
