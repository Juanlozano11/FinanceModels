import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

def main():
    """One-day 95% Value at Risk for a $1M portfolio using Student-t returns."""
    
    # --- Parameters ---
    V = 1_000_000
    mu_ann, sigma_ann = 0.05, 0.20
    days = 252
    z95 = 1.645
    nu = 5          # degrees of freedom
    N = 100_000
    seed = 42

    np.random.seed(seed)

    # --- 1. Annual → Daily ---
    mu_d = mu_ann / days
    sigma_d = sigma_ann / np.sqrt(days)

    # --- 2. Generate t-distributed samples scaled to sigma_d ---
    t_samples = sigma_d * t.rvs(df=nu, size=N) / np.sqrt(nu / (nu - 2))

    # --- 3. Compute daily returns ---
    R = mu_d + t_samples

    # --- 4. Compute losses and Monte Carlo 95% VaR ---
    losses = -V * R
    VaR_MC = np.percentile(losses, 95)

    # --- 5. Analytical Normal 95% VaR ---
    VaR_norm = V * (z95 * sigma_d - mu_d)

    # --- 6. Print results ---
    print(f"Monte Carlo VaR (t=5):   ${VaR_MC:,.2f}")
    print(f"Analytical VaR (Normal): ${VaR_norm:,.2f}")
    print(f"Difference:               ${VaR_MC - VaR_norm:,.2f}")

    # --- 7. Plot ---
    plt.figure(figsize=(8,5))
    plt.hist(losses, bins=60, density=True, alpha=0.7, label="Simulated Losses (t=5)")
    plt.axvline(VaR_MC, color='red', linestyle='--', label='VaR 95% (Monte Carlo)')
    plt.axvline(VaR_norm, color='green', linestyle='--', label='VaR 95% (Normal)')
    plt.title("Loss Distribution and 95% VaR Comparison")
    plt.xlabel("Loss ($)")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    main()