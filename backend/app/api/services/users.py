from fastapi.param_functions import Depends
from starlette.status import HTTP_409_CONFLICT
from app.api.dependencies.database import get_repository
from app.api.services.base import BaseService
from app.db.repositories.user import UserRepository

from fastapi import HTTPException
from app.models.user import UserInDB, userCreate


class UserService(BaseService):
    def __init__(
        self, repo: UserRepository = Depends(get_repository(UserRepository))
    ) -> None:
        super().__init__(repo)

    async def create_user(self, *, new_user: userCreate) -> UserInDB:

        user_exist = await self.repository.find_exist_user(user_email=new_user.email)

        if user_exist:
            raise HTTPException(
                status_code=HTTP_409_CONFLICT, detail="user already exist"
            )

        created_user = await self.repository.create_user(new_user=new_user)
        return created_user

