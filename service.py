from sqlalchemy.orm import Session, aliased
from database import SessionLocal
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_products(db: Session):

    query = db.query(models.Products)

    Products_all = query.all()
    Products_all = (
        [new_data.to_dict() for new_data in Products_all]
        if Products_all
        else Products_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Products_all": "Products_all"},
    }
    return res


async def post_products(db: Session, raw_data: schemas.PostProducts):
    product: str = raw_data.product
    product_null: str = raw_data.product_null

    record_to_be_added = {"product": product, "product_null": product_null}
    new_Products = models.Products(**record_to_be_added)
    db.add(new_Products)
    db.commit()
    db.refresh(new_Products)
    Products_inserted_record = new_Products.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Products_inserted_record": "Products_inserted_record"},
    }
    return res


async def get_orders_id(db: Session, id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.id == id))

    Orders_one = query.first()

    Orders_one = (
        (Orders_one.to_dict() if hasattr(Orders_one, "to_dict") else vars(Orders_one))
        if Orders_one
        else Orders_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Orders_one": "Orders_one"},
    }
    return res


async def post_orders(db: Session, raw_data: schemas.PostOrders):
    order_name: str = raw_data.order_name
    orders_user_id: int = raw_data.orders_user_id
    order_product_id: int = raw_data.order_product_id

    record_to_be_added = {
        "order_name": order_name,
        "orders_user_id": orders_user_id,
        "order_product_id": order_product_id,
    }
    new_Orders = models.Orders(**record_to_be_added)
    db.add(new_Orders)
    db.commit()
    db.refresh(new_Orders)
    Orders_inserted_record = new_Orders.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Orders_inserted_record": "Orders_inserted_record"},
    }
    return res


async def put_orders_id(db: Session, raw_data: schemas.PutOrdersId):
    id: int = raw_data.id
    order_name: str = raw_data.order_name
    orders_user_id: int = raw_data.orders_user_id
    order_product_id: int = raw_data.order_product_id

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.id == id))
    Orders_edited_record = query.first()

    if Orders_edited_record:
        for key, value in {
            "id": id,
            "order_name": order_name,
            "orders_user_id": orders_user_id,
            "order_product_id": order_product_id,
        }.items():
            setattr(Orders_edited_record, key, value)

        db.commit()
        db.refresh(Orders_edited_record)

        Orders_edited_record = (
            Orders_edited_record.to_dict()
            if hasattr(Orders_edited_record, "to_dict")
            else vars(Orders_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Orders_edited_record": "Orders_edited_record"},
    }
    return res


async def get_orders(db: Session):

    query = db.query(models.Orders)

    Orders_all = query.all()
    Orders_all = (
        [new_data.to_dict() for new_data in Orders_all] if Orders_all else Orders_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Orders_all": "Orders_all"},
    }
    return res


async def delete_orders_id(db: Session, id: int):

    query = db.query(models.Orders)
    query = query.filter(and_(models.Orders.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        Orders_deleted = record_to_delete.to_dict()
    else:
        Orders_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Orders_deleted": "Orders_deleted"},
    }
    return res


async def get_products_id(db: Session, id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.id == id))

    Products_one = query.first()

    Products_one = (
        (
            Products_one.to_dict()
            if hasattr(Products_one, "to_dict")
            else vars(Products_one)
        )
        if Products_one
        else Products_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Products_one": "Products_one"},
    }
    return res


async def put_products_id(db: Session, raw_data: schemas.PutProductsId):
    id: int = raw_data.id
    product: str = raw_data.product
    product_null: str = raw_data.product_null

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.id == id))
    Products_edited_record = query.first()

    if Products_edited_record:
        for key, value in {
            "id": id,
            "product": product,
            "product_null": product_null,
        }.items():
            setattr(Products_edited_record, key, value)

        db.commit()
        db.refresh(Products_edited_record)

        Products_edited_record = (
            Products_edited_record.to_dict()
            if hasattr(Products_edited_record, "to_dict")
            else vars(Products_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Products_edited_record": "Products_edited_record"},
    }
    return res


async def delete_products_id(db: Session, id: int):

    query = db.query(models.Products)
    query = query.filter(and_(models.Products.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        Products_deleted = record_to_delete.to_dict()
    else:
        Products_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Products_deleted": "Products_deleted"},
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    username: str = raw_data.username
    user_null: str = raw_data.user_null

    record_to_be_added = {"username": username, "user_null": user_null}
    new_Users = models.Users(**record_to_be_added)
    db.add(new_Users)
    db.commit()
    db.refresh(new_Users)
    Users_inserted_record = new_Users.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Users_inserted_record": "Users_inserted_record"},
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        Users_deleted = record_to_delete.to_dict()
    else:
        Users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Users_deleted": "Users_deleted"},
    }
    return res


async def post_tablestudents(db: Session, raw_data: schemas.PostTablestudents):
    username: str = raw_data.username
    somenull: str = raw_data.somenull
    price: int = raw_data.price

    record_to_be_added = {"price": price, "somenull": somenull, "username": username}
    new_TableStudents = models.Tablestudents(**record_to_be_added)
    db.add(new_TableStudents)
    db.commit()
    db.refresh(new_TableStudents)
    TableStudents_inserted_record = new_TableStudents.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"TableStudents_inserted_record": "TableStudents_inserted_record"},
    }
    return res


