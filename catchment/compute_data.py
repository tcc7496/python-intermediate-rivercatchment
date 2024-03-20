"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views


def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    works out the std for each day.
    """

    ### Problems with code ###
    # Too many things done in the function - reading inputs, doing
    # analysis, producing outputs.
    # File specified to specifically in glob.glob and there is no
    # visibility of that file when running it.
    # map() used for one thing but then a for loop used elsewhere.
    # code is not very readable - no comments.
    
    data = data_source.load_catchment_data() # load_catchment_data() is the INTERFACE
    #data = CSVDataSource(data_dir)

    return compute_standard_deviation_by_data(data)


def compute_standard_deviation_by_data(data):
    """Calcluate the daily standard deviation on potentially mutliple
    data."""
    return pd.concat(map(daily_std, data))


def daily_std(data):
    """Calculate the daily mean of a 2d data array.
    Index must be np.datetime64 compatible format."""
    return data.groupby(data.index.date).std()

def load_catchment_data(data_dir):
    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError('No CSV files found in the data directory')

    return map(models.read_variable_from_csv, data_file_paths)

### Object definitions ###
class CSVDataSource():
    def __init__(self, data_dir):
        self.data_dir = data_dir
    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
        data = map(models.read_variable_from_csv, data_file_paths)
        return list(data)
    
class JSONDataSource():
    def __init__(self, data_dir):
        self.data_dir = data_dir
    def load_catchment_data(self): # same method name as in CSV so we can use it in the same way.
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
    
        data = map(models.read_variable_from_json, data_file_paths)
        return list(data)

