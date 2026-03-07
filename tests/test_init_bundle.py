import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "init_bundle.py"


def test_init_bundle_creates_files(tmp_path):
    out_dir = tmp_path / "bundle"
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--out",
            str(out_dir),
            "--project-name",
            "Live2Reels",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert (out_dir / "prd.md").exists()
    assert (out_dir / "contracts.md").exists()
    assert (out_dir / "schema.sql").exists()
    assert (out_dir / "test-plan.md").exists()
    assert (out_dir / "epics.md").exists()
    assert "project_slug: live2reels" in result.stdout
    assert "# Live2Reels" in (out_dir / "prd.md").read_text(encoding="utf-8")


def test_init_bundle_skips_existing_without_force(tmp_path):
    out_dir = tmp_path / "bundle"
    out_dir.mkdir(parents=True)
    target = out_dir / "prd.md"
    target.write_text("keep me", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--out",
            str(out_dir),
            "--project-name",
            "SpecKit",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert target.read_text(encoding="utf-8") == "keep me"
    assert "skipped: prd.md" in result.stdout
