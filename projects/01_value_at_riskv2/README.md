# Project 01 — Value at Risk (t-Distribution)

**Goal.** Re-implement one-day 95 % VaR but assume daily returns follow a Student-t distribution with ν = 5 degrees of freedom.  
Compare:
- Analytical VaR (Normal assumption)
- Empirical VaR (Monte Carlo using Student-t samples)

---

## Problem

Portfolio value \(V = 1{,}000{,}000\).  
Annual volatility \( \sigma_{ann} = 0.20 \).  
Annual drift \( \mu_{ann} = 0.05 \).  
Trading days per year \( = 252 \).  
Confidence level \( = 95\% \).  
Degrees of freedom \( \nu = 5 \).  
Simulations \( N = 100{,}000 \).

Tasks:
1. Convert annual μ, σ to daily.
2. Simulate N daily returns \(R_d\) from a scaled Student-t(ν).
3. Compute losses \(L = -V R_d\).
4. Estimate 95 % Monte Carlo VaR = 95th percentile of L.
5. Compare with Normal analytical VaR.
6. Plot both loss distributions on the same chart.

---

## Outputs
- Print both VaR values and their difference.
- Plot histogram of losses with red vertical lines for each VaR.
