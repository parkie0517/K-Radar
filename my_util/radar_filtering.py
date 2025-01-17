def filter_roi(self, dict_item):

    x_min, y_min, z_min, x_max, y_max, z_max = self.roi.xyz
    list_keys = self.roi.keys
    for temp_key in list_keys:
        if temp_key in ['rdr_sparse', 'ldr64']:
            temp_data = dict_item[temp_key] # temp_data가 포인트 클라우드 데이터임
            temp_data = temp_data[np.where(
                (temp_data[:, 0] > x_min) & (temp_data[:, 0] < x_max) &
                (temp_data[:, 1] > y_min) & (temp_data[:, 1] < y_max) &
                (temp_data[:, 2] > z_min) & (temp_data[:, 2] < z_max))]
            dict_item[temp_key] = temp_data
        # elif temp_key == 'label': # moved to dict item
    
    return dict_item