from abc import ABC, abstractmethod


class RadialBasisFunction(ABC):
    @abstractmethod
    def __call__(self, x, y, epsilon=1.0, m=0):
        raise NotImplementedError

