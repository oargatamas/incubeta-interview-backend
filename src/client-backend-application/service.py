import sqlalchemy
from sqlalchemy import select
from repository import connect

connStr =  'mysql+pymysql://incubeta_ads:incubeta_ads@localhost:6446/incubeta_ads?charset=utf8mb4' # Todo move to ENV variable
def get_offers(origin, destination, date_of_departure):
    engine = connect()
    metadata = sqlalchemy.MetaData()
    metadata.reflect(bind=engine)
    fare_prices = metadata.tables["user"]

    #Todo parse origin and destination correctly to involve all columns, Also add the date to the query params
    return select(fare_prices).where(fare_prices.c.org_city_name == origin and fare_prices.c.dst_city_name == destination).all()

