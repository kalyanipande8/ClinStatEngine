"""Simulate 820 raw clinical trial subject records -- the real input
the ADaM derivation pipeline standardizes."""
from __future__ import annotations

import numpy as np
import pandas as pd

N_SUBJECTS = 820
SEED = 1187


def simulate(n: int = N_SUBJECTS, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    return pd.DataFrame({
        "USUBJID": [f"S-{i:04d}" for i in range(n)],
        "ARM": rng.choice(["Active", "Placebo"], n),
        "BASESCORE": np.round(rng.normal(50, 10, n), 2),
        "WEEK8SCORE": np.round(rng.normal(44, 11, n), 2),
    })


if __name__ == "__main__":
    print(simulate().shape)
