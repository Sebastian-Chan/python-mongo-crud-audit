from services.user_service import UserService
from views.input_helpers import get_valid_string, get_optional_string

def user_menu():
    service = UserService()
    
    while True:
        print("\n--- MÓDULO DE USUARIOS ---")
        print("1. Registrar Usuario")
        print("2. Consultar Usuario por Email")
        print("3. Listar Todos los Usuarios")
        print("4. Actualizar Usuario")
        print("5. Eliminar Usuario")
        print("6. Volver al Menú Principal")
        
        opcion = get_valid_string("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            print("\n-- Registrar Usuario --")
            email = get_valid_string("Email: ")
            nombre = get_valid_string("Nombre: ")
            apellido = get_valid_string("Apellido: ")
            
            res = service.create_user(email, nombre, apellido)
            print(res["message"])
            
        elif opcion == "2":
            print("\n-- Consultar Usuario --")
            email = get_valid_string("Email del usuario: ")
            res = service.get_user(email)
            if res["success"]:
                u = res["data"]
                print(f"\nEmail: {u['email']} | Nombre: {u['nombre']} {u['apellido']} | Creado: {u['fecha_creado']}")
            else:
                print(res["message"])
                
        elif opcion == "3":
            print("\n-- Lista de Usuarios --")
            res = service.list_users()
            if res["data"]:
                for u in res["data"]:
                    print(f"- {u['email']} | {u['nombre']} {u['apellido']} | {u['fecha_creado']}")
            else:
                print("No hay usuarios registrados.")
                
        elif opcion == "4":
            print("\n-- Actualizar Usuario --")
            email = get_valid_string("Email del usuario a actualizar: ")
            nombre = get_optional_string("Nuevo nombre (dejar en blanco para no cambiar): ")
            apellido = get_optional_string("Nuevo apellido (dejar en blanco para no cambiar): ")
            
            res = service.update_user(email, nombre if nombre else None, apellido if apellido else None)
            print(res["message"])
            
        elif opcion == "5":
            print("\n-- Eliminar Usuario --")
            email = get_valid_string("Email del usuario a eliminar: ")
            confirmar = get_valid_string(f"¿Confirma eliminar a {email}? (s/n): ").lower()
            if confirmar == 's':
                res = service.delete_user(email)
                print(res["message"])
            else:
                print("Eliminación cancelada.")
                
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Elija un número entre 1 y 6.")