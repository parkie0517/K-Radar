import numpy as np





####################################################################################################
####################################################################################################
####################################################################################################





def filter_roi(self, dict_item):

    x_min, y_min, z_min, x_max, y_max, z_max = roi
    temp_data = 

    temp_data = dict_item[temp_key] # temp_data가 포인트 클라우드 데이터임
    temp_data = temp_data[np.where(
        (temp_data[:, 0] > x_min) & (temp_data[:, 0] < x_max) &
        (temp_data[:, 1] > y_min) & (temp_data[:, 1] < y_max) &
        (temp_data[:, 2] > z_min) & (temp_data[:, 2] < z_max))]
    dict_item[temp_key] = temp_data
    
    return dict_item





####################################################################################################
####################################################################################################
####################################################################################################



# x_min, y_min, z_min, x_max, y_max, z_max
roi = 0.,-16.,-2.,72.,16.,7.6 # this is from cfg_RTNH_wide.yml

rpc_before = np.load('./KRadar/my_util/visualize_filtered_rpc-doppler/rpc_before.npy')

