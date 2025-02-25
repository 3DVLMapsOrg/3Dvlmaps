import open3d as o3d
import numpy as np

def create_voxel(coordinates, predicts, color_palette, voxel_size=0.05):
    colored_voxel_grid = o3d.geometry.VoxelGrid()
    colored_voxel_grid.voxel_size = voxel_size

    for coordinate, mask in zip(coordinates, predicts):
        o3d_voxel = o3d.geometry.Voxel(coordinate, color_palette[mask])
        colored_voxel_grid.add_voxel(o3d_voxel)

    return colored_voxel_grid

def create_real_rgb_voxel(coordinates, colors, voxel_size=0.05):
    voxel_grid = o3d.geometry.VoxelGrid()
    voxel_grid.voxel_size = voxel_size

    for coordinate, color in zip(coordinates, colors):
        o3d_voxel = o3d.geometry.Voxel(coordinate, color.reshape(3,1))
        voxel_grid.add_voxel(o3d_voxel)

    return voxel_grid

def create_white_voxel(coordinates, color=[1,1,1], voxel_size=0.05):
    voxel_grid = o3d.geometry.VoxelGrid()
    voxel_grid.voxel_size = voxel_size

    for coordinate in coordinates:
        o3d_voxel = o3d.geometry.Voxel(coordinate, color)
        voxel_grid.add_voxel(o3d_voxel)

    return voxel_grid

def visualize_map(voxel_grid, background_color = [0,0,0]):
    vis = o3d.visualization.Visualizer()
    vis.create_window(visible=True)
    vis.get_render_option().background_color = background_color
    vis.add_geometry(voxel_grid)

    # x,y,x -> red, green, and blue
    axis_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0)
    vis.add_geometry(axis_frame)

    print("running visualization")
    vis.run()
    vis.close()
