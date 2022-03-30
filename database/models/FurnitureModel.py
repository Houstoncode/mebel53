from database.models.BaseModel import BaseModel
from database.schemas.FurnitureSchema import FurnitureSchema, BaseSchema


class FurnitureModel(BaseModel):
    def __init__(self):
        super().__init__()
        BaseSchema.metadata.create_all(self._engine)

    def list(self):
        result = []
        for row in self._session.query(FurnitureSchema).all():
            item = dict(row.__dict__)
            item.pop('_sa_instance_state', None)
            result.append(item)
        return result
