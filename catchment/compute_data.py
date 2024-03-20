"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models #, views

class CSVDataSource:
    """
    Loads all the catchment CSV files within a specified directory.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
        data = map(models.read_variable_from_csv, data_file_paths)
        return list(data)

def daily_std(data):
    return data.groupby(data.index.date).std()

def compute_standard_deviation_by_day(data):
    daily_std_list = map(daily_std, data)

    daily_standard_deviation = pd.concat(daily_std_list)
    return daily_standard_deviation

def analyse_data(data_source):
    data = data_source.load_catchment_data() 
    return compute_standard_deviation_by_day(data)

#def analyse_data(data_dir):
#    """Calculate the standard deviation by day between datasets.
#
#    Gets all the measurement data from the CSV files in the data directory,
#    works out the mean for each day, and then graphs the standard deviation
#    of these means.
#    """
#    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
#    if len(data_file_paths) == 0:
#        raise ValueError('No CSV files found in the data directory')
#    data = map(models.read_variable_from_csv, data_file_paths)
#
#    return compute_standard_deviation_by_day(data)
