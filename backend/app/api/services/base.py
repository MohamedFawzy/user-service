from app.db.repositories.base import BaseRepository

from app.db.repositories.base import BaseRepository


class BaseService:
    def __init__(self, repo: BaseRepository) -> None:
        self.repository = repo
