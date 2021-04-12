# FastAPI User-Service
User Managment service Based On FastAPI and Postgres DB
- User Register
- Update User
- Delete User
- Read Users
- Forget Password
- Active User Uses OTP


### install
- `docker-compose up --build`
- `http://localhost:8000`
-  Update .env.template and rename it to .env
-  Run Migrations
    - `docker ps` then use container ID for user-service
    - login to container uses `docker exec -it {$containerId} /bin/bash`
    - execute the command `alembic upgrade head`
    - users table created.

### TODO
- Update User
- Delete User
- Read Users
- Forget Password
- Active User Uses OTP