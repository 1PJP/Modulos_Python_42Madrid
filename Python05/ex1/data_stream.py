from abc import ABC, abstractmethod
from typing import Any, List, Dict, Tuple

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: List[str] = []
        self._count: int = 0

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
        else:
            self._data.append(str(data))

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
        else:
            self._data.append(data)

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(i, dict) and
                all(isinstance(k, str) and isinstance(v, str)
                     for k, v in i.items())
                for i in data
                          )
        else:
            if isinstance(data, dict):
                key_ok = all(isinstance(k, str) for k in data.keys())
                value_ok = all(isinstance(v, str) for v in data.values())
                return key_ok and value_ok
            else:
                return False
    def ingest(self, data: List[Dict[str, str]] | Dict[str, str]) -> None:
        if not self.validate(data):
            raise ValueError('Improper log data')
        if isinstance(data, list):
            for i in data:
                self._data.append(f"{i['log_level']}: {i['log_message']}")
        else:
            self._data.append(f"{data['log_level']}: {data['log_message']}")

class DataStream(DataProcessor):
    def __init__(self) -> None:
        self._processor: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            for i in self._processor:
                if i.validate(data):
                    i.ingest(data)
                    break
            else:
                print(f'DataStream error - Can`t process element in stream: {data}')
#el For data, recorre cada elemento del stream, uno por uno dato tras dato
#el for i (for i  para ese dato, prueba cada procesador registrado
#el if  pregunta este procesador puede manejar este dato
#el ingest dice si puede y lo procesa
#el break sale del bucle de procesadores por que ya encontró el correcto, y vuelve al for data para el siguiente dato
#el else del for dice que si ninguno puede procesar el dato imprima error

