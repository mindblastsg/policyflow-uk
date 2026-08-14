import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).parents[1]


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_synthetic_flow_fixture_validates_against_v01_schemas() -> None:
    fixture = _load(
        ROOT / "data" / "examples" / "synthetic-financial-policy-flow" / "example.json"
    )
    flow_schema = _load(ROOT / "schemas" / "flow.schema.json")
    event_schema = _load(ROOT / "schemas" / "event.schema.json")

    Draft202012Validator.check_schema(flow_schema)
    Draft202012Validator.check_schema(event_schema)

    Draft202012Validator(flow_schema).validate(fixture["flow"])
    for event in fixture["events"]:
        Draft202012Validator(event_schema).validate(event)
