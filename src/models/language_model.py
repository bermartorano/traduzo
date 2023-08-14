from src.models.abstract_model import AbstractModel
from src.database.db import db


class LanguageModel(AbstractModel):
    _collection = db['languages']

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        raise NotImplementedError

    @classmethod
    def list_dicts(cls):
        raise NotImplementedError
