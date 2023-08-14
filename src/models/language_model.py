from .abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db['languages']

    def __init__(self, data):
        super.__init__(self, data)

    def to_dict(self):
        raise NotImplementedError

    @classmethod
    def list_dicts(cls):
        raise NotImplementedError
