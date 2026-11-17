import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.simulate_raw_data import simulate
from src.adam_pipeline import derive_adam, validate_derivation, generate_tlfs
from src.sample_size_calculator import TEMPLATES, find_required_n


def test_at_least_800_subjects():
    df = simulate()
    assert len(df) >= 800


def test_derivation_matches_independent_recomputation():
    raw = simulate()
    adam = derive_adam(raw)
    check = validate_derivation(adam)
    assert check["chg_match_pct"] == 100.0


def test_exactly_5_templates_defined():
    assert len(TEMPLATES) == 5


def test_two_sample_ttest_sample_size_is_found():
    result = find_required_n("two_sample_ttest")
    assert result["required_n_per_arm"] is not None
    assert result["achieved_power"] >= 0.8


def test_all_templates_produce_valid_results():
    for name in TEMPLATES:
        result = find_required_n(name, n_grid=range(10, 120, 20))
        assert result["template"] == name
