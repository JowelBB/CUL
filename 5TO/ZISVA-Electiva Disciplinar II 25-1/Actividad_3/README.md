# API RESTful con Flask y PyMySQL

Este repositorio contiene una API RESTful desarrollada con Flask y PyMySQL para gestionar productos y categorías.

## Requisitos

* Python 3.x
* Flask
* PyMySQL
* MySQL

## Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/JowelBB/CUL.git
    5TO/ZISVA-Electiva Disciplinar II 25-1/Actividad_3
    ```

2.  **Crea un entorno virtual (opcional pero recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura la base de datos:**

    * Crea una base de datos MySQL llamada `mi_api`.
    * Crea las tablas `productos` y `categorias` usando el siguiente script SQL:

        ```sql
        CREATE DATABASE mi_api;
        USE mi_api;

        CREATE TABLE categorias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL
        );

        CREATE TABLE productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            descripcion TEXT,
            precio DECIMAL(10, 2) NOT NULL,
            categoria_id INT,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        );
        ```

    * Actualiza las credenciales de la base de datos en el archivo `db_config.py`:

        ```python
        db_config = {
            'host': 'localhost',
            'user': 'tu_usuario',
            'password': 'tu_contraseña',
            'database': 'mi_api'
        }
        ```

5.  **Ejecuta la API:**

    ```bash
    python main.py
    ```

## Uso de la API

La API estará disponible en `http://127.0.0.1:5000`.

### Recursos

* `/productos`: Gestiona productos.
* `/categorias`: Gestiona categorías.

### Operaciones CRUD

#### Productos

* **Obtener todos los productos (GET):**

    ```
    GET /productos
    ```

* **Obtener un producto por ID (GET):**

    ```
    GET /productos/<id>
    ```

* **Crear un producto (POST):**

    ```
    POST /productos
    ```

    Cuerpo (JSON):

    ```json
    {
        "nombre": "Nombre del producto",
        "descripcion": "Descripción del producto",
        "precio": 99.99,
        "categoria_id": 1
    }
    ```

* **Actualizar un producto (PUT):**

    ```
    PUT /productos/<id>
    ```

    Cuerpo (JSON):

    ```json
    {
        "nombre": "Nuevo nombre",
        "descripcion": "Nueva descripción",
        "precio": 129.99,
        "categoria_id": 2
    }
    ```

* **Eliminar un producto (DELETE):**

    ```
    DELETE /productos/<id>
    ```

#### Categorías

* **Obtener todas las categorías (GET):**

    ```
    GET /categorias
    ```

* **Obtener una categoría por ID (GET):**

    ```
    GET /categorias/<id>
    ```

* **Crear una categoría (POST):**

    ```
    POST /categorias
    ```

    Cuerpo (JSON):

    ```json
    {
        "nombre": "Nombre de la categoría"
    }
    ```

* **Actualizar una categoría (PUT):**

    ```
    PUT /categorias/<id>
    ```

    Cuerpo (JSON):

    ```json
    {
        "nombre": "Nuevo nombre"
    }
    ```

* **Eliminar una categoría (DELETE):**

    ```
    DELETE /categorias/<id>
    ```

## Pruebas con Postman

1.  Abre Postman.
2.  Crea una nueva solicitud.
3.  Ingresa la URL de la API (por ejemplo, `http://127.0.0.1:5000/productos`).
4.  Selecciona el método HTTP (GET, POST, PUT, DELETE).
5.  Si es necesario, agrega los encabezados (Headers) y el cuerpo (Body) en formato JSON.
6.  Haz clic en "Send" (Enviar).
