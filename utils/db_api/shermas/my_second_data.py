from sqlalchemy import Column, String, sql

from utils.db_api.db_gino import TimedBaseModel


class SecondDATA(TimedBaseModel):
    __tablename__ = 'my_second_data'
    article = Column(String(100), primary_key=True)
    description = Column(String(100))
    price_eur_without_nds = Column(String(100))
    change_article = Column(String(100))

    query: sql.select
