import sqlalchemy

connStr = 'mysql+pymysql://incubeta_ads:incubeta_ads@localhost:6446/incubeta_ads?charset=utf8mb4'  # Todo move to ENV variable
def connect():
    engine = sqlalchemy.create_engine(connStr)
    engine.connect()
    return engine