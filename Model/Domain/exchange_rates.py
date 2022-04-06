from Utils.utils import Base
from sqlalchemy import Column, Integer, DATETIME, Float, CHAR


class ExchangeRates(Base):
    __tablename__ = 'exchange_rates'

    id = Column(Integer, primary_key=True)
    from_currency = Column(CHAR(3))
    to_currency = Column(CHAR(3))
    date_time = DATETIME
    rate = Column(Float)