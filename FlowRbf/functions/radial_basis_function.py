from abc import ABC, abstractmethod
import numpy as np

class RadialBasisFunction(ABC):
    @abstractmethod
    def __call__(self, r, epsilon=1.0, m=0):
        pass

    def func(self, x, y, epsilon=1.0):
        r = np.linalg.norm(x - y)
        return self(r, epsilon, 0)

    def gradient(self, x, y, epsilon=1.0):
        r = np.linalg.norm(x - y)
        return epsilon * self(r, epsilon, 1) * (x - y) / r
    
    def div(self, x, y, epsilon=1.0):
        return np.sum(self.gradient(x, y, epsilon))

    def hessian(self, x, y, epsilon=1.0):
        r = np.linalg.norm(x - y)
        outer = np.outer(x - y, x - y)
        return (epsilon ** 2 * self(r, epsilon, 2) * outer / r ** 2 + 
                epsilon * self(r, epsilon, 1) *  np.linalg.eye(x.shape[0]) / r - 
                epsilon * self.gradient(x, y, epsilon) * outer / r ** 3)

    @abstractmethod
    def laplacian(self, x, y, epsilon=1.0):
        r = np.linalg.norm(x - y)
        first_d = self(r, epsilon, 1)
        second_d = self(r, epsilon, 2)
        dot = np.dot(x - y, x - y)

        return (epsilon ** 2 * second_d * dot/ r ** 2 + 
                epsilon * first_d / r - 
                epsilon * dot / r ** 3)