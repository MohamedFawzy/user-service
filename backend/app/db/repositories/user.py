from sqlalchemy.sql.sqltypes import Boolean
from app.db.repositories.base import BaseRepository
from app.models.user import userCreate, UserInDB


CREATE_USER_QUERY = """
    INSERT INTO users (first_name, last_name, email, password)
    VALUES (:first_name, :last_name, :email, :password)
    RETURNING id, first_name, last_name, email, password;
"""

FIND_EXIST_USER = """
    SELECT email FROM users WHERE email = :email
"""


class UserRepository(BaseRepository):
    """
    All database actions related to user
    """

    async def create_user(self, *, new_user: userCreate) -> UserInDB:
        query_values = new_user.dict()
        user = await self.db.fetch_one(query=CREATE_USER_QUERY, values=query_values)
        return UserInDB(**user)

    async def find_exist_user(self, *, user_email: str) -> Boolean:
        return await self.db.fetch_one(
            query=FIND_EXIST_USER, values={"email": user_email}
        )
