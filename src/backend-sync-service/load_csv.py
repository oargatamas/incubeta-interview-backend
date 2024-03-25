import dask.dataframe as dd

#connStr =  'mysql+pymysql://incubeta_ads:incubeta_ads@mysql-router/incubeta_ads?charset=utf8mb4'
connStr =  'mysql+pymysql://incubeta_ads:incubeta_ads@localhost:6446/incubeta_ads?charset=utf8mb4'
def load_csv_delta():

    df = dd.read_csv('../../resources/file_2.csv', blocksize=25e6,
                     converters={
                         'lowest_fare_economy_oneway': convertStringToNumber,
                         'lowest_fare_economy_return': convertStringToNumber,
                         'lowest_fare_premium_oneway': convertStringToNumber,
                         'lowest_fare_premium_return': convertStringToNumber,
                     })
    #df['id'] = None
    df.to_sql('fare_prices', connStr, if_exists='append', index=False)


def convertStringToNumber(value):
    if(value == ' '):
        return 0
    return int(value)

load_csv_delta()

