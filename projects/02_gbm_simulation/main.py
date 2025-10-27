import numpy as np

def simulate_gbm_paths(S0, mu, sigma, T, days, n_paths, seed):
    # Set random seed for reproducibility
    np.random.seed(seed)
    
    # Calculate time increment (dt) for each step
    dt = T / days
    
    # Generate random increments for Brownian motion (Wiener process)
    # Normally distributed with mean 0 and std sqrt(dt)
    dW = np.random.normal(loc=0.0, scale=np.sqrt(dt), size=(days, n_paths))
    
    # Initialize array to store simulated stock prices
    # Shape: (days + 1) x n_paths, including initial price at t=0
    S = np.zeros((days + 1, n_paths))
    
    # Set initial stock prices at time 0
    S[0] = S0
    
    # Iterate over each time step to simulate paths
    for t in range(1, days + 1):
        # Apply Geometric Brownian Motion formula:
        # S_t = S_{t-1} * exp((mu - 0.5*sigma^2)*dt + sigma*dW)
        S[t] = S[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * dW[t-1])
    
    # Return simulated stock price paths
    return S

def main():
    # --- Parameters ---
    S0 = 100            # Initial stock price
    mu = 0.08           # Expected annual return (drift)
    sigma = 0.25        # Annual volatility
    T = 1               # Total time horizon in years
    days = 252          # Number of trading days in one year
    n_paths = 10_000    # Number of simulated paths
    seed = 42           # Random seed for reproducibility
    K = 90.0           # Threshold for bonus probability (e.g., P(S_T < K))

    # 1) Simulate GBM paths
    S = simulate_gbm_paths(S0, mu, sigma, T, days, n_paths, seed)
    
    # Extract final prices at maturity T
    ST = S[-1]

    # --- Summary metrics (printed as a small table) ---
    emp_mean = float(np.mean(ST))
    emp_std  = float(np.std(ST, ddof=0))
    median   = float(np.median(ST))
    theo_mean = float(S0 * np.exp(mu * T))
    prob_below = float(np.mean(ST < K))
  
    # Build rows for a simple ASCII table without extra deps
    rows = [
        ("Parameter", "Value"),
        ("-"*9, "-"*20),
        ("S0", f"{S0:,.2f}"),
        ("mu (annual)", f"{mu:.4f}"),
        ("sigma (annual)", f"{sigma:.4f}"),
        ("T (years)", f"{T}"),
        ("days", f"{days}"),
        ("paths", f"{n_paths:,}"),
        ("", ""),
        ("Metric", "Result"),
        ("-"*6, "-"*20),
        ("E[S_T] empirical", f"{emp_mean:,.4f}"),
        ("Std[S_T] empirical", f"{emp_std:,.4f}"),
        ("Median S_T", f"{median:,.4f}"),
        ("E[S_T] theoretical", f"{theo_mean:,.4f}"),
        (f"P(S_T < {K:.2f})", f"{prob_below:.4%}"),
    ]
  
    # Pretty print with aligned columns
    col1_width = max(len(str(r[0])) for r in rows)
    col2_width = max(len(str(r[1])) for r in rows)
    print("\n=== GBM Simulation Summary ===")
    for left, right in rows:
        print(f"{left:<{col1_width}}  |  {right:>{col2_width}}")
    print()  # blank line after table

    # 2) Plot sample paths for visualization
    import matplotlib.pyplot as plt
    plt.figure(figsize=(9,5))
    # Plot first 10 simulated paths out of 10,000
    plt.plot(S[:, :10])
    plt.title("GBM Sample Paths (10 out of 10,000)")
    plt.xlabel("Days")
    plt.ylabel("Stock Price")
    plt.grid(True, alpha=0.3)
    plt.show()

    # 3) Plot histogram of final stock prices to observe distribution
    plt.figure(figsize=(8,5))
    plt.hist(ST, bins=60, density=True, alpha=0.85)
    plt.title("Distribution of Final Prices $S_T$")
    plt.xlabel("$S_T$")
    plt.ylabel("Density")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()