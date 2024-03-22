# RiverCatch
![Continuous Integration build in GitHub Actions](https://github.com/tcc7496/python-intermediate-rivercatchment/actions/workflows/main.yml/badge.svg)

RiverCatch is a data management system written in Python that manages measurement data collected in river catchment surveys and campaigns.

## Main features
Here are some key features of Inflam:

- Provide basic statistical analyses of data
- Ability to work on measurement data in Comma-Separated Value (CSV) format
- Generate plots of measurement data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites
RiverCatch requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Pandas](https://pandas.pydata.org/) - makes use of Panda's dataframes
- [GeoPandas](https://geopandas.org/) - makes use of GeoPanda's spatial operations
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run RiverCatch's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - RiverCatch's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Modules

A description of what each module does, and how they link together.

### catchment-analysis

The MVC Controller of the environmental data system. The Controller is responsible for:
- selecting the necessary models and views for the current task
- passing data between catchment/models, catchment/views and catchment/compute_data

### models
Models representing catchment data.

The Model layer is responsible for the 'business logic' part of the software.

Catchment data is held in a Pandas dataframe (2D array) where each column contains
data for a single measurement site, and each row represents a single measurement
time across all sites.

This module contains functions to:
- Read a named variable from a CSV, JSON or XML file, and returns a pandas dataframe containing that variable. Requires "filename" to load and returns 2D array of given variable. Index will be dates and columns will be the individual sites
- Calculate the daily total, mean, maximum or minimum of a 2D data array (Index must be np.datetime64 compatible format)

### views

Contains code for plotting inflammation data

### compute_data

This module contains three classes (CSVDataSource, XMLDataSource and JSONDataSource) for handling CSV, XML and JSON data sources respectively. These classes return a list of CSV, XML and JSON file paths.

There are functions to:
- Get all the measurement data from a CSVDataSource and return the std for each day for each file in the CSVDataSource list.
- Compute the standard deviation of a list of dataframes indexed with daily date values
