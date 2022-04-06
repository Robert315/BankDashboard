
from Utils.utils import Base
from sqlalchemy import Column, CHAR


class Currency(Base):
    __tablename__ = 'currency'

    currency = Column(CHAR(3))
