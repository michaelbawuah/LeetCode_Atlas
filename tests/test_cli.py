"""Exercise the user commands, including sparse-node and design fixtures."""

import json
import subprocess
import sys


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "atlas", *args], text=True, capture_output=True, check=False
    )


def test_browse_by_pattern_and_difficulty():
    result = run_cli("list", "--pattern", "binary-search", "--difficulty", "Medium")
    assert result.returncode == 0
    assert "Search in Rotated Sorted Array" in result.stdout
    assert "Binary Search  | Easy" not in result.stdout


def test_run_custom_arguments():
    result = run_cli("run", "1", "--args", "[[2,7,11,15],9]")
    assert result.returncode == 0
    assert json.loads(result.stdout) == [0, 1]


def test_run_stateful_fixture_and_unknown_id():
    result = run_cli("run", "155")
    assert result.returncode == 0
    assert json.loads(result.stdout)["passed"] is True
    missing = run_cli("run", "999999")
    assert missing.returncode != 0
    assert "Unknown problem" in missing.stderr
