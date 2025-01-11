from abc import ABC, abstractmethod
from enum import Enum
from FlowRbf.functions.radial_basis_function import RadialBasisFunction 


class Region(ABC):
    class RegionType(Enum):
        INTERIOR = 0
        NO_SLIP_WALL = 1
        FREE_SLIP_WALL = 2
        VELOCITY_INLET = 3
        MASS_FLOW_INLET = 4
        PRESSURE_INLET = 5
        VELOCITY_OUTLET = 6
        MASS_FLOW_OUTLET = 7
        PRESSURE_OUTLET = 8
        SYMMETRY = 9

    @abstractmethod
    def operator(self, rbf: RadialBasisFunction):
        pass
