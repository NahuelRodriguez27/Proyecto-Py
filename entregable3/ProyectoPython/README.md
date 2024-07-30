## Instalación

1. Clona el repositorio:
    bash
    git clone <URL del repositorio>
    cd myproject
    

2. Instala las dependencias:
    bash
    pip install -r requirements.txt
    

3. Realiza las migraciones de la base de datos:
    bash
    python manage.py migrate
    

4. Ejecuta el servidor:
    bash
    python manage.py runserver
    

## Funcionalidades

- **Crear Autor**: [http://localhost:8000/create_author/](http://localhost:8000/create_author/)
- **Crear Libro**: [http://localhost:8000/create_book/](http://localhost:8000/create_book/)
- **Crear Editorial**: [http://localhost:8000/create_publisher/](http://localhost:8000/create_publisher/)
- **Buscar Libro**: [http://localhost:8000/search/](http://localhost:8000/search/)

## Orden de Prueba

1. Crear un autor.
2. Crear un libro asociado a ese autor.
3. Crear una editorial y asociar libros a la editorial.
4. Buscar un libro por su título.

-Nahuel Rodriguez
