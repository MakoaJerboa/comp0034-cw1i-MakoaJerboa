from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from coursework1 import db

class YR2011(db.Model):
    """
    Represents a model for the year 2011 data.

    Attributes:
        area (str): The name of the area.
        total (int): The total number of workers for that area.
        fifteen_or_less (int): The number of workers working for fifteen or less hours.
        sixteen_to_thirty (int): The number of workers working for sixteen to thirty hours.
        thirty_one_to_forty_eight (int): The number of workers working for thirty one to forty eight hours.
        forty_nine_or_more (int): The number of workers working for forty nine or more hours.
    """
    __tablename__ = 'yr2011'
    area: Mapped[str] = mapped_column(String, primary_key=True)
    total = mapped_column(Integer, nullable=False)
    fifteen_or_less: Mapped[int] = mapped_column(Integer)
    sixteen_to_thirty: Mapped[int] = mapped_column(Integer)
    thirty_one_to_forty_eight: Mapped[int] = mapped_column(Integer)
    forty_nine_or_more: Mapped[int] = mapped_column(Integer)

class YR2021(db.Model):
    """
    Represents a model for the year 2021 data.

    Attributes:
        area (str): The name of the area.
        total (int): The total number of workers for that area.
        fifteen_or_less (int): The number of workers working for fifteen or less hours.
        sixteen_to_thirty (int): The number of workers working for sixteen to thirty hours.
        thirty_one_to_forty_eight (int): The number of workers working for thirty one to forty eight hours.
        forty_nine_or_more (int): The number of workers working for forty nine or more hours.
    """
    __tablename__ = 'yr2021'
    area: Mapped[str] = mapped_column(String, primary_key=True)
    total = mapped_column(Integer, nullable=False)
    fifteen_or_less: Mapped[int] = mapped_column(Integer)
    sixteen_to_thirty: Mapped[int] = mapped_column(Integer)
    thirty_one_to_forty_eight: Mapped[int] = mapped_column(Integer)
    forty_nine_or_more: Mapped[int] = mapped_column(Integer)