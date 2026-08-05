from services.user_service import UserService

class UserModel:
    @classmethod
    def find_by_email(cls, email):
        return UserService.find_by_email(email)

    @classmethod
    def find_by_id(cls, user_id):
        return UserService.find_by_id(user_id)

    @classmethod
    def create(cls, name, email, password, role='customer', permissions=None):
        return UserService.create(name=name, email=email, password=password, role=role, permissions=permissions)

    @classmethod
    def verify_password(cls, user, password):
        return UserService.verify_password(user, password)
