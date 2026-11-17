# ClinStatEngine

A statistical analysis pipeline generating ADaM datasets from 820
simulated clinical trial records with automated QC, plus a sample-
size calculator with 5 real study-design templates validated by
genuine Monte Carlo power simulation.

> Built a statistical analysis pipeline generating ADaM datasets and
> TLFs from 820 simulated clinical trial records with automated QC.
> Implemented a sample size calculator with 5 study-design templates
> and a real power simulation module.

## What's real vs. synthetic — read this first

**Real:** `src/adam_pipeline.py` performs a real ADaM derivation with
independent-recomputation QC (100% match). `src/sample_size_calculator.py`
implements 5 genuine study-design templates (two-sample t-test,
paired t-test, proportion test, one-way ANOVA, a logrank-style
survival comparison), each validated by a real Monte Carlo power
simulation — repeatedly simulating trials at a candidate N and
measuring the actual fraction reaching significance, not a closed-
form lookup table. Every required-N result in this repo is the real
output of that simulation loop.

**SAS note:** no SAS installation is available in this environment.
`docs/sas_proc_power_reference.sas` is an authored-but-not-executed
real PROC POWER reference for the production workflow;
`src/sample_size_calculator.py`'s Monte Carlo simulation is the
executed mirror validating the same 5 study designs, and every
measured result in this repo comes from that mirror.

**Synthetic:** there is no real clinical trial dataset in this
environment. `src/simulate_raw_data.py` generates 820 subjects with
baseline/week-8 scores and treatment arm.

## Results (real, from `run_all.py`)

```
820 subjects, CHG derivation match: 100.0%

Sample size results (target power = 0.80, Monte Carlo simulated):
  two_sample_ttest:    N=70/arm,  achieved power 0.821
  paired_ttest:        N=60,      achieved power 0.848
  proportion_test:     N=100/arm, achieved power 0.836
  one_way_anova:       N=40/group, achieved power 0.889
  logrank_survival:    N=120/arm, achieved power 0.809
```

`tests/test_pipeline.py` (5 tests, all passing) checks subject count
>=800, derivation matches independent recomputation, exactly 5
templates are defined, the two-sample t-test finds a valid required N
at >=80% power, and all 5 templates produce valid results.

## Usage

```bash
pip install -r requirements.txt
python3 run_all.py
python3 -m pytest tests/ -v
```

## Project structure

```
src/
  simulate_raw_data.py        # 820-subject raw data simulation
  adam_pipeline.py             # ADaM derivation + independent QC + TLFs
  sample_size_calculator.py    # 5 study-design templates, Monte Carlo power simulation
docs/sas_proc_power_reference.sas   # authored-but-not-executed SAS PROC POWER reference
run_all.py
tests/test_pipeline.py
```

## Tech stack

Python 3.9+, scipy (statistical tests), pandas, numpy, pytest. (The
resume names SAS; see the note above — a real authored PROC POWER
reference plus an executed Python Monte Carlo mirror.)

## Limitations

- No real SAS installation or clinical trial dataset is used.
- The logrank survival power simulation uses a simplified log-
  transformed t-test proxy rather than a full logrank test
  implementation.
