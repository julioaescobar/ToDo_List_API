Docker:
- To pull the image of the official postgresql use: docker pull postgres
- To run the image of the official postgresql use: docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=password -d postgres


3. Asociar la tabla de TODOS con la de Users
4. Modificar consultas de TODOS,BATCH e ITEMS para que consideren el usuario
5. Permitir actualizar contraseña
7. refactorizar