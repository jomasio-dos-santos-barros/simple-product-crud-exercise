from datetime import datetime

from src.core import BaseModel


class ProductModel(BaseModel):
    """
    Class to access product table on db

    Attributes:
        id (str)
        name (Str)
        price (float)
        quantity (int)
        created_at (datetime)
        updated_at (datetime)

    Methods:
        add
        get
        update
        delete
    """
    def __init__(
        self,
        id: str,
        name: str,
        price: float,
        quantity: int,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now()
    ):
        if not isinstance(id, str):
            raise TypeError("Invalid ID type")
        if not isinstance(name, str):
            raise TypeError("Invalid NAME type")
        if not isinstance(price, float):
            raise TypeError("Invalid PRICE type")
        if not isinstance(quantity, int):
            raise TypeError("Invalid QUANTITY type")
        if not isinstance(created_at, datetime):
            raise TypeError("Invalid CREATED_AT type")
        if not isinstance(updated_at, datetime):
            raise TypeError("Invalid UPDATED_AT type")

        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.created_at = created_at
        self.updated_at = updated_at


    def add(self):
        return self
    
    def get(self):
        return self
    
    def update(self):
        return self
    
    def delete(self):
        return self