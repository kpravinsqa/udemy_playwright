import csv
import json
from pathlib import Path
from typing import Any

import pytest


PROJECT_ROOT = Path(__file__).resolve().parent


@pytest.fixture(scope="session")
def project_root() -> Path:
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def test_data_dir(project_root: Path) -> Path:
    return project_root / "test data"


@pytest.fixture(scope="session")
def json_test_data(test_data_dir: Path) -> Any:
    with (test_data_dir / "testdata.json").open(encoding="utf-8") as data_file:
        return json.load(data_file)


@pytest.fixture(scope="session")
def csv_test_data(test_data_dir: Path) -> list[dict[str, str | None]]:
    with (test_data_dir / "testdata.csv").open(
        encoding="utf-8-sig", newline=""
    ) as data_file:
        return list(csv.DictReader(data_file))


@pytest.fixture(scope="session")
def browser_context_args(
    browser_context_args: dict[str, Any],
) -> dict[str, Any]:
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture(
    scope="session",
    params=["chrome", "msedge"],
    ids=["chrome", "edge"],
)
def browser_type_launch_args(request: pytest.FixtureRequest) -> dict[str, str]:
    return {"channel": request.param, "headless": False}