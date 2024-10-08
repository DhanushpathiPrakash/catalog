from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    description = Column(String, nullable=True)