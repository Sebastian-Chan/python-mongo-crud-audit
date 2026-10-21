from repositories.article_repository import ArticleRepository
from repositories.user_repository import UserRepository

class ArticleService:
    def __init__(self):
        self.article_repo = ArticleRepository()
        self.user_repo = UserRepository()

    def create_article(self, nombre, descripcion, marca, usuario_modifico):
        if not nombre or not nombre.strip():
            return {"success": False, "message": "El nombre del artículo no puede estar vacío."}
        
        email_usuario = usuario_modifico.strip().lower()
        user_exists = self.user_repo.find_by_email(email_usuario)
        if not user_exists:
            return {"success": False, "message": "Integridad referencial fallida: El usuario responsable no existe."}

        article_data = {
            "nombre": nombre.strip(),
            "descripcion": descripcion.strip() if descripcion else "",
            "marca": marca.strip() if marca else "",
            "usuario_modifico": email_usuario
        }

        article_id = self.article_repo.create(article_data)
        return {"success": True, "message": "Artículo registrado exitosamente.", "id": article_id}

    def get_article(self, article_id):
        article = self.article_repo.find_by_id(article_id)
        if not article:
            return {"success": False, "message": "Artículo no encontrado o ID inválido."}
        return {"success": True, "data": article}

    def list_articles(self):
        articles = self.article_repo.get_all()
        return {"success": True, "data": articles}

    def update_article(self, article_id, nombre, descripcion, marca, usuario_modifico):
        update_data = {}

        if nombre is not None:
            if not nombre.strip():
                return {"success": False, "message": "El nombre del artículo no puede estar vacío."}
            update_data["nombre"] = nombre.strip()

        if descripcion is not None:
            update_data["descripcion"] = descripcion.strip()

        if marca is not None:
            update_data["marca"] = marca.strip()

        if usuario_modifico is not None:
            email_usuario = usuario_modifico.strip().lower()
            user_exists = self.user_repo.find_by_email(email_usuario)
            if not user_exists:
                return {"success": False, "message": "Integridad referencial fallida: El usuario responsable no existe."}
            update_data["usuario_modifico"] = email_usuario

        if not update_data:
            return {"success": False, "message": "No hay datos para actualizar."}

        updated = self.article_repo.update(article_id, update_data)
        if not updated:
            return {"success": False, "message": "No se pudo actualizar el artículo o ID inválido."}
        return {"success": True, "message": "Artículo actualizado exitosamente."}

    def delete_article(self, article_id):
        deleted = self.article_repo.delete(article_id)
        if not deleted:
            return {"success": False, "message": "El artículo no existe o ID inválido."}
        return {"success": True, "message": "Artículo eliminado exitosamente."}