# infrastructure/repositories.py
from sqlalchemy.orm import Session
from src.domain.models import Item, ItemCreate

class ItemRepository:
    @staticmethod
    def create_item(db: Session, item: ItemCreate):
        db_item = Item(name=item.name, description=item.description)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def get_item(db: Session, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()

    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Item).offset(skip).limit(limit).all()

    @staticmethod
    def delete_item(db: Session, item_id: int):
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item:
            db.delete(db_item)
            db.commit()
            return True
        return False