async def delete_tablestudents_id(db: Session, id: int):

    query = db.query(models.Tablestudents)
    query = query.filter(and_(models.Tablestudents.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        TableStudents_deleted = record_to_delete.to_dict()
    else:
        TableStudents_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"TableStudents_deleted": "TableStudents_deleted"},
    }
    return res


async def get_tablestudents(db: Session):

    query = db.query(models.Tablestudents)

    TableStudents_all = query.all()
    TableStudents_all = (
        [new_data.to_dict() for new_data in TableStudents_all]
        if TableStudents_all
        else TableStudents_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"TableStudents_all": "TableStudents_all"},
    }
    return res


async def get_tablestudents_id(db: Session, id: int):

    query = db.query(models.Tablestudents)
    query = query.filter(and_(models.Tablestudents.id == id))

    TableStudents_one = query.first()

    TableStudents_one = (
        (
            TableStudents_one.to_dict()
            if hasattr(TableStudents_one, "to_dict")
            else vars(TableStudents_one)
        )
        if TableStudents_one
        else TableStudents_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"TableStudents_one": "TableStudents_one"},
    }
    return res


async def put_tablestudents_id(db: Session, raw_data: schemas.PutTablestudentsId):
    id: int = raw_data.id
    username: str = raw_data.username
    somenull: str = raw_data.somenull
    price: int = raw_data.price

    query = db.query(models.Tablestudents)
    query = query.filter(and_(models.Tablestudents.id == id))
    TableStudents_edited_record = query.first()

    if TableStudents_edited_record:
        for key, value in {
            "id": id,
            "price": price,
            "somenull": somenull,
            "username": username,
        }.items():
            setattr(TableStudents_edited_record, key, value)

        db.commit()
        db.refresh(TableStudents_edited_record)

        TableStudents_edited_record = (
            TableStudents_edited_record.to_dict()
            if hasattr(TableStudents_edited_record, "to_dict")
            else vars(TableStudents_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"TableStudents_edited_record": "TableStudents_edited_record"},
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    Users_all = query.all()
    Users_all = (
        [new_data.to_dict() for new_data in Users_all] if Users_all else Users_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Users_all": "Users_all"},
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    Users_one = query.first()

    Users_one = (
        (Users_one.to_dict() if hasattr(Users_one, "to_dict") else vars(Users_one))
        if Users_one
        else Users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Users_one": "Users_one"},
    }
    return res


async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id: int = raw_data.id
    username: str = raw_data.username
    user_null: str = raw_data.user_null

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    Users_edited_record = query.first()

    if Users_edited_record:
        for key, value in {
            "id": id,
            "username": username,
            "user_null": user_null,
        }.items():
            setattr(Users_edited_record, key, value)

        db.commit()
        db.refresh(Users_edited_record)

        Users_edited_record = (
            Users_edited_record.to_dict()
            if hasattr(Users_edited_record, "to_dict")
            else vars(Users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"Users_edited_record": "Users_edited_record"},
    }
    return res
