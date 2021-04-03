from databases import Database

"""
Base repository layer
"""


class BaseRepository:
    def __init__(self, db: Database) -> None:
        self.db = db

