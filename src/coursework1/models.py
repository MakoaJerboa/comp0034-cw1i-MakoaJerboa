from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from coursework1 import db

'''
class Total(db.Model):
    __tablename__ = "total"
    total: Mapped[int] = mapped_column(Integer, primary_key=True)
'''
class Total(db.Model):
    __tablename__ = 'total'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    total = mapped_column(Integer, nullable=False)

class Area(db.Model):
    __tablename__ = "area"
    area: Mapped[str] = mapped_column(String, primary_key=True)
    #total: Mapped[int] = mapped_column(ForeignKey("total"))


class Hours(db.Model):
    __tablename__ = "hours"
    hours: Mapped[int] = mapped_column(Integer, primary_key=True)
    #area: Mapped[str] = mapped_column(ForeignKey("area"))
    #total: Mapped[int] = mapped_column(ForeignKey("total"))
    fifteen_or_less: Mapped[int] = mapped_column(Integer, primary_key=True)
    sixteen_to_thirty: Mapped[int] = mapped_column(Integer, primary_key=True)
    thirty_one_to_forty_eight: Mapped[int] = mapped_column(Integer, primary_key=True)
    forty_nine_or_more: Mapped[int] = mapped_column(Integer, primary_key=True)
