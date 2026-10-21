from services.article_service import ArticleService
from views.input_helpers import get_valid_string, get_optional_string

def article_menu():
    service = ArticleService()
    
    while True:
        print("\n--- MÓDULO DE ARTÍCULOS ---")
        print("1. Registrar Artículo")
        print("2. Consultar Artículo por ID")
        print("3. Listar Todos los Artículos")
        print("4. Actualizar Artículo")
        print("5. Eliminar Artículo")
        print("6. Volver al Menú Principal")
        
        opcion = get_valid_string("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            print("\n-- Registrar Artículo --")
            nombre = get_valid_string("Nombre del artículo: ")
            descripcion = get_optional_string("Descripción: ")
            marca = get_optional_string("Marca: ")
            usuario_modifico = get_valid_string("Email del usuario responsable (auditoría): ")
            
            res = service.create_article(nombre, descripcion, marca, usuario_modifico)
            print(res["message"])
            
        elif opcion == "2":
            print("\n-- Consultar Artículo --")
            art_id = get_valid_string("ID del artículo: ")
            res = service.get_article(art_id)
            if res["success"]:
                a = res["data"]
                print(f"\nID: {a['_id']} | Nombre: {a['nombre']} | Marca: {a['marca']} | Desc: {a['descripcion']} | Modificado por: {a['usuario_modifico']}")
            else:
                print(res["message"])
                
        elif opcion == "3":
            print("\n-- Lista de Artículos --")
            res = service.list_articles()
            if res["data"]:
                for a in res["data"]:
                    print(f"- ID: {a['_id']} | {a['nombre']} ({a['marca']}) | Modificado por: {a['usuario_modifico']}")
            else:
                print("No hay artículos registrados.")
                
        elif opcion == "4":
            print("\n-- Actualizar Artículo --")
            art_id = get_valid_string("ID del artículo a actualizar: ")
            nombre = get_optional_string("Nuevo nombre (en blanco para omitir): ")
            descripcion = get_optional_string("Nueva descripción (en blanco para omitir): ")
            marca = get_optional_string("Nueva marca (en blanco para omitir): ")
            usuario_modifico = get_optional_string("Nuevo email de usuario responsable (en blanco para omitir): ")
            
            res = service.update_article(
                art_id,
                nombre if nombre else None,
                descripcion if descripcion else None,
                marca if marca else None,
                usuario_modifico if usuario_modifico else None
            )
            print(res["message"])
            
        elif opcion == "5":
            print("\n-- Eliminar Artículo --")
            art_id = get_valid_string("ID del artículo a eliminar: ")
            confirmar = get_valid_string("¿Confirma eliminar este artículo? (s/n): ").lower()
            if confirmar == 's':
                res = service.delete_article(art_id)
                print(res["message"])
            else:
                print("Eliminación cancelada.")
                
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Elija un número entre 1 y 6.")