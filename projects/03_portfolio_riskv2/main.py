import numpy as np
import matplotlib.pyplot as plt

def portfolio_sigma(sigma1, sigma2, w1, w2, rho):
    """Return portfolio volatility for given parameters."""
    # Formula: σ_p = sqrt(w1²σ1² + w2²σ2² + 2w1w2ρσ1σ2)
    sigma_p = np.sqrt((w1**2)*(sigma1**2) + (w2**2)*(sigma2**2) + 2*w1*w2*rho*sigma1*sigma2)
    return sigma_p

def main():
    w1, w2 = 0.6, 0.4
    sigma1, sigma2 = 0.012, 0.009

    # 1. Create correlation values from -1 to +1
    rhos = np.linspace(-1, 1, 11)

    # 2. Compute portfolio volatility for each rho
    sigmas = []
    for rho in rhos:
        sigma_p = portfolio_sigma(sigma1, sigma2, w1, w2, rho)
        sigmas.append(sigma_p)
        print(f"rho={rho:+.1f} → portfolio σ_p = {sigma_p:.5f}")

    # 3. Plot correlation vs portfolio volatility
    plt.figure(figsize=(8,5))
    plt.plot(rhos, sigmas, marker="o", linewidth=2)
    plt.title("Effect of Correlation on Portfolio Volatility")
    plt.xlabel("Correlation ρ")
    plt.ylabel("Portfolio Volatility σ_p")
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    main()