import bisect
import open3d as o3d


class Centres(o3d.geometry.PointCloud):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self._group_regions = []
        self._group_sizes = []

        self._build_boundaries()

    def _build_boundaries(self):
        self._boundaries = [0]
        for size in self._group_sizes:
            self._boundaries.append(self._boundaries[-1] + size)
        
    def add(self, region, cloud):
        self._group_regions.append(region)
        self._group_sizes.append(cloud.shape[0])
        self.append(cloud)
        self._build_boundaries()

    def get_region(self, idx):
        if idx < 0 or idx >= self.points.shape[0]:
            raise IndexError("Global index out of range")

        group_idx = bisect.bisect_right(self.boundaries, idx)
        return self._group_regions[group_idx]