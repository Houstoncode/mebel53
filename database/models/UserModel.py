from database.models.BaseModel import BaseModel
from database.schemas.UserSchema import UserSchema, BaseSchema


class UserModel(BaseModel):
    def __init__(self):
        super().__init__()
        BaseSchema.metadata.create_all(self._engine)

    def createUser(self, email, full_name, password):
        if self.findUserByEmail(email) is not None:
            return None

        user = UserSchema(full_name=full_name, email=email, password=password)
        self._session.add(user)
        self._session.commit()

        return user

    def findUserByEmail(self, email):
        return self._session.query(UserSchema).filter(UserSchema.email == email).first()

    def list(self):
        result = []
        for row in self._session.query(UserSchema).all():
            item = dict(row.__dict__)
            item.pop('_sa_instance_state', None)
            result.append(item)
        return result
