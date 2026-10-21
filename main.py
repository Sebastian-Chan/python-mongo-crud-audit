from config.database import init_db
from views.user_views import user_menu
from views.article_views import article_menu
from views.input_helpers import get_valid_string

def main():
    print("Inicializando conexión con MongoDB e índices...")
    try:
        init_db()
        print("Conexión establecida correctamente.")
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return

    while True:
        print("\n=== SISTEMA DE AUDITORÍA DE INVENTARIO ===")
        print("1. Módulo de Usuarios")
        print("2. Módulo de Artículos")
        print("3. Salir")
        
        opcion = get_valid_string("Seleccione un módulo (1-3): ")
        
        if opcion == "1":
            user_menu()
        elif opcion == "2":
            article_menu()
        elif opcion == "3":
            print("\nSaliendo del sistema. ¡Hasta luego, Maestro!")
            break
        else:
            print("Opción inválida. Seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()