from config.database import get_database
from pymongo.errors import DuplicateKeyError

class UserRepository:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.usuarios

    def create(self, user_data):
        try:
            result = self.collection.insert_one(user_data)
            return str(result.inserted_id)
        except DuplicateKeyError:
            return None

    def find_by_email(self, email):
        return self.collection.find_one({"email": email}, {"_id": 0})

    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))

    def update(self, email, update_data):
        result = self.collection.update_one({"email": email}, {"$set": update_data})
        return result.modified_count > 0

    def delete(self, email):
        result = self.collection.delete_one({"email": email})
        return result.deleted_count > 0