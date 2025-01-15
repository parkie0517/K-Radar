import numpy as np

# Load the .npy file
file_path = '/mnt/heejun_ssd/sparse_radar_tensor_wide_range/rtnh_wider_1p_1/1/sprdr_00033.npy'
data = np.load(file_path)

# Print the shape and type of the data
print(f"Shape of the data: {data.shape}")
print(f"Data type: {data.dtype}")
# Optionally, print the data itself
print(data[:10])