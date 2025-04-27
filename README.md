# HSC

1. Activar entorno
2. Inicializar servidor
3. Abrir ARC

Operaciones en API: 

VER
    GET http://127.0.0.1:8000/api/categorias/

    Sin body



CREAR
    POST http://127.0.0.1:8000/api/categorias/

    body -> raw -> json

    {
    "nombreCat": "Nueva Categoria"
    }





BORRAR
    DELETE http://127.0.0.1:8000/api/categorias/2/ (idCategoria)

    Sin body





Actualizar 
    PUT http://127.0.0.1:8000/api/categorias/2/ (idCategoria)

    body -> raw -> json

    {
    "nombreCat": "Nuevo nombre"
    }


