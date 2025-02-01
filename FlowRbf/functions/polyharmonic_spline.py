import numpy as np
from numpy.polynomial import Polynomial
from .radial_basis_function import RadialBasisFunction


class PolyharmonicSpline(RadialBasisFunction):
    def __init__(self, k=3):
        self.super().__init__()

        if self.k % 2 == 0 or self.k < 1:
            raise ValueError("`k` is a positive odd integrer.")
        self.k = k

        self.poly = Polynomial([0] * (k - 1) + [1])
    
    def __call__(self, r, epsilon=1.0, m=0):
        return self.poly.deriv(epsilon * r, m)
