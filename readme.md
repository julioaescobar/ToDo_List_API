Docker:
- To pull the image of the official postgresql use: docker pull postgres
- To run the image of the official postgresql use: docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=password -d postgres


TODO:
0. Mover y mejorar lógica
1. Autenticación
2. Separar Schemas
3. Migración
4. Subir archivo
5. Handling errors
6. Background Tasks
7. Testing
8. Additional status codes
9. Middleware