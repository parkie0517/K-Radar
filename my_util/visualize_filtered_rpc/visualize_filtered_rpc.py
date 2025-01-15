import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d

# Load the radar point cloud data
root_path = "./my_util/visualize_filtered_rpc"
rpc_before = np.load(root_path + '/rpc_before.npy')
rpc_after = np.load(root_path + '/rpc_after.npy')

# Extract x, y, z, and intensity for both datasets
x_before, y_before, z_before, intensity_before = rpc_before[:, 0], rpc_before[:, 1], rpc_before[:, 2], rpc_before[:, 3]
x_after, y_after, z_after, intensity_after = rpc_after[:, 0], rpc_after[:, 1], rpc_after[:, 2], rpc_after[:, 3]

# Create Open3D point clouds
pcd_before = o3d.geometry.PointCloud()
pcd_before.points = o3d.utility.Vector3dVector(np.column_stack((x_before, y_before, z_before)))
pcd_before.colors = o3d.utility.Vector3dVector(plt.cm.viridis(intensity_before / intensity_before.max())[:, :3])

pcd_after = o3d.geometry.PointCloud()
pcd_after.points = o3d.utility.Vector3dVector(np.column_stack((x_after, y_after, z_after)))
pcd_after.colors = o3d.utility.Vector3dVector(plt.cm.viridis(intensity_after / intensity_after.max())[:, :3])

# Visualize the point clouds
o3d.visualization.draw_geometries([pcd_before], window_name='Radar Point Cloud Before Filtering')
o3d.visualization.draw_geometries([pcd_after], window_name='Radar Point Cloud After Filtering')