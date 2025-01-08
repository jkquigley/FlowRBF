import numpy as np
import scipy.sparse as sp
import open3d as o3d
from radial_basis_function import RadialBasisFunction


class Solver:
    def __init__(self, rbf: RadialBasisFunction, k: int, centres: o3d.t.geometry.PointCloud):
        self.set_rbf(rbf)
        self.set_centres(centres)
        self.set_k(k)

    def set_rbf(self, rbf: RadialBasisFunction):
        self.rbf = rbf

    def set_k(self, k: int):
        self.k = k

    def set_centres(self, centres: o3d.geometry.PointCloud):
        self.centres = centres
        self.n = self.centres.points.shape[0]
        self.kd_tree = o3d.t.geometry.KDTreeFlann(centres)
    
    def solve(self, operators, rhs):
        mat = sp.lil_matrix((self.n, self.n))
        b = np.zeros(self.n)
        for i in range(self.n):
            control = self.centres.points[i]
            operator = operators[control.operator_idx]
            _, idx, _ = self.kd_tree.search_knn_vector_3d(control, self.k)
            for j in idx:
                val = operator(self.rbf)(control, self.centres.points[j])
                mat[i, j] = val
                mat[j, i] = val
            
            b[i] = rhs[control.operator_idx](control)
        
        return sp.linalg.solve(mat, b)
