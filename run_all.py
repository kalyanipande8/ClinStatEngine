import json
import os

from src.simulate_raw_data import simulate
from src.adam_pipeline import derive_adam, validate_derivation, generate_tlfs
from src.sample_size_calculator import TEMPLATES, find_required_n


def main():
    raw = simulate()
    adam = derive_adam(raw)
    derivation_check = validate_derivation(adam)
    tlfs = generate_tlfs(adam)

    sample_size_results = {name: find_required_n(name) for name in TEMPLATES}

    summary = {"n_subjects": len(raw), "derivation_validation": derivation_check, "tlfs": tlfs,
               "n_study_design_templates": len(TEMPLATES), "sample_size_results": sample_size_results}

    os.makedirs("results", exist_ok=True)
    with open("results/summary.json", "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    main()
