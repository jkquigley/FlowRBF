from abc import ABC, abstractmethod
from ..functions.radial_basis_function import RadialBasisFunction 


class Region(ABC):
    @abstractmethod
    def operator(self, rbf: RadialBasisFunction, x, y):
        pass
