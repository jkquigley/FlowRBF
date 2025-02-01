import numpy as np
import open3d as o3d
import scipy.sparse as sp
from .functions.radial_basis_function import RadialBasisFunction
from .centres import Centres


class Solver:
    def __init__(self, rbf: RadialBasisFunction, centres: Centres, k: int):
        self._kd_tree = None

        self._rbf = None
        self.rbf = rbf

        self._centres = None
        self.centres = centres

        self._k = None
        self.k = k

    @property
    def rbf(self):
        """Getter for the radial basis function."""
        return self._rbf

    @rbf.setter
    def rbf(self, rbf: RadialBasisFunction):
        """Setter for the radial basis function."""
        self._rbf = rbf
    
    @property
    def centres(self):
        """Getter for the centres."""
        return self._centres
    
    @centres.setter
    def centres(self, value: Centres):
        """Setter for the system."""
        self._centres = value
        self._kd_tree = o3d.geometry.KDTreeFlann(self._centres)
    
    @property
    def k(self):
        """Getter for the number of nearest neighbours."""
        return self._k
    
    @k.setter
    def k(self, value: int):
        """Setter for the number of nearest neighbours."""
        self._k = value

    def _matrix(self):
        """Matrix of the system."""
        rows = []
        cols = []
        mat_vals = []
        rhs_vals = []
        for i in range(self.system.n):
            x = self.centres.points[i]
            region = self.centres.get_region(i)

            _, idxs, _ = self._kd_tree.search_knn_vector_3d(x, self.k)
            for j in idxs:
                y = self.centres.points[j]

                mat_val, rhs_val = region.operator(self.rbf, x, y)

                rows.append(i)
                cols.append(j)
                mat_vals.append(mat_val)
                rhs_vals.append(rhs_val)
        
        return sp.csr_matrix((mat_vals, (rows, cols)), shape=(self.system.n, self.system.n)), np.array(rhs_vals)
