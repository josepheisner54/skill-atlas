import pytest

from skill_atlas.cli.main import run


def test_cli_runs(capsys: pytest.CaptureFixture[str]) -> None:
    run(["--nodes", "2"])
    captured = capsys.readouterr()
    assert "generated graph with 2 nodes" in captured.out
