"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models


def daily_std(data):
    """Calculate the daily std of a 2d data array.
    Index must be np.datetime64 compatible format."""
    return data.groupby(data.index.date).std()

def compute_standard_deviation_by_day(data):
    """Calculate the standard deviation by day between datasets"""
    daily_std_list = map(daily_std, data)  
    return pd.concat(daily_std_list)

def load_catchment_data(data_dir):
    """Gets all the measurement data from the CSV files in the data directory"""
    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError('No CSV files found in the data directory')
    
    data = map(models.read_variable_from_csv, data_file_paths)
    return list(data)

def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    and works out the std for each day
    """
    data = load_catchment_data(data_dir)

    return compute_standard_deviation_by_day(data)
