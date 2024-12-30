from numpy.polynomial import Polynomial


class RadialBasisFunction:
    def __init__(self, epsilon=1.0):
        self.epsilon = epsilon

    def __call__(self, r):
        raise NotImplementedError


class PolyharmonicSpline(RadialBasisFunction):
    def __init__(self, epsilon=1.0, k=3):
        self.super().__init__(epsilon)

        if self.k % 2 == 0 or self.k < 1:
            raise ValueError("`m` is a positive odd integrer.")
        self.k = k

        self.poly = Polynomial([0] * (k - 1) + [1])
    
    def __call__(self, r, m=0):
        return self.epsilon ** self.k * self.poly.deriv(r, m)
