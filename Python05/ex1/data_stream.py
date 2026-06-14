from abc import ABC, abstractmethod
import typing
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
                self._count_total += 1
        else:
            self._data.append(f"{data['log_level']}: {data['log_message']}")
            self._count_total += 1

class DataStream:
    def __init__(self) -> None:
        self._processor: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processor.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
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
#aqui anadi un contador extra de de cada ingest para que lleve la cuenta de cuantos procesos lleva

    def print_processor_status(self) -> None:
        if not self._processor:
            print('No processor found, no data\n')
        else:
            for i in self._processor:
                print(f'{type(i).__name__}: total {i._count_total} items processed, remaining {len(i._data)} on processor')


if __name__ == '__main__':
    print('=== Code Nexus - data Stream ===\n')
    print('Initialize Data Stream...')
    print('== DataStream statistics ==')
    
    stream = DataStream()
    stream.print_processor_status()
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    print('Registering Numerc Processor\n')
    info = ['Hello world', [3.14, -1, 2.71],
          [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]
    print(f'Send first batch of data on stream: {info}')
    stream.process_stream(info)
    print('=== DataStream statistics ===')
    stream.print_processor_status()

    print('\nRegistering other data processor')
    text = TextProcessor()
    stream.register_processor(text)
    log = LogProcessor()
    stream.register_processor(log)
    print('Send teh same batch again')
    stream.process_stream(info)
    print('== DataStream statistics ==')
    stream.print_processor_status()

    print('\nConsume some elements from the data processor: Numeric 3, text 2, Log 1')
    key, value = numeric.output()
    key, value = numeric.output()
    key, value = numeric.output()
    key, value = text.output()
    key, value = text.output()
    key, value = log.output()
    print('== DataStream statistics ==')
    stream.print_processor_status()
