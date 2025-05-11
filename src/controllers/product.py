from src.models import ProductModel
from src.schemas import ProductRequest, ProductResponse

class ProductController:
    def __init__(self):
        pass

    def add_product(self, request: ProductRequest) -> ProductResponse:
        pass

    @staticmethod
    def map_request_to_model(request: ProductRequest) -> ProductModel:

        data = request.to_dict()

        ProductModel(**data)

