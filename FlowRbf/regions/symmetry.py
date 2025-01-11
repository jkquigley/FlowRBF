from region import Region
from FlowRbf.functions.radial_basis_function import RadialBasisFunction


class Symmetry(Region):
    def __init__(self):
        pass

    def operator(self, rbf: RadialBasisFunction):
        def func(x, y, *args, **kwargs):
            raise NotImplementedError()  # TODO: Implement this
        
        return func
