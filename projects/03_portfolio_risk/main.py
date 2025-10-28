# projects/03_two_asset_portfolio_risk/main.py
"""
Project 03 — Two-Asset Portfolio Risk & Correlation
Fully working version.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_correlated_returns(mu1, mu2, sigma1, sigma2, rho, N, seed=7):
    """
    Generate N samples of (R1, R2) ~ Normal with given means, vols, and correlation rho.
    Use Cholesky on the 2x2 covariance matrix.
    Returns: R1 (N,), R2 (N,)
    """
    np.random.seed(seed)

    # 1) Build covariance matrix Sigma
    Sigma = np.array([
        [sigma1**2, rho * sigma1 * sigma2],
        [rho * sigma1 * sigma2, sigma2**2]
    ])

    # 2) Cholesky factorization: Sigma = L @ L.T
    L = np.linalg.cholesky(Sigma)

    # 3) Generate independent standard normals Z ~ N(0, I)
    Z = np.random.normal(size=(2, N))

    # 4) Correlate: X = L @ Z
    X = L @ Z

    # Add means
    mu_vec = np.array([[mu1], [mu2]])
    R = mu_vec + X

    # 5) Return R1, R2 as 1D arrays
    R1, R2 = R[0, :], R[1, :]
    return R1, R2


def main():
    # --- Parameters ---
    V = 1_000_000
    mu1, sigma1 = 0.0002, 0.012
    mu2, sigma2 = 0.00015, 0.009
    rho = 0.4
    w1, w2 = 0.6, 0.4
    N = 50_000
    seed = 7

    # 1) Simulate correlated daily returns
    R1, R2 = simulate_correlated_returns(mu1, mu2, sigma1, sigma2, rho, N, seed)

    # 2) Portfolio returns
    Rp = w1 * R1 + w2 * R2

    # 3a) Histogram of portfolio returns
    plt.figure(figsize=(8, 5))
    plt.hist(Rp, bins=80, density=True, alpha=0.85)
    plt.title("Portfolio Daily Return $R_p$")
    plt.xlabel("$R_p$")
    plt.ylabel("Density")
    plt.grid(True, alpha=0.3)
    plt.show()

    # 3b) Scatter of (R1, R2)
    plt.figure(figsize=(6, 6))
    plt.scatter(R1, R2, s=4, alpha=0.3)
    plt.title("Asset Returns Scatter (R1 vs R2)")
    plt.xlabel("R1")
    plt.ylabel("R2")
    plt.grid(True, alpha=0.3)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()

    # 4) Analytical vs Monte Carlo variance
    mu_p = w1 * mu1 + w2 * mu2
    var_p_analytical = (w1**2) * (sigma1**2) + (w2**2) * (sigma2**2) + 2 * w1 * w2 * rho * sigma1 * sigma2
    var_p_mc = np.var(Rp, ddof=0)

    print("\n=== Portfolio Risk Summary ===")
    print(f"Analytical Var(Rp): {var_p_analytical:.8f}")
    print(f"Monte Carlo Var(Rp): {var_p_mc:.8f}")
    print(f"Difference: {abs(var_p_analytical - var_p_mc):.8e}")

    # 5) (Optional) VaR 95%
    z95 = 1.645
    sigma_p = np.sqrt(var_p_analytical)
    VaR95 = V * (z95 * sigma_p - mu_p)
    print(f"95% One-Day VaR (Normal): ${VaR95:,.2f}")


if __name__ == "__main__":
    main()