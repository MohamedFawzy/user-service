from typing import List
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED
from app.api.services.users import UserService

from app.models.user import userCreate, UserPublic

router = APIRouter()


@router.get("/")
async def get_all_users() -> List[dict]:
    users = [{"id": 1, "name": "mohamed", "email": "mfawzy22@gmail.com"}]

    return users


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
