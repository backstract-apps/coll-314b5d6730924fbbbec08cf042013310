from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary, text
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Orders(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True, autoincrement=True )
    order_name = Column(String, primary_key=False, autoincrement=True )
    orders_user_id = Column(Integer, primary_key=False )
    order_product_id = Column(Integer, primary_key=False )


class Products(Base):
    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True, autoincrement=True )
    product = Column(String, primary_key=False, autoincrement=True )
    product_null = Column(String, primary_key=False, autoincrement=True )


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, autoincrement=True )
    username = Column(String, primary_key=False, autoincrement=True )
    user_null = Column(String, primary_key=False, autoincrement=True )


class Tablestudents(Base):
    __tablename__ = 'TableStudents'
    id = Column(Integer, primary_key=True, autoincrement=True )
    username = Column(String, primary_key=False, autoincrement=True )
    somenull = Column(String, primary_key=False, autoincrement=True )
    price = Column(Integer, primary_key=False )


