import numpy as np
import pandas as pd
import sqlalchemy as sa
import dask.dataframe as dd
import dask.array as da
import dask.bag as db

def load_csv_delta():
    con = sa.create_engine('mysql://localhost/db')
    df = dd.read_csv('myfiles.*.csv')