class BaseModel:
    def __init__(self):
        pass


    def to_dict(
        self,
        include: dict = {}, 
        exclude: list = []
    ):
        
        data = self.__dict__

        for key, value in data.items():

            if key in exclude or value is None:
                del data[key]

        data.update(include)

        return data

        
    