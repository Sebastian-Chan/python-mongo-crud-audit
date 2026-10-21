from repositories.user_repository import UserRepository
from datetime import datetime

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, email, nombre, apellido):
        if not email or not nombre or not apellido:
            return {"success": False, "message": "Todos los campos son obligatorios."}
        
        fecha_creado = datetime.now().strftime("%Y-%m-%d")
        
        user_data = {
            "email": email.strip().lower(),
            "nombre": nombre.strip(),
            "apellido": apellido.strip(),
            "fecha_creado": fecha_creado
        }

        user_id = self.repository.create(user_data)
        if not user_id:
            return {"success": False, "message": "El correo electrónico ya está registrado."}
        
        return {"success": True, "message": "Usuario registrado exitosamente.", "id": user_id}

    def get_user(self, email):
        user = self.repository.find_by_email(email.strip().lower())
        if not user:
            return {"success": False, "message": "Usuario no encontrado."}
        return {"success": True, "data": user}

    def list_users(self):
        users = self.repository.get_all()
        return {"success": True, "data": users}

    def update_user(self, email, nombre, apellido):
        email_clean = email.strip().lower()
        update_data = {}
        if nombre:
            update_data["nombre"] = nombre.strip()
        if apellido:
            update_data["apellido"] = apellido.strip()

        if not update_data:
            return {"success": False, "message": "No hay datos para actualizar."}

        updated = self.repository.update(email_clean, update_data)
        if not updated:
            return {"success": False, "message": "No se pudo actualizar el usuario o no existe."}
        return {"success": True, "message": "Usuario actualizado exitosamente."}

    def delete_user(self, email):
        deleted = self.repository.delete(email.strip().lower())
        if not deleted:
            return {"success": False, "message": "El usuario no existe o no pudo eliminarse."}
        return {"success": True, "message": "Usuario eliminado exitosamente."}