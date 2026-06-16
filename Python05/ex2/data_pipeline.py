from abc import ABC, abstractmethod
import typing
from typing import Protocol
from typing import Any, List, Dict, Tuple

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: List[str] = []
        self._count: int = 0
        self._count_total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        last = self._data.pop(0)
        data = self._count
        self._count += 1
        return (data, last)
    

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(i, (int, float)) for i in data)
        else:
            return isinstance(data, (int, float))
        
    def ingest(self, data: List[int | float] | int | float) -> None:
        if not self.validate(data):
            raise ValueError('Improper numeric data')
        if isinstance(data, list):
            for i in data:
                self._data.append(str(i))
                self._count_total += 1
        else:
            self._data.append(str(data))
            self._count_total += 1

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(i, str) for i in data)
        else:
            return isinstance(data, str)
        
    def ingest(self, data: List[str] | str) -> None:
        if not self.validate(data):
            raise ValueError('Improper text data')
        if isinstance(data, list):
            for i in data:
                self._data.append(i)
                self._count_total += 1
        else:
            self._data.append(data)
            self._count_total += 1

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(i, dict) and
                all(isinstance(k, str)
                    and isinstance(v, str) for k, v in i.items())
                    for i in data
            )
        else:
            if isinstance(data, dict):
                key = all(isinstance(k, str) for k in data.keys())
                value = all(isinstance(v, str) for v in data.values())
                return key and value
            else:
                return False
    
    def ingest(self, data: List[Dict[str, str]] | Dict[str, str]) -> None:
        if not self.validate(data):
            raise ValueError('Improper log data')
        if isinstance(data, list):
            for i in data:
                self._data.append(f"{i['log_level']}: {i['log_message']}")
                self._count_total += 1
        else:
            self._data.append(f"{data['log_level']}: {data['log_message']}")
            self._count_total += 1

class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...
    #los '...' es co o el pass de la clase ABC
    
class CSVPlugin():
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        element_C = [tupla[1] for tupla in data]
        total = ','.join(element_C)
        print('CSV Ouput:')
        print(f'{total}')
    """ 
    aqui use una lista de comprension en lugar de hacer 
    elemets_C = []
    for tupla in data;
    elements.append(tupla[1])

    es lo mismo pero en una sola linea, donde le digo que me de 
    el valor 1 de data, implementado algo nuevo
    creamos una variable total y con join unimos los elementos 
    con una  ',' 
    y hacemos 2 prints uno de la info y otro del valor total 

    """
class JSONPlugin():
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        element_J = [f'"item_{number}": "{valor}"' for number, valor in data]
        total = "{" + ','.join(element_J) + "}"
        print('JSON Output:')
        print(f'{total}')

    """
    aqui usamos otra vez una lista de comprension en lugar de :
    element_J = []
    for number, valor in data:
    elemnt_J.append(f'"item_{numer}": "{valor}"')

    volvemos a unir todo con join, pero JSON necesita "{}" asi que 
    las sumamos al principio y usamos la misma logica que el join de CSV, solo que
    al principio y al final lleva {} y las agregamos con un '+' ya que es un str
    y luego el print descriptivo del Json y el print de la union qye la 
    guardanos en una variable 
    """