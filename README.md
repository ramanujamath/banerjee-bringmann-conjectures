# Proofs of two conjectures of Banerjee and Bringmann

This repository contains the paper

> **Proofs of two conjectures of Banerjee and Bringmann on overpartitions and universal mock theta functions**
> Ramanuja (2026)

together with the LaTeX source and all Python scripts used to discover and check the results.

## Summary

Banerjee and Bringmann ([arXiv:2611.00728](https://arxiv.org/abs/2611.00728)) related two families of restricted overpartitions, counted by `op_1^[1](n)` and `op_1^[2](n)`, to Hickerson's universal mock theta functions. They conjectured two infinite families of congruences modulo 2 and 4 (their Conjectures 4.1 and 4.2). The paper proves both, in each case through a sharper statement:

- `op_1^[1](4m)` is odd if and only if `m` is a triangular number (Theorem 1.3, giving Conjecture 4.1);
- `op_1^[2](2m)` is congruent mod 4 to the sum over divisors `d` of `8m+1` of the Kronecker symbol `(-4/d)` (Theorem 1.5, giving Conjecture 4.2).

It also proves:

- `op_1^[1](4n+1)` is divisible by 4 for all `n` (Theorem 1.7);
- an explicit formula for `op_1^[1](4m)` mod 4 in terms of representation numbers of binary quadratic forms (Theorem 1.8);
- a description of `op_1^[1](4m)` mod 4 whenever a prime `p` with `p ≡ 1 (mod 8)` or `p ≡ 13, 23 (mod 24)` exactly divides `8m+1`, which gives infinitely many explicit congruence families (Theorem 1.9, Corollary 1.10);
- an exact identity for the even part of `OP_1^[2](q)` (Proposition 1.11).

## Repository layout

| Path | Contents |
| --- | --- |
| `paper/overpartitions_mock_theta.tex` | LaTeX source of the paper (amsart, compiles with `pdflatex`, no external `.bib`) |
| `paper/overpartitions_mock_theta.pdf` | Compiled paper |
| `submission/cover_letter.tex`, `.pdf` | Cover letter for submission to *The Ramanujan Journal* |
| `scripts/` | All Python scripts (exploration and verification) |
| `scripts/generate_data.sh` | Regenerates the intermediate data files the scripts read |

## Reproducing the computations

Requirements: Python 3 with `numpy`. All computations are exact integer power-series arithmetic (modulo `2^40` where noted) or exact counts of representations by quadratic forms.

```bash
cd scripts
bash generate_data.sh        # creates op1_40000.npy, op2_40000.npy, omega.npy, B.npy, op1_4m_mod4.npy, found.npy
python3 conj41.py            # then run any check script, e.g. Conjecture 4.1 for primes < 200
```

The `.npy` files are generated data and are not committed (see `.gitignore`). Scripts must be run from inside `scripts/` because they import each other and read the data files from the working directory.

To build the paper: `cd paper && pdflatex overpartitions_mock_theta.tex` (run twice for references).

## Script index

Scripts are listed by the result they support. Some are exploratory: they record the path to the results, including searches that found nothing and two scripts that contain mistakes later corrected (marked *superseded*).

**Shared helpers and data generation**

| Script | Purpose |
| --- | --- |
| `op.py` | Coefficients of `OP_1^[1](q)` from the Banerjee–Bringmann series (`python3 op.py N`) |
| `op2.py` | Coefficients of `OP_1^[2](q)`; also provides series helpers `mul1`, `div1`, `shift` |
| `lib.py` | Eta-quotient series and a congruence scanner |
| `etafit.py` | Identifies a series as an eta quotient via its logarithmic derivative |
| `modfit.py` | Searches for eta quotients matching a series modulo 2 or 4 |
| `omegapieces.py` | Coefficients of `omega(q)`; parity of its 4-dissection pieces |
| `bodd.py` | Coefficients of `B(q)`; parity of its odd-index coefficients |
| `classify.py` | `a(4m) mod 4` for `m < 10^6` via Theorem 1.8 (checked against direct values), and a scan for congruence progressions |

**Checks against the combinatorial definitions**

| Script | Purpose |
| --- | --- |
| `brute1.py` | Brute-force count of `op_1^[1](n)`, `n < 36` |
| `brute2.py` | Brute-force count of `op_1^[2](n)`, `n < 40` |

**Initial exploration**

| Script | Purpose |
| --- | --- |
| `scan.py` | *Superseded.* First congruence scan over eta quotients; it used single factors `(1-q^k)` instead of `(q^k;q^k)_inf`. |
| `scan2.py` | Corrected scan over eta quotients (recovers Ramanujan's congruences for `p(n)`) |
| `verify.py` | Extended checks of candidate congruences from `scan2.py` |

**Theorem 1.3 and Conjecture 4.1**

| Script | Purpose |
| --- | --- |
| `conj41.py` | Conjecture 4.1 for all primes `p < 200`; triangular-number pattern |
| `proof_check.py` | The `nu`/`omega` identity (B) exactly and the mod 2 reduction |

**Theorem 1.5 and Conjecture 4.2**

| Script | Purpose |
| --- | --- |
| `conj42.py` | Conjecture 4.2 for primes `p < 140`, and its failure for `p ≡ 1 (mod 8)` |
| `explore2.py` | Pattern of `op_1^[2](2m)` mod 4 against the factorization of `8m+1` |
| `fit.py` | Eta-quotient search for the mod 4 correction (interrupted; replaced by the analytic argument) |
| `check42.py` | Theorem 1.5, the `f_4/f_1` congruence, and the facts about `B(q)` |

**Dissections of omega and B; Theorem 1.7**

| Script | Purpose |
| --- | --- |
| `dissect.py`, `dissect2.py` | Which dissection pieces of `omega`, `B`, `op_1^[1]`, `op_1^[2]` are eta quotients |
| `omegacheck.py` | Lemma 3.1 (i), (ii), (iv) and the parity of `w(4n+2)` |
| `apsy.py` | Watson's identity and its 4-dissection, `f(q) f_1 ≡ 1 (mod 4)`, parity of `omega` |
| `scanop.py` | Congruence scan for `op_1^[1]`, `op_1^[2]` modulo 3, 4, 5, 7, 8, 16 |
| `op1mod4.py` | Theorem 1.7 (both statements) |

**Modulo 8 and Proposition 1.11**

| Script | Purpose |
| --- | --- |
| `mod8explore.py` | `op_1^[2](2m)` mod 8 against the divisor sum |
| `btest.py` | Compares `b(4n+3)/2 mod 2` with partition parities `p(an+b)` |
| `exact8.py` | Proposition 1.11 exactly for `m < 6000` |

**Theorem 1.8: `a(4m)` mod 4 via binary quadratic forms**

| Script | Purpose |
| --- | --- |
| `families.py`, `mod3.py`, `primes8.py` | Structure of the progressions found by `classify.py` |
| `cstruct.py`, `binfit.py`, `formsearch.py` | Searches for binary-form formulas |
| `class2.py` | Class `m ≡ 2 (mod 3)` formula for `m < 10^6`, and the predicted families |
| `dbg.py`, `id3.py` | The reduced mod 2 theta identity for class `m ≡ 2 (mod 3)` |
| `id2.py` | *Superseded* by `id3.py` (its shift used `np.roll`, which wraps around) |
| `ramid.py` | Ramanujan's identity `psi(q)psi(q^3) = phi(q^6)psi(q^4) + q phi(q^2)psi(q^12)` exactly |
| `class0dbg.py`, `class0.py` | Class `m ≡ 0 (mod 3)`: theta-product form and representation-number form |
| `class1.py` | Class `m ≡ 1 (mod 3)`: theta-product form and representation-number form |
| `final_check.py` | Simplified class `m ≡ 1` formula for `m < 300000`; families with `p^3 ∥ 8m+1` |

**Theorem 1.9 and Corollary 1.10: prime families**

| Script | Purpose |
| --- | --- |
| `primefam.py` | Which primes `p < 400` give families, by residue mod 24 |
| `p1rule.py`, `p1fail.py` | For `p ≡ 1, 17 (mod 24)`: failures occur only when `(8m+1)/p` is a square |
| `epsrule.py` | Formula for `epsilon(p)` for all primes `p ≡ 1 (mod 8)` below `2·10^5` |
| `thm8check.py` | Theorem 1.9(b) for `p < 5000` (246,192 cases) |
| `epssimp.py` | Simplified rule for `p ≡ 1 (mod 24)`; class numbers of the orders used |

## Use of AI tools

An AI assistant (Claude, Anthropic) was used for exploratory computations, literature search and drafting, including writing these scripts. The author has checked all statements and proofs and takes full responsibility for the content.

## Citation

If you use this work, please cite the paper (arXiv identifier to be added once posted).
