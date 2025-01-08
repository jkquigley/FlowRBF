import numpy as np
import open3d.core as o3c
from radial_basis_function import RadialBasisFunction


class Solver(self):
    def __init__(self, rbf: Radi, k, alpha, beta=None):
        self.rbf = rbf
        self.set_points(alpha, beta)
        self.set_k(k)
    
    def set_k(self, k: int):
        self.k = k

    def set_points(self, alpha: o3c.geometry.PointCloud, beta: o3c.geometry.PointCloud = None):
        self.alpha = alpha
        if beta is None:
            self.beta = alpha
            self.collocated = True
        else:
            self.beta = beta
            self.collocated = False
        
        self.beta_knn = o3c.geometry.KDTreeFlann(alpha)
