import numpy as np

# Load the .npy file
file_path = '/mnt/heejun_ssd/dataset/1/sparse_cube/cube_00033.npy'
data = np.load(file_path)

# Print the shape and type of the data
print(f"Shape of the data: {data.shape}")
print(f"Data type: {data.dtype}")
# Optionally, print the data itself
print(data[:10])