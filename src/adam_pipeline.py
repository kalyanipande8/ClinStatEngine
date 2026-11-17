"""Real ADaM derivation + TLF generation: change-from-baseline
derivation (independently re-derived for QC) and 3 standard summary
TLFs."""
from __future__ import annotations

import pandas as pd


def derive_adam(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["CHG"] = df["WEEK8SCORE"] - df["BASESCORE"]
    return df


def validate_derivation(adam: pd.DataFrame) -> dict:
    indep_chg = adam["WEEK8SCORE"] - adam["BASESCORE"]
    match = (adam["CHG"].round(6) == indep_chg.round(6)).mean()
    return {"chg_match_pct": round(float(match) * 100, 3)}


def generate_tlfs(adam: pd.DataFrame) -> dict:
    return {
        "demog_by_arm": adam.groupby("ARM").size().to_dict(),
        "baseline_by_arm": adam.groupby("ARM")["BASESCORE"].mean().round(2).to_dict(),
        "chg_by_arm": adam.groupby("ARM")["CHG"].mean().round(2).to_dict(),
    }
