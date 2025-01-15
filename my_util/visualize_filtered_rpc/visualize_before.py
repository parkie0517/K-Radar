import numpy as np
import open3d as o3d
from matplotlib import cm

# Load the radar point cloud data
root_path = "./my_util/visualize_filtered_rpc"
rpc_before = np.load(root_path + '/rpc_before.npy')

# Extract x, y, z coordinates and intensity
xyz = rpc_before[:, :3]
intensity = rpc_before[:, 3]

# Print intensity stats for debugging
print("Intensity Stats:")
print(f"Min: {intensity.min()}, Max: {intensity.max()}, Mean: {intensity.mean()}")

# Apply a logarithmic scale to the intensity values
intensity_log = np.log1p(intensity)  # log(1 + intensity) to handle values near 0

# Normalize the log-transformed intensity to [0, 1]
intensity_normalized = (intensity_log - intensity_log.min()) / (intensity_log.max() - intensity_log.min() + 1e-8)

# Map normalized intensity values to colors using a rainbow colormap
# Use matplotlib's 'jet' colormap
colormap = cm.get_cmap('plasma')  # You can also try 'viridis' or others
colors = colormap(intensity_normalized)[:, :3]  # Extract RGB values (ignore alpha)

# Create an Open3D PointCloud object
pcd = o3d.geometry.PointCloud()

# Set the points
pcd.points = o3d.utility.Vector3dVector(xyz)

# Assign colors to the points
pcd.colors = o3d.utility.Vector3dVector(colors)

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd],
                                  window_name="Radar Point Cloud with Rainbow Intensity",
                                  width=800,
                                  height=600,
                                  left=50,
                                  top=50,
                                  point_show_normal=False)
