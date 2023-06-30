from sqlalchemy import Column, String, sql

from utils.db_api.db_gino import TimedBaseModel


# class Hehehe (TimedBaseModel):
#     __tablename__ = 'my_data_nnnnn'
#     type_o = Column(String(100))
#     product_group = Column(String(100))
#     availability_of_comp = Column(String(100))
#     new_article = Column(String(100), primary_key=True)
#     old_article = Column(String(100))
#     name = Column(String(100))
#     price_in_euro = Column(String(100))
#     price_in_rub = Column(String(100))
#     discount_group = Column(String(100))
#     ean_upc_code = Column(String(100))
#     net_weight_kg = Column(String(100))
#     gross_weight_kg = Column(String(100))
#     length_excluding_packaging_mm = Column(String(100))
#     width_excluding_packaging_mm = Column(String(100))
#     height_without_packaging_mm = Column(String(100))
#     approximate_delivery_time = Column(String(100))
#     group = Column(String(100))
#
#     query: sql.select