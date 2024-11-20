from fastapi import APIRouter, Depends
from app.database import get_db
from sqlmodel import Session
from sqlmodel import Session, func, select
from app.models import Item



router = APIRouter()
@router.get('/')
def get_items(db: Session = Depends(get_db)):
    result = db.exec(select(Item)) 
    items = result.all()
    return items