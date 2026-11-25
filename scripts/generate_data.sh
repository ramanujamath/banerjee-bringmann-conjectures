#!/usr/bin/env bash
# Regenerate the intermediate data files (*.npy) used by the verification scripts.
# Run from inside the scripts/ directory:  bash generate_data.sh
set -euo pipefail

python3 op.py 40000        # op1_40000.npy : coefficients of OP_1^[1](q) up to q^39999
python3 op2.py 40000       # op2_40000.npy : coefficients of OP_1^[2](q) up to q^39999
python3 omegapieces.py     # omega.npy     : coefficients of omega(q) up to q^5999
python3 bodd.py            # B.npy         : coefficients of McIntosh's B(q) up to q^11999
python3 classify.py        # op1_4m_mod4.npy (a(4m) mod 4 for m < 10^6, via Theorem 1.8) and found.npy
