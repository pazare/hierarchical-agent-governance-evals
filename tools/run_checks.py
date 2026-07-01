#!/usr/bin/env python3
"""Offline verification suite for the curated public release.

STDLIB ONLY. No API keys, no network, no third-party dependencies, and the
working tree stays clean (bytecode is compiled to a temp dir; nothing is
written into the repository).

This is the release counterpart of the research repo's full-workspace
`tools/run_checks.py`: it verifies what this curated release actually ships —
it does not (and honestly cannot) re-run the live experiments. What it checks:

  1. every shipped Python file compiles;
  2. the confidence-bounds library self-test passes (code/ci.py);
  3. the figure generator's data report verifies against anchored bounds
     (paper/figures/make_confidence_forest.py --check);
  4. every file the release manifest promises is present;
  5. held-back / private material is structurally absent;
  6. every relative link in README.md resolves;
  7. LICENSE / CITATION / README metadata are coherent.

Run from a bare clone:  python3 tools/run_checks.py
(Staged in the research repo under publication_prep/public_release/tools/;
it runs against the release tree layout, i.e. after export.)
"""

from __future__ import annotations

import os
import py_compile
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable

REQUIRED_FILES = [
    ".gitattributes",
    ".gitignore",
    "AI_USAGE.md",
    "CITATION.cff",
    "DISCLOSURE.md",
    "FRAMEWORK_authority_calibration.md",
    "LICENSE",
    "MANIFEST.md",
    "README.md",
    "code/ci.py",
    "docs/ethics_and_release.md",
    "paper/figures/confidence_forest.pdf",
    "paper/figures/confidence_forest.png",
    "paper/figures/make_confidence_forest.py",
    "paper/submission_compact.pdf",
    "paper/submission_compact.tex",
    "tools/check_program.py",
    "tools/run_checks.py",
]

# Material the release manifest explicitly holds back. Its absence is a check,
# so a future re-export cannot silently sweep it in.
HELD_BACK_PATHS = [
    "docs/private",
    "docs/DESIGN_least_character_redteam.md",
    "experiments",
    "evidence",
    "bibliography",
    "scenarios",
    "results",
    "transcripts",
    "prompts",
    "scoring",
    "configs",
    "analysis",
    "legacy",
    "publication_prep",
    "registration_packets",
    "paper/zavala_authority_calibration_book.tex",
    "paper/zavala_authority_calibration_book.pdf",
    "paper/submission_compact_holdsafe.tex",
    "paper/submission_compact_holdsafe_anon.tex",
]


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str


def run_command(name: str, args: list[str], *, must_contain: list[str]) -> CheckResult:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    proc = subprocess.run(
        [PYTHON, "-B", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        env=env,
    )
    output = proc.stdout + proc.stderr
    missing = [needle for needle in must_contain if needle not in output]
    ok = proc.returncode == 0 and not missing
    if ok:
        detail = "ok"
    elif proc.returncode != 0:
        detail = f"exit {proc.returncode}"
    else:
        detail = "missing expected text: " + ", ".join(missing)
    if not ok:
        print(f"\n--- {name} output ---")
        print(output.rstrip())
    return CheckResult(name, ok, detail)


def compile_python() -> CheckResult:
    """Byte-compile every shipped .py file into a temp dir (tree stays clean)."""
    failures = []
    count = 0
    with tempfile.TemporaryDirectory() as tmp:
        for path in sorted(ROOT.rglob("*.py")):
            if ".git" in path.parts:
                continue
            count += 1
            target = Path(tmp) / f"{count}_{path.name}c"
            try:
                py_compile.compile(str(path), cfile=str(target), doraise=True)
            except py_compile.PyCompileError as exc:
                failures.append(f"{path.relative_to(ROOT)}: {exc.msg.splitlines()[0]}")
    if failures:
        return CheckResult("compile Python files", False, "; ".join(failures[:3]))
    return CheckResult("compile Python files", True, f"ok ({count} files)")


def required_files_check() -> CheckResult:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).is_file()]
    if missing:
        return CheckResult("release files present", False, "missing: " + ", ".join(missing[:5]))
    return CheckResult("release files present", True, f"ok ({len(REQUIRED_FILES)} files)")


def held_back_absent_check() -> CheckResult:
    present = [rel for rel in HELD_BACK_PATHS if (ROOT / rel).exists()]
    if present:
        return CheckResult("held-back material absent", False, "present: " + ", ".join(present[:5]))
    return CheckResult("held-back material absent", True, f"ok ({len(HELD_BACK_PATHS)} paths checked)")


def readme_links_check() -> CheckResult:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    broken = []
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        rel = target.split("#", 1)[0]
        if rel and not (ROOT / rel).exists():
            broken.append(rel)
    if broken:
        return CheckResult("README relative links resolve", False, "broken: " + ", ".join(sorted(set(broken))[:5]))
    return CheckResult("README relative links resolve", True, "ok")


def metadata_check() -> CheckResult:
    problems = []
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if "MIT License" not in license_text:
        problems.append("LICENSE is not MIT")
    if "Pablo Zavala" not in license_text:
        problems.append("LICENSE does not name the copyright holder")
    if "Zavala" not in (ROOT / "CITATION.cff").read_text(encoding="utf-8"):
        problems.append("CITATION.cff missing author")
    if "Reproduce in three commands" not in (ROOT / "README.md").read_text(encoding="utf-8"):
        problems.append("README missing the reproduce block")
    if problems:
        return CheckResult("license/citation/readme metadata", False, "; ".join(problems))
    return CheckResult("license/citation/readme metadata", True, "ok")


def build_checks() -> list[CheckResult]:
    return [
        compile_python(),
        run_command(
            "confidence-bounds self-test (code/ci.py)",
            ["code/ci.py"],
            must_contain=["PASS", "0.0758"],
        ),
        run_command(
            "confidence-forest data report (--check)",
            ["paper/figures/make_confidence_forest.py", "--check"],
            must_contain=["--check PASS", "6/19", "Wilson 95%", "no files written"],
        ),
        required_files_check(),
        held_back_absent_check(),
        readme_links_check(),
        metadata_check(),
    ]


def main() -> int:
    results = build_checks()
    print("# Release checks")
    print()
    print("| check | result | detail |")
    print("|---|---|---|")
    for r in results:
        print(f"| {r.name} | **{'PASS' if r.ok else 'FAIL'}** | {r.detail} |")
    print()
    passed = sum(1 for r in results if r.ok)
    print(f"Checks passed: {passed}/{len(results)}")
    print("Overall: PASS" if passed == len(results) else "Overall: FAIL")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
