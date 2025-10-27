# Project 02 — Geometric Brownian Motion (GBM) Simulation

**Goal.** Build a daily GBM simulator to study one-year price evolution, visualize sample paths, and compare empirical vs. theoretical results — without peeking at solutions.

---

## Problem Statement (Raw)

A stock starts at **S₀ = 100** and follows **Geometric Brownian Motion (GBM)**

\[
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
\]

with annual parameters: **μ = 0.08**, **σ = 0.25**, and **252 trading days/year**.

**Tasks**
1. Simulate **10,000** price paths over **T = 1 year** with **daily** steps.  
2. Plot **≥10** sample paths on one chart.  
3. Estimate and visualize the **distribution of final prices** \(S_T\).  
4. Compare **empirical mean** of \(S_T\) to the **theoretical mean** \(\mathbb{E}[S_T]=S_0 e^{\mu T}\).  
5. **(Bonus)** Estimate \( \mathbb{P}(S_T < 90) \).

> ⚠️ Do not include answers/values here. Keep this file problem-focused.

---

## Model & Discretization

Use the **Euler–Maruyama** (log form) or the exact GBM step:

\[
S_{t+\Delta t} = S_t \exp\!\Big((\mu - \tfrac{1}{2}\sigma^2)\Delta t + \sigma \sqrt{\Delta t}\,Z\Big), \quad Z \sim \mathcal N(0,1)
\]

with \(\Delta t = \tfrac{1}{252}\).

---

## Repository Layout