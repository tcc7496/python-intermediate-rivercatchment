"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models


class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    def load_catchment_data(self):
        """Gets all the measurement data from the CSV files in the data directory"""
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
           raise ValueError('No CSV files found in the data directory')
    
        data = map(models.read_variable_from_csv, data_file_paths)
        return list(data)

class JSONDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    def load_catchment_data(self):
        """Gets all the measurement data from the JSON files in the data directory"""
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
           raise ValueError('No JSON files found in the data directory')
    
        data = map(models.read_variable_from_json, data_file_paths)
        return list(data)

def daily_std(data):
    """Calculate the daily std of a 2d data array.
    Index must be np.datetime64 compatible format."""
    return data.groupby(data.index.date).std()

def compute_standard_deviation_by_day(data):
    """Calculate the standard deviation by day between datasets"""
    daily_std_list = map(daily_std, data)  
    return pd.concat(daily_std_list)

def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    and works out the std for each day
    """
    data = data_source.load_catchment_data()

    return compute_standard_deviation_by_day(data)
