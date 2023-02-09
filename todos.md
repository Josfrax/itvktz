# Prueba técnica Kuantaz

# ToDos
[x] Crear Tabla Institucion (Nombre,descripción,dirección,fecha de creación)
[x] Crear CRUD para Instituciones
[x] Crear servicios para listar instituciones.
[ ] Crear servicio para listar una institución (Filtró por id) con sus respectivos proyectos y responsable del proyecto.
[ ] Crear servicio para listar instituciones donde a cada institución se agregue a la dirección la ubicación de google maps ejemplo: “https://www.google.com/maps/search/+ direccion ” y la abreviación del nombre (solo los primeros tres caracteres).

[x] Crear Tabla Proyecto (Nombre,descripción,fecha inicio,fecha termino)
[x] Crear servicios para listar proyectos.
[ ] Crear servicio para listar los proyectos que la respuesta sea el nombre del proyecto y los días que faltan para su término. 

[ ] Crear tabla Usuario (Nombre,Apellidos,RUT,fecha de nacimiento,cargo,edad)
[ ] Crear servicios para listar usuarios.
[ ] Crear servicio para listar un usuario (filtro por Rut) con sus respectivos proyectos.

[ ] Crear una Api Rest con Flask y su respectiva base de datos en PostgresSql
[ ] Crear documentación con Swagger.
[ ] Crear archivo Postman u otro.
[ ] Test unitarios
[ ] Crear repositorio con acceso publico.


# Notes
Una institución tiene varios proyectos 
Un proyecto tiene un usuario responsable
Un usuario puede tener más de un proyecto.
Ocupar ORM de preferencia sqlalchemy.

# Source:
- https://docs.google.com/document/d/1OKk3MvPqPiaKcejjpScQXo0iMGA5S8n1mN0r3WfqMwI/edit