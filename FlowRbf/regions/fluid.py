from .region import Region
from ..functions.radial_basis_function import RadialBasisFunction 


class Fluid(Region):
    def __init__(self, density: float, viscosity: float):
        self._density = None
        self.density = density

        self._viscosity = None
        self.viscosity = viscosity
    
    @property
    def density(self):
        """Getter for the density."""
        return self._density
    
    @density.setter
    def density(self, density: float):
        """Setter for the density."""
        if density <= 0:
            raise ValueError("The density must be positive.")

        self._density = density
    
    @property
    def viscosity(self):
        """Getter for the viscosity."""
        return self._viscosity
    
    @viscosity.setter
    def viscosity(self, viscosity: float):
        """Setter for the viscosity."""
        if viscosity <= 0:
            raise ValueError("The viscosity must be positive.")

        self._viscosity = viscosity

    def operator(self, rbf: RadialBasisFunction, x, y):
        pass