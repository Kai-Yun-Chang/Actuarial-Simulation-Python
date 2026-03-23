# Actuarial-Simulation-Python
📌 Project Overview

This project develops a Monte Carlo simulation framework to model insurance losses and analyze how risk is distributed between insurers and reinsurers under different policy structures.

The model incorporates a frequency-severity framework and evaluates how deductibles, policy limits, and reinsurance retention reshape loss distributions.

⚙️ Methodology
1. Frequency-Severity Framework

Frequency: Modeled using a Poisson distribution

Severity: Modeled using multiple distributions:

Lognormal

Pareto (heavy-tailed)

Gamma

Exponential

2. Monte Carlo Simulation

Simulated thousands of policy years

Generated aggregate losses: $S = \sum_{i=1}^{n} X_i$
where: $𝑁$: number of claims $X_i$: claim severity

3. Insurance Contract Structure

The model incorporates realistic policy features:

Deductible: filters small claims

Policy Limit: caps large claims

Reinsurance (Stop-Loss / Excess Layer):

Retention level
