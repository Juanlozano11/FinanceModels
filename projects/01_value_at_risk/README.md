# Project 01 — One-Day Value at Risk (VaR)

### Research Question
Estimate the **95% one-day Value at Risk (VaR)** for a portfolio using both:
1. Analytical methods (assuming Normal returns)
2. Monte Carlo simulation

### Model
\[
R_d \sim \mathcal{N}(\mu_d, \sigma_d^2), \quad
\mu_d = \frac{\mu_{\text{ann}}}{252}, \quad
\sigma_d = \frac{\sigma_{\text{ann}}}{\sqrt{252}}
\]

Then,
\[
\text{VaR}_{0.95} = V(z_{0.95}\sigma_d - \mu_d)
\]

### Files
| File | Purpose |
|------|----------|
| `var_analysis.py` | Main script for analytical + simulation-based VaR |
| `main.ipynb` | Notebook with explanation and plots |
| `results/var_distribution.png` | Visual representation of VaR cutoff |

### Expected Results
- Analytical VaR ≈ **$20,500**
- Monte Carlo VaR ≈ **$20,400**
- Visualization highlights the 5% left-tail of daily returns.