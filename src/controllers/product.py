from src.core import DBConnectionManager
from src.models import ProductModel
from src.schemas import ProductRequest, ProductResponse

class ProductController:
    """
    Controller class for managing product-related operations.

    Attributes:
        db (DBConnectionManager): Database connection manager instance.
    Methods:
        add_product(request: ProductRequest) -> ProductResponse:
            Adds a new product to the database.
        get_products() -> list[ProductResponse]:
            Retrieves all products from the database.
        map_request_to_model(request: ProductRequest) -> ProductModel:
            Maps the request data to the ProductModel.
        map_model_to_response(model: ProductModel) -> ProductResponse:
            Maps the ProductModel to the response object.
    """
    def __init__(self):
        self.db = DBConnectionManager()

    def add_product(self, request: ProductRequest) -> ProductResponse:
        """
        Method to add a new product to the database.

        Args:
            request (ProductRequest): The request object containing product data.
        Returns:
            ProductResponse: The response object containing the added product data.
        """
        with self.db as db_session:
            model = self.map_request_to_model(request)
            model.add(db_session)

            response = self.map_model_to_response(model)

        return response
    
    def get_products(self) -> list[ProductResponse]:
        """
        Method to get all products from the database.

        Returns:
            list[ProductResponse]: A list of response objects containing product data.
        """
        with self.db as db_session:
            products = ProductModel.get(db_session)

            response = [self.map_model_to_response(product) for product in products]

        return response

    @staticmethod
    def map_request_to_model(request: ProductRequest) -> ProductModel:
        """
        Map the request data to the ProductModel.

        Args:
            request (ProductRequest): The request object containing product data.
        Returns:
            ProductModel: The mapped ProductModel object.
        """
        data = request.to_dict()

        model = ProductModel(**data)

        return model

    @staticmethod
    def map_model_to_response(model: ProductModel) -> ProductResponse:
        """
        Map the ProductModel to the response object.

        Args:
            model (ProductModel): The ProductModel object.
        Returns:
            ProductResponse: The mapped ProductResponse object.
        """
        data = model.to_dict()

        response = ProductResponse(**data)

        return response
