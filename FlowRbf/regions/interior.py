from radial_basis_function import RadialBasisFunction 

class Interior:
    def __init__(self, porosity: float = 0.0):
        if porosity < 0.0 or porosity > 1.0:
            raise ValueError("`porosity` must be in [0, 1].")
        
        self.porosity = porosity

    def operator(self, rbf: RadialBasisFunction):
        def func(x, y, *args, **kwargs):
            return rbf(x, y, *args, **kwargs)
        
        return func
