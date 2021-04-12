from fastapi.param_functions import Depends
from starlette.status import HTTP_409_CONFLICT
from app.api.dependencies.database import get_repository
from app.api.services.base import BaseService
from app.db.repositories.user import UserRepository

from fastapi import HTTPException
from app.models.user import UserInDB, userCreate
from passlib.context import CryptContext
from typing import List


class UserService(BaseService):
    def __init__(
        self, repo: UserRepository = Depends(get_repository(UserRepository))
    ) -> None:
        super().__init__(repo)
        self.pwd_context = CryptContext(schemes=["bcrypt"])

    def hash_password(self, *, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, *, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    async def find_all_users(self) -> List[UserInDB]:
        result = await self.repository.find_all_users()
        print("result", result)
        return result

    async def create_user(self, *, new_user: userCreate) -> UserInDB:

        user_exist = await self.repository.find_exist_user(user_email=new_user.email)

        if user_exist:
            raise HTTPException(
                status_code=HTTP_409_CONFLICT, detail="user already exist"
            )

        new_user.password = self.hash_password(password=new_user.password)

        created_user = await self.repository.create_user(new_user=new_user)
        return created_user

