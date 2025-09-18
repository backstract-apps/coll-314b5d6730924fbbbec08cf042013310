from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Orders(BaseModel):
    order_name: str
    orders_user_id: int
    order_product_id: int


class ReadOrders(BaseModel):
    order_name: str
    orders_user_id: int
    order_product_id: int
    class Config:
        from_attributes = True


class Products(BaseModel):
    product: str
    product_null: Optional[str]=None


class ReadProducts(BaseModel):
    product: str
    product_null: Optional[str]=None
    class Config:
        from_attributes = True


class Users(BaseModel):
    username: str
    user_null: Optional[str]=None


class ReadUsers(BaseModel):
    username: str
    user_null: Optional[str]=None
    class Config:
        from_attributes = True


class Tablestudents(BaseModel):
    username: str
    somenull: Optional[str]=None
    price: int


class ReadTablestudents(BaseModel):
    username: str
    somenull: Optional[str]=None
    price: int
    class Config:
        from_attributes = True




class PostProducts(BaseModel):
    product: Optional[str]=None
    product_null: Optional[str]=None

    class Config:
        from_attributes = True



class PostOrders(BaseModel):
    order_name: Optional[str]=None
    orders_user_id: Optional[int]=None
    order_product_id: Optional[int]=None

    class Config:
        from_attributes = True



class PutOrdersId(BaseModel):
    id: Optional[int]=None
    order_name: Optional[str]=None
    orders_user_id: Optional[int]=None
    order_product_id: Optional[int]=None

    class Config:
        from_attributes = True



class PutProductsId(BaseModel):
    id: Optional[int]=None
    product: Optional[str]=None
    product_null: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    username: Optional[str]=None
    user_null: Optional[str]=None

    class Config:
        from_attributes = True



class PostTablestudents(BaseModel):
    username: Optional[str]=None
    somenull: Optional[str]=None
    price: Optional[int]=None

    class Config:
        from_attributes = True



class PutTablestudentsId(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    somenull: Optional[str]=None
    price: Optional[int]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    user_null: Optional[str]=None

    class Config:
        from_attributes = True

