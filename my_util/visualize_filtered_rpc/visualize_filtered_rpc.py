import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the radar point cloud data
root_path = "./my_util/visualize_filtered_rpc"
rpc_before = np.load(root_path + '/rpc_before.npy')
rpc_after = np.load(root_path + '/rpc_after.npy')

# Extract x, y, z, and intensity for both datasets
x_before, y_before, z_before, intensity_before = rpc_before[:, 0], rpc_before[:, 1], rpc_before[:, 2], rpc_before[:, 3]
x_after, y_after, z_after, intensity_after = rpc_after[:, 0], rpc_after[:, 1], rpc_after[:, 2], rpc_after[:, 3]

# Create a figure with two subplots
fig = plt.figure(figsize=(20, 10))

# First subplot for the radar point cloud before filtering
ax1 = fig.add_subplot(121, projection='3d')
scatter1 = ax1.scatter(x_before, y_before, z_before, c=intensity_before, cmap='viridis', s=1)
cbar1 = fig.colorbar(scatter1, ax=ax1, label='Intensity')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Radar Point Cloud Before Filtering')

# Second subplot for the radar point cloud after filtering
ax2 = fig.add_subplot(122, projection='3d')
scatter2 = ax2.scatter(x_after, y_after, z_after, c=intensity_after, cmap='viridis', s=1)
cbar2 = fig.colorbar(scatter2, ax=ax2, label='Intensity')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Radar Point Cloud After Filtering')

plt.show()