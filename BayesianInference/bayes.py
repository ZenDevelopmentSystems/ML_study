"""
Module for Bayesian Inference.
"""

import numpy as np
import scipy.stats as stats

def coin_flip(n, trials):
    """
    """
    num_of_success = np.random.binomial(
        n=n, p=0.5, size=trials) == k
    res = sum(num_of_success) / trials * 100
    return res

if __name__ == "__main__":
    print('Succcess')