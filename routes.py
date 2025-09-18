from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/products/')
async def get_products(db: Session = Depends(get_db)):
    try:
        return await service.get_products(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/products/')
async def post_products(raw_data: schemas.PostProducts, db: Session = Depends(get_db)):
    try:
        return await service.post_products(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/id/')
async def get_orders_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_orders_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/orders/')
async def post_orders(raw_data: schemas.PostOrders, db: Session = Depends(get_db)):
    try:
        return await service.post_orders(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/orders/id/')
async def put_orders_id(raw_data: schemas.PutOrdersId, db: Session = Depends(get_db)):
    try:
        return await service.put_orders_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/orders/')
async def get_orders(db: Session = Depends(get_db)):
    try:
        return await service.get_orders(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/orders/id/')
async def delete_orders_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_orders_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/products/id/')
async def get_products_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_products_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/products/id/')
async def put_products_id(raw_data: schemas.PutProductsId, db: Session = Depends(get_db)):
    try:
        return await service.put_products_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/products/id/')
async def delete_products_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_products_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id/')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tablestudents/')
async def post_tablestudents(raw_data: schemas.PostTablestudents, db: Session = Depends(get_db)):
    try:
        return await service.post_tablestudents(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tablestudents/id/')
async def delete_tablestudents_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_tablestudents_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tablestudents/')
async def get_tablestudents(db: Session = Depends(get_db)):
    try:
        return await service.get_tablestudents(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tablestudents/id/')
async def get_tablestudents_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_tablestudents_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tablestudents/id/')
async def put_tablestudents_id(raw_data: schemas.PutTablestudentsId, db: Session = Depends(get_db)):
    try:
        return await service.put_tablestudents_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id/')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

