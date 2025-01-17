"""
This file is used to filter the radar data based on the region of interest (ROI) defined in the configuration file.
"""

import numpy as np





####################################################################################################
####################################################################################################
####################################################################################################





def filter_roi(rpc_before, roi, save_path):

    x_min, y_min, z_min, x_max, y_max, z_max = roi
    
    temp_data = np.load(rpc_before) # shape is (150000, 4)

    temp_data = temp_data[np.where(
        (temp_data[:, 0] > x_min) & (temp_data[:, 0] < x_max) &
        (temp_data[:, 1] > y_min) & (temp_data[:, 1] < y_max) &
        (temp_data[:, 2] > z_min) & (temp_data[:, 2] < z_max))]

    
    np.save(save_path, temp_data) # shape is (64612, 4)
    print(f"Filtered data saved to {save_path}")





####################################################################################################
####################################################################################################
####################################################################################################



# x_min, y_min, z_min, x_max, y_max, z_max
roi = 0.,-16.,-2.,72.,16.,7.6 # this is from cfg_RTNH_wide.yml

rpc_before = './my_util/visualize_filtered_rpc_doppler/rpc_before.npy'
save_path = './my_util/visualize_filtered_rpc_doppler/rpc_after.npy'
filter_roi(rpc_before, roi, save_path)