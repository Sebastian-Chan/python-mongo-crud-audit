# Sistema de Auditoría de Inventario

Prototipo en consola desarrollado en Python y MongoDB para gestionar y auditar artículos e inventarios, registrando el usuario responsable de la última modificación.

## Organización del Código (Arquitectura por Capas)

El proyecto se divide en módulos independientes para garantizar la separación de responsabilidades:
- **`config/`**: Contiene la configuración inicial de la base de datos y la gestión de conexiones mediante `pymongo`.
- **`repositories/`**: Capa de persistencia. Ejecuta directamente las consultas y operaciones CRUD hacia las colecciones de MongoDB (`usuarios` y `articulos`).
- **`services/`**: Capa de lógica de negocio. Aplica las reglas de validación estricta (nombres no vacíos, integridad referencial de usuarios y control de duplicidad).
- **`views/`**: Capa de presentación. Gestiona la interfaz de consola, submenús interactivos y captura segura de errores de teclado.
- **`main.py`**: Orquestador principal que inicializa el sistema y maneja el flujo general de navegación.

## Justificación del Almacenamiento (MongoDB)
Se seleccionó **MongoDB** por las siguientes ventajas:
- **Flexibilidad de Esquema:** Permite modelar documentos estructurados (`usuarios` y `articulos`) de manera natural mediante diccionarios en Python (JSON/BSON).
- **Escalabilidad y Rendimiento:** Ideal para sistemas de inventarios donde los registros de auditoría y catálogos pueden crecer dinámicamente.
- **Desventaja considerada:** Al ser una base de datos NoSQL orientada a documentos, las relaciones (como la integridad referencial de `usuario_modifico`) deben validarse explícitamente a nivel de la capa de servicio, lo cual se resolvió implementando consultas previas en el flujo de negocio.

## 3. Estrategia de Claves
- **Colección Usuarios (`_id` y `email`):** El campo `email` funciona como clave de negocio natural y única (reforzada con un índice único en MongoDB). Es el identificador principal legible para la auditoría.
- **Colección Artículos (`_id` y `usuario_modifico`):** Cada artículo utiliza un `ObjectId` nativo de MongoDB como clave primaria unívoca. El campo `usuario_modifico` actúa como clave foránea lógica que almacena el `email` de un usuario existente.