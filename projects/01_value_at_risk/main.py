# projects/01_value_at_risk/var_analysis.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

# --- Parameters ---
V = 1_000_000           # portfolio value
mu_ann = 0.05           # annual drift
sigma_ann = 0.20        # annual volatility
days = 252              # trading days
z95 = 1.645             # z-score for 95% confidence
N = 100_000             # Monte Carlo paths

# --- Derived daily parameters ---
mu_d = mu_ann / days
sigma_d = sigma_ann / np.sqrt(days)

# --- Analytical VaR ---
VaR_analytical = V * (z95 * sigma_d - mu_d)

# --- Monte Carlo Simulation ---
rng = np.random.default_rng(42)
R = rng.normal(loc=mu_d, scale=sigma_d, size=N)
losses = -V * R
VaR_MC = np.percentile(losses, 95)

# --- Print results ---
print(f"Daily μ: {mu_d:.8f}")
print(f"Daily σ: {sigma_d:.8f}")
print(f"Analytical VaR 95%: ${VaR_analytical:,.2f}")
print(f"Monte Carlo VaR 95%: ${VaR_MC:,.2f}")

# --- Visualization ---
x = np.linspace(mu_d - 4*sigma_d, mu_d + 4*sigma_d, 500)
pdf = norm.pdf(x, mu_d, sigma_d)
cutoff = mu_d - z95 * sigma_d

plt.figure(figsize=(8,5))
plt.plot(x, pdf, linewidth=2)
plt.fill_between(x[x <= cutoff], pdf[x <= cutoff], color='red', alpha=0.3)
plt.axvline(cutoff, color='red', linestyle='--', label='95% VaR cutoff')
plt.title('Daily Return Distribution and 95% VaR Region')
plt.xlabel('Daily Return')
plt.ylabel('Probability Density')
plt.legend()
plt.grid()

# Save figure
os.makedirs("projects/01_value_at_risk/results", exist_ok=True)
plt.savefig("projects/01_value_at_risk/results/var_distribution.png", dpi=300)
plt.show()