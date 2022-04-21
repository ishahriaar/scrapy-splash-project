# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.engine.base import Engine
# from sqlalchemy.engine.url import URL
# from sqlalchemy.ext.declarative import declarative_base
# from jxw_demo import settings

# DecBase = declarative_base()

# def db_connect():
#     """
#     Performs database connection using database settings from settings.py.
#     Returns sqlalchemy engine instance
#     """
    
#     print(URL(**settings.DATABASE))
#     return create_engine(URL(**settings.DATABASE))


# def create_scrapedata_table(engine: Engine):
#      DecBase.metadata.create_all(engine)
     

# class StoreResult(DecBase):
#     __tablename__  = "scrapedata"
    
#     name = Column('name', String, primary_key=True)
#     link = Column('link', String)


