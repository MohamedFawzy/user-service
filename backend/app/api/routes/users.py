from typing import List
from fastapi import APIRouter, Body, Depends
from sqlalchemy.sql.functions import user
from starlette.status import HTTP_201_CREATED
from app.api.services.users import UserService

from app.models.user import userCreate, UserPublic

router = APIRouter()


@router.get(
    "/", response_model=List[UserPublic], name="users:find-all", status_code=200
)
async def get_all_users(
    user_service: UserService = Depends(UserService),
) -> List[UserPublic]:
    return await user_service.find_all_users()


@router.post(
    "/",
    response_model=UserPublic,
    name="users:create-user",
    status_code=HTTP_201_CREATED,
)
async def create_new_user(
    new_user: userCreate = Body(..., embed=False),
    user_service: UserService = Depends(UserService),
) -> UserPublic:
    created_user = await user_service.create_user(new_user=new_user)
    return created_user
