# application/services.py
from sqlalchemy.orm import Session
from src.domain.models import ItemCreate, ItemRead
from src.infrastructure.repositories import ItemRepository

class ItemService:
    @staticmethod
    def create_item(db: Session, item: ItemCreate):
        return ItemRepository.create_item(db, item)

    @staticmethod
    def get_item(db: Session, item_id: int):
        return ItemRepository.get_item(db, item_id)

    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 10):
        return ItemRepository.get_items(db, skip, limit)

    @staticmethod
    def delete_item(db: Session, item_id: int):
        return ItemRepository.delete_item(db, item_id)
