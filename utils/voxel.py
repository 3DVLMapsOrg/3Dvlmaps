import numpy as np

class Voxel:
    def __init__(self, coord, feature_shape) -> None:
        self.coordinates = coord
        self.feature_weight = 0
        self.color_weight = 0
        self.features = np.zeros(feature_shape)
        self.colors = np.zeros((1,3))

    def update_color(self, color):
        self.colors = (self.colors * self.color_weight + color) / (self.color_weight + 1)
        self.color_weight += 1

    def update_feature(self, feature):
        if self.features.shape != feature.shape:
            raise ValueError("Feature shape must match voxel feature shape")

        self.features = (self.features * self.feature_weight + feature) / (self.feature_weight + 1)
        self.feature_weight += 1

def GetVoxelCoor(point, voxel_size=0.05):
    return ((point) / voxel_size).astype(int)

def GetAbsVoxelCoor(point, min_bound_voxel_grid, voxel_size=0.05):
    return ((point - min_bound_voxel_grid) / voxel_size).astype(int)