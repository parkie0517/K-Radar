import numpy as np

# Load the .npy file
file_path = '/mnt/heejun_ssd/rtnh_wider_1p_1_doppler/1/rdr_sparse_doppler_00033.npy'
data = np.load(file_path)

# Print the shape and type of the data
print(f"Shape of the data: {data.shape}")
print(f"Data type: {data.dtype}")
breakpoint()
# Optionally, print the data itself
print(data[:10])