"""Browse problems and run a solution on a fixture or your own JSON input."""

import argparse
import json

from atlas.runtime import check_result, evaluate, metadata, problem_dirs


def find_problem(value):
    matches = [
        folder
        for folder in problem_dirs()
        if str(metadata(folder)["id"]) == value or folder.name == value
    ]
    if not matches:
        raise ValueError(f"Unknown problem: {value}. Use `python -m atlas list`.")
    return matches[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    listing = sub.add_parser("list", help="Browse implemented problems")
    listing.add_argument("--pattern")
    listing.add_argument("--difficulty", choices=["Easy", "Medium", "Hard"])
    run = sub.add_parser("run", help="Run a Python solution locally")
    run.add_argument("problem", help="Numeric ID or padded folder name")
    choice = run.add_mutually_exclusive_group()
    choice.add_argument("--args", help="JSON array of method arguments")
    choice.add_argument("--case", type=int, default=0, help="Zero-based shared fixture index")
    args = parser.parse_args()
    if args.command == "list":
        for folder in problem_dirs():
            meta = metadata(folder)
            if args.pattern and args.pattern not in meta["patterns"]:
                continue
            if args.difficulty and args.difficulty != meta["difficulty"]:
                continue
            languages = "Python + C++23" if (folder / "solution.cpp").exists() else "Python"
            print(f"{meta['id']:>4}  {meta['title']}  | {meta['difficulty']} | {languages}")
        return 0
    try:
        folder = find_problem(args.problem)
        meta = metadata(folder)
        if args.args is not None:
            actual = evaluate(folder, args=json.loads(args.args))
            print(json.dumps(actual))
            return 0
        cases = json.loads((folder / "cases.json").read_text())
        if not 0 <= args.case < len(cases):
            raise ValueError(f"Fixture index must be between 0 and {len(cases) - 1}")
        case = cases[args.case]
        inputs = {key: case[key] for key in ("args", "operations", "arguments") if key in case}
        actual = evaluate(folder, **inputs)
        passed = check_result(meta, actual, case["expected"])
        print(json.dumps({"case": case["name"], "result": actual, "passed": passed}))
        return 0 if passed else 1
    except (ValueError, TypeError, KeyError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    raise SystemExit(main())
