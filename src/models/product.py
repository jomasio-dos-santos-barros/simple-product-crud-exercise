from datetime import datetime
from sqlite3 import Connection

from src.core import BaseModel, id_generator


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
        add(db_session)
        get(db_session, product_id)
        update(db_session)
        delete(db_session, product_id)
    """
    def __init__(
        self,
        name: str,
        price: float,
        quantity: int,
        id: str = id_generator(),
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


    
    def add(self, db_session: Connection) -> "ProductModel":
        """
        Add a new product to the database

        Args:
            db_session (Connection): Database connection

        Returns:
            ProductModel: The created product
        """
        # Implementation for adding a product to the database
        cursor = db_session.cursor()
        cursor.execute(
            """
            INSERT INTO products (id, name, price, quantity, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (self.id, self.name, self.price, self.quantity, self.created_at, self.updated_at)
        )
        return self
    
    @staticmethod
    def get(db_session: Connection, product_id: str | None = None) -> "ProductModel":
        """
        Get a product from the database
        Args:
            db_session (Connection): Database connection
            product_id (str | None): Product ID to fetch. If None, fetch all products.
        Returns:
            ProductModel | list[ProductModel] | None: The fetched product or list of products
        """
        cursor = db_session.cursor()
        if product_id is None:
            cursor.execute("SELECT * FROM product")
            rows = cursor.fetchall()
            return [
                ProductModel(
                    id=row[0],
                    name=row[1],
                    price=row[2],
                    quantity=row[3],
                    created_at=datetime.fromisoformat(row[4]),
                    updated_at=datetime.fromisoformat(row[5])
                )
                for row in rows
            ]
        else:
            cursor.execute("SELECT * FROM product WHERE id = ?", (product_id,))
            row = cursor.fetchone()
            if row:
                return ProductModel(
                    id=row[0],
                    name=row[1],
                    price=row[2],
                    quantity=row[3],
                    created_at=datetime.fromisoformat(row[4]),
                    updated_at=datetime.fromisoformat(row[5])
                )
            return None
    
    def update(self, db_session: Connection) -> "ProductModel":
        """
        Update a product in the database

        Args:
            db_session (Connection): Database connection
        Returns:
            ProductModel: The updated product
        """
        cursor = db_session.cursor()
        cursor.execute(
            """
            UPDATE products
            SET name = ?, price = ?, quantity = ?, updated_at = ?
            WHERE id = ?
            """,
            (self.name, self.price, self.quantity, datetime.now(), self.id)
        )
        db_session.commit()
        return self
    
    @staticmethod
    def delete(db_session: Connection, product_id: str) -> bool:
        """
        Delete a product from the database
        Args:
            db_session (Connection): Database connection
            product_id (str): Product ID to delete
        Returns:
            bool: True if the product was deleted, False otherwise
        """
        cursor = db_session.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        db_session.commit()
        
        return cursor.rowcount > 0