from fastapi import APIRouter, Depends
from app.database import get_db
from sqlmodel import Session
from sqlmodel import Session, func, select
from app.models import Item



router = APIRouter()
memory_items = [
    {
        'id': 1,
        'name': 'Item 1',
        'description': 'Item 1 description'
        
    },
    {
        'id': 2,
        'name': 'Item 2',
        'description': 'Item 2 description'        
    }
]
@router.get('/')
def get_items(db: Session = Depends(get_db)):
    for item in memory_items:
        db.add(Item(**item))
        db.commit()
    result = db.exec(select(Item)) 
    items = result.all()
    return items