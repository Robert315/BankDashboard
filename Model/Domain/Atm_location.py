from Utils.utils import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TINYINT, CHAR, VARCHAR


class AtmLocation(Base):
    __tablename__ = "atm_location"

    atm_id = Column(VARCHAR(9))
    adress = Column(VARCHAR(200))
    lat = Column(CHAR(9))
    lng = Column(CHAR(9))
    number_ATMs = TINYINT
