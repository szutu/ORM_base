from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


# local database connection initialize
engine = create_engine('sqlite:///C:\\Users\\szutu\\Desktop\\REST_API\\git\\repozytorium1\\stockBase.sqlite')
# to manage tables
base = declarative_base()


class Operations(base):
    __tablename__ = 'operation'

    #konstrukcja tabeli w bazie
    operation_id = Column(Integer, primary_key=True)
    data = Column(String)
    stock_name = Column(String)
    price = Column(Integer)

    def __init__(self, operation_id, data, stock_name, price):
        self.operation_id = operation_id
        self.data = data
        self.stock_name = stock_name
        self.price = price


class Investors(base):
    __tablename__ = 'investors'

    id_investor = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    capital = Column(Integer)

    def __init__(self, id_investor, name, surname, capital):
        self.id_investor = id_investor
        self.name = name
        self.surname = surname
        self.capital = capital


# creation of table
base.metadata.create_all(engine)



