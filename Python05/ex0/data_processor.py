from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self):
        self._data: list = []
        self._count: int = 0
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
     pass
    
    @abstractmethod
    def ingest(self, data: Any) -> None:
       pass

    def output(self) -> tuple:
        temp = self._data.pop(0)
        data = self._count
        self._count += 1
        return (data, temp)
    
class NumericProcessor(DataProcessor):
    def validate(self, data):
       if isinstance(data, list):
          all(isinstance(i, (int, float)) for i in data)
       else:
        return isinstance(data, (int, float))
    