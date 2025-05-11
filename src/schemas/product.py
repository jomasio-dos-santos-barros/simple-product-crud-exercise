from dataclasses import dataclass, Field
from datetime import datetime

from src.core import BaseModel


@dataclass
class ProductBase(BaseModel):
    """
    Base product class

    Attributes:
        name (str) product name
        price (float) product price
        quantity (int) product quantity
    """
    name: str
    price: float
    quantity: int


@dataclass
class ProductRequest(ProductBase):
    """
    Class to create a product

    Attributes:
        name (str) product name
        price (float) product price
        quantity (int) product quantity
    """
    pass

@dataclass
class ProductUpdate(BaseModel):
    """
    Class to update a product

    Attributes:
        name: str | None = None
        price: float | None = None
        quantity: int | None = None
    """
    name: str | None = None
    price: float | None = None
    quantity: int | None = None

@dataclass
class ProductResponse(ProductBase):
    """
    Class with full product data

    Attributes:
        id (str) product id
        name (str) product name
        price (float) product price
        quantity (int) product quantity on db
        created_at (datetime) product create datetime
        updated_at (datetime) product update datetime
    """
    id: str
    created_at: datetime
    updated_at: datetime