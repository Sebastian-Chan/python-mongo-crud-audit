def get_valid_string(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("El campo no puede estar vacío. Intente de nuevo.")
                continue
            return value
        except (KeyboardInterrupt, EOFError):
            print("\nOperación cancelada.")
            return None

def get_optional_string(prompt):
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        return ""