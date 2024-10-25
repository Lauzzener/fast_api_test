# domain/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


# Modelo ORM
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)


# Schemas do Pydantic
class ItemCreate(BaseModel):
    name: str
    description: str


class ItemRead(ItemCreate):
    id: int

    class Config:
        orm_mode = True
