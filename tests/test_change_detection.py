from policyflow.change_detection import classify_change, content_hash, normalise_text
from policyflow.models import ChangeStatus


def test_normalisation_is_conservative_and_deterministic() -> None:
    assert normalise_text("  Alpha\t beta  \r\nGamma  ") == " Alpha beta\nGamma"


def test_hash_ignores_line_ending_and_horizontal_whitespace_noise() -> None:
    assert content_hash("Alpha  beta\r\nGamma") == content_hash("Alpha beta\nGamma")


def test_change_classification() -> None:
    current = content_hash("current")
    assert classify_change(None, current) is ChangeStatus.NEW
    assert classify_change(current, current) is ChangeStatus.UNCHANGED
    assert classify_change(content_hash("old"), current) is ChangeStatus.CHANGED
