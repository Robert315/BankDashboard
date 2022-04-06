from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('mysql+pymysql://admin:AcerNitro5!@localhost:3306/BankDashboard')
