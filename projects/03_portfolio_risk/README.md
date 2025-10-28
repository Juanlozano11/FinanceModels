# Project 03 — Two-Asset Portfolio Risk & Correlation

**Goal.** Simulate a 2-asset portfolio with correlated daily returns to study:
- Portfolio return distribution
- Effect of correlation ρ on risk
- Analytical vs. Monte-Carlo variance of the portfolio


---

## Problem Statement (Raw)

You have two assets with daily returns assumed Normal:

- Asset 1: mean μ₁, volatility σ₁  
- Asset 2: mean μ₂, volatility σ₂  
- Correlation: ρ  
- Portfolio weights: **w = (w₁, w₂)** with w₁ + w₂ = 1

**Tasks (20 min):**
1. Simulate **N = 50,000** daily return pairs \((R₁, R₂)\) with the specified **ρ** using Cholesky.
2. Compute portfolio return \( R_p = w_1 R_1 + w_2 R_2 \).
3. Visualize:
   - Histogram of \( R_p \) (density)
   - Scatter of \((R_1, R_2)\) to see correlation
4. Compute and compare **analytical** vs **Monte-Carlo** portfolio variance:
   \[
   \mathrm{Var}(R_p) = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1 w_2 \rho \sigma_1 \sigma_2.
   \]
5. (Optional) Estimate **95% one-day VaR** of the portfolio assuming Normality:
   \[
   \text{VaR}_{0.95} = V \cdot \left( z_{0.95}\,\sigma_p - \mu_p \right),
   \]
   where \( \mu_p = w_1 \mu_1 + w_2 \mu_2 \), \( \sigma_p = \sqrt{\mathrm{Var}(R_p)} \), \( z_{0.95}=1.645 \).

> Keep this file problem-only. Do not include numeric answers here.

---

## Parameters (use these to start; you may change later)

- Portfolio value \( V = \$1{,}000{,}000 \)
- \( \mu_1 = 0.0002,\; \sigma_1 = 0.012 \)
- \( \mu_2 = 0.00015,\; \sigma_2 = 0.009 \)
- \( \rho = 0.4 \)  (try also: −0.2, 0.0, 0.8)
- Weights: \( w_1 = 0.6,\; w_2 = 0.4 \)
- Simulations: \( N = 50{,}000 \)

---

## Expected Artifacts

- Figure 1: Histogram of \( R_p \) (with grid and labeled axes)
- Figure 2: Scatter of \((R_1, R_2)\)
- Console summary (optional): empirical mean/var vs. analytical var, and (optional) VaR

---

## Hints (ask only if you want them)

- Build covariance matrix Σ from σ’s and ρ, then use **Cholesky** to correlate standard Normals.
- Analytical variance uses \( w^\top \Sigma w \).

---

## Extensions (later)

- Sweep ρ across a grid and plot σₚ vs ρ (diversification curve).
- Add a third asset and compare frontier points for a few weight pairs.