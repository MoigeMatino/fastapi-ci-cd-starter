from uuid import uuid4

from sqlmodel import Field, SQLModel

class ItemBase(SQLModel):
    name: str
    description: str = Field(default=None)
    
class Item(ItemBase, table=True):
    id: str | None = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    
class ItemCreate(ItemBase):
    ...
    
