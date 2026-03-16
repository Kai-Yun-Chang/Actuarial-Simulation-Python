# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:30:28 2026

@author: user
"""
"""
Created on Mon Mar 16 14:56:42 2026

@author: user
"""
import numpy as np

# Define function
# Severity distributions 產生損失金額 -----------------------------

def generate_severity(n_claims, dist, params):

    if dist == "lognormal":
        mu, sigma = params
        return np.random.lognormal(mu, sigma, n_claims)

    elif dist == "gamma":
        shape, scale = params
        return np.random.gamma(shape, scale, n_claims)

    elif dist == "exponential":
        scale = params[0]
        return np.random.exponential(scale, n_claims)

    elif dist == "pareto":
        shape = params[0]
        return (np.random.pareto(shape, n_claims) + 1) * 1000

    else:
        raise ValueError("Unsupported distribution")


# Policy structure (deductible & limit) -----------------------------

def compute_payments(claim_sizes, deductible, limit):

    payments = []

    for claim in claim_sizes:

        # deductible
        payment = max(0, claim - deductible)

        # policy limit
        payment = min(payment, limit)

        payments.append(payment)

    return np.array(payments)

# Per-claim reinsurance -----------------------------

def apply_reinsurance(payments, retention):

    insurer_claims = np.minimum(payments, retention)
    reinsurer_claims = np.maximum(0, payments - retention)

    return insurer_claims.sum(), reinsurer_claims.sum()

# One year simulation -----------------------------

def per_simulation(n_policy, lambda_freq, dist, params, deductible, limit, retention):

    # frequency - 決定理賠claims次數
    n_claims = np.random.poisson(lambda_freq * n_policy)

    if n_claims == 0:
        return 0,0

    # severity - 隨機產生每件理賠案件金額
    claim_sizes = generate_severity(n_claims, dist, params)

    # apply policy terms
    payments = compute_payments(claim_sizes, deductible, limit)

    # reinsurance
    insurer_loss, reinsurer_loss = apply_reinsurance(payments, retention)

    return insurer_loss, reinsurer_loss

# Monte Carlo simulation -----------------------------

def run_simulation(n_sim, n_policy, lambda_freq, dist, params, deductible, limit, retention):

    insurer_losses = []
    reinsurer_losses = []

    for i in range(n_sim):

        insurer_loss, reinsurer_loss = per_simulation(n_policy, lambda_freq, dist, params, deductible, limit, retention)
        insurer_losses.append(insurer_loss)
        reinsurer_losses.append(reinsurer_loss)

    return np.array(insurer_losses), np.array(reinsurer_losses)