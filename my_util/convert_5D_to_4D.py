"""
This file is used to convert 5D radar point cloud data to 4D radar point cloud data.
[x, y, z, intensity, doppler] -> [x, y, z, dpopler]
"""

import numpy as np

def convert_5D_to_4D(input_file, output_file):
    # Load the 5D radar point cloud data
    radar_data_5D = np.load(input_file) # shape is (150000, 5)
    
    # Check if the input data has 5 columns
    if radar_data_5D.shape[1] != 5:
        raise ValueError("Input data must have 5 columns: [x, y, z, intensity, doppler]")
    
    # Extract x, y, z, and doppler (skip intensity)
    radar_data_4D = radar_data_5D[:, [0, 1, 2, 4]] # shape is (150000, 4)
    
    # Save the 4D radar point cloud data
    np.save(output_file, radar_data_4D)
    print(f"Converted 5D data to 4D and saved to {output_file}")

# Example usage
input_file = '/mnt/heejun_ssd/rtnh_wider_1p_1_doppler/13/rdr_sparse_doppler_00069.npy'
output_file = './my_util/visualize_filtered_rpc_doppler/rpc_before.npy'
convert_5D_to_4D(input_file, output_file)