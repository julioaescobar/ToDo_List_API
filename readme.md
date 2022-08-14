Docker:
- To pull the image of the official postgresql use: docker pull postgres
- To run the image of the official postgresql use: docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=password -d postgres


1. Utilizar Depends para la autenticación
2. Solicitar autenticación para las demás rutas
3. Asociar la tabla de TODOS con la de Users
4. Filtrar consultas de TODOS e ITEMS con el usuario
5. Permitir actualizar contraseña
6. Crear módulo de roles
