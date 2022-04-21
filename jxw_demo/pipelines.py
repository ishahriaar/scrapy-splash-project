# Define your item pipelines here

from sqlalchemy.orm import sessionmaker

from jxw_demo.models import StoreResult, create_scrapedata_table, db_connect


class JxwPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates scrapedata table.
        """
        engine = db_connect()
        create_scrapedata_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        session = self.Session()
        instance = session.query(StoreResult).filter_by(**item).one_or_none()
        if instance:
            return instance
        jxw_item = StoreResult(**item)

        try:
            session.add(jxw_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
        
