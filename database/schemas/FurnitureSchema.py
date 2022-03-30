from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

BaseSchema = declarative_base()


class FurnitureSchema(BaseSchema):
    __tablename__ = "furnitures"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)


