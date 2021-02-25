from abc import ABCMeta, abstractmethod
from typing import List

from common.database import Database


class Model(metaclass=ABCMeta):   
    @classmethod
    def all(cls) -> List:
        return [cls(**elem) for elem in Database.find(cls.collection, {})]

    @abstractmethod
    def json(self):
        raise NotImplementedError
