from config.database import get_database
from bson.objectid import ObjectId

class ArticleRepository:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.articulos

    def create(self, article_data):
        result = self.collection.insert_one(article_data)
        return str(result.inserted_id)

    def find_by_id(self, article_id):
        try:
            obj_id = ObjectId(article_id)
            article = self.collection.find_one({"_id": obj_id})
            if article:
                article["_id"] = str(article["_id"])
            return article
        except Exception:
            return None

    def get_all(self):
        articles = list(self.collection.find({}))
        for article in articles:
            article["_id"] = str(article["_id"])
        return articles

    def update(self, article_id, update_data):
        try:
            obj_id = ObjectId(article_id)
            result = self.collection.update_one({"_id": obj_id}, {"$set": update_data})
            return result.modified_count > 0
        except Exception:
            return False

    def delete(self, article_id):
        try:
            obj_id = ObjectId(article_id)
            result = self.collection.delete_one({"_id": obj_id})
            return result.deleted_count > 0
        except Exception:
            return False