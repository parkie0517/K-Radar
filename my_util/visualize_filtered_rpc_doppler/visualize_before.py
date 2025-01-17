import numpy as np
import open3d as o3d
from matplotlib import cm

# Load the radar point cloud data
root_path = "./my_util/visualize_filtered_rpc_doppler"
rpc_before = np.load(root_path + '/rpc_before.npy')

# Extract x, y, z coordinates and doppler
xyz = rpc_before[:, :3]
doppler = rpc_before[:, 3]

# Print doppler stats for debugging
print("doppler Stats:")
print(f"Min: {doppler.min()}, Max: {doppler.max()}, Mean: {doppler.mean()}")

# Shift doppler values to make them positive
doppler_shifted = doppler - doppler.min() + 1e-8  # Ensure all values are > 0

# Apply a logarithmic scale to the shifted doppler values
doppler_log = np.log1p(doppler_shifted)  # log(1 + shifted doppler)

# Normalize the log-transformed doppler to [0, 1]
doppler_normalized = (doppler_log - doppler_log.min()) / (doppler_log.max() - doppler_log.min() + 1e-8)


# Map normalized doppler values to colors using a rainbow colormap
colormap = cm.get_cmap('plasma')  # You can also try 'viridis' or others
colors = colormap(doppler_normalized)[:, :3]  # Extract RGB values (ignore alpha)

# Create an Open3D PointCloud object
pcd = o3d.geometry.PointCloud()

# Set the points
pcd.points = o3d.utility.Vector3dVector(xyz)

# Assign colors to the points
pcd.colors = o3d.utility.Vector3dVector(colors)

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd],
                                  window_name="Radar Point Cloud with Rainbow doppler",
                                  width=800,
                                  height=600,
                                  left=50,
                                  top=50,
                                  point_show_normal=False)
