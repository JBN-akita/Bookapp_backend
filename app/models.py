from sqlalchemy import Column, Integer, String, Date
from datetime import datetime,date
from settings import Base


class Books(Base):
    # テーブル名
    __tablename__ = 'books'

    # 各カラム
    id = Column(Integer, primary_key=True)#主キーがid
    name = Column(String,nullable=False)#nameはnotnull
    publisher = Column(String)#name以外はnull許容
    author = Column(String)
    page_count = Column(Integer)
    published_date = Column(Date)
    price = Column(Integer)

