from numpy.polynomial import Polynomial


class RadialBasisFunction:
    def __init__(self):
        pass

    def __call__(self, r, m=0, epsilon=1.0):
        raise NotImplementedError


class PolyharmonicSpline(RadialBasisFunction):
    def __init__(self, k=3):
        self.super().__init__()

        if self.k % 2 == 0 or self.k < 1:
            raise ValueError("`m` is a positive odd integrer.")
        self.k = k

        self.poly = Polynomial([0] * (k - 1) + [1])
    
    def __call__(self, r, m=0, epsilon=1.0):
        return self.epsilon ** self.k * self.poly.deriv(r, m)
