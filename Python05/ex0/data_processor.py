from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple, Union
#las clases astractas no llevan cuerpo, a diferencia de una normal
#solo llevan un pass pero obliga a cada funcion llevarla y se le poner
#el cuerpo dentro de cada funcion


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: List[str] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
#valida el dato para que sea un int o un float


    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
#pasa el parametro por validate, lanza la excepcion y guarda el dato hecho str

    def output(self) -> Tuple[int, str]:
        temp = self._data.pop(0) #extraigo ultimo valor 
        data = self._count #guarda  valor extraido
        self._count += 1 #suma una al contador
        return (data, temp) #retorna un numero y el str


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(i, (int, float)) for i in data)
        else:
            return isinstance(data, (int, float))

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None: # o podemos usar | en ligar de Union
        if not self.validate(data):
            raise ValueError('Improper numeric data')
        if isinstance(data, list):
            for i in data:
                self._data.append(str(i)) #anadimos el elemento trasformsado en str a la Lista
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(i, str) for i in data)
        else:
            return isinstance(data, str)

    def ingest(self, data: str | List[str]) -> None:
        if not self.validate(data):
            raise ValueError('improper text data')
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
                all(isinstance(k, str)
                    and isinstance(v, str) for k, v in i.items())
                for i in data
            )
        else:
            if isinstance(data, dict):
                valid_keys = all(isinstance(k, str) for k in data.keys())
                valid_value = all(isinstance(v, str) for v in data.values())
                return valid_keys and valid_value
            else:
                return (False)
#toca realizar la comprovacion para una lista de dict y para un dict solo
#se verifica que todas las listan sean dict validos y que cada dict tenga
#valores validos, tanto clave y valor sean str
#y si no es un dict o una list solo un str da un return false

    def ingest(self, data: list[Dict[str, str]] | Dict[str, str]) -> None:
        if not self.validate(data):
            raise ValueError('Invalid log entry')
        if isinstance(data, list):
            for i in data:
                self._data.append(f"{i['log_level']}: {i['log_message']}")
        else:
            self._data.append(f"{data['log_level']}: {data['log_message']}")
#validamos que sean los parametros correctos y vemos, si es una lista
#hacemos un for para recorrer y agreagar al dict cada str
#si no es una lista y es un dict suelto, lo agregamos 


if __name__ == '__main__':
    print('=== Code Nexus - Data Preocessor ===\n')

    print('Testing Numeric Processor...')
    numeric = NumericProcessor()
    num_true = numeric.validate(42)
    print(f" Trying to validate input '42': {num_true}")
    num_false = numeric.validate('Hello')
    print(f" Trying to validate input 'Hello': {num_false}")
    print(" Test inavlid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest('foo')
    except ValueError as e:
        print(f' Got exception: {e}')
    numeric.ingest([1, 2, 3, 4, 5])
    print(' Processing data: [1, 2, 3, 4, 5]')
    print(' Extracting 3 values...')
    key, value = numeric.output()
    print(f' Numeric value {key}: {value}')
    key, value = numeric.output()
    print(f' Numeric value {key}: {value}')
    key, value = numeric.output()
    print(f' Numeric value {key}: {value}\n')

    print('Testing Text Processor...')
    texting = TextProcessor()
    text_false = texting.validate(42)
    print(f" Trying to validate input '42': {text_false}")
    texting.ingest(['Hello', 'Nexus', 'World'])
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    print(' Extracting 1 value...')
    key, value = texting.output()
    print(f' Text value {key}: {value}\n')

    print('Testing Log Processor...')
    log = LogProcessor()
    log_false = log.validate('Hello')
    print(f" Trying to validate input 'Hello': {log_false}")
    log.ingest(
        [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
         {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
         )
    print(
        " Processing data: [{'log_level': 'NOTICE', 'log_message':"
        " 'Connection to server'},"
        "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}] "
        )
    print(' Extracting 2 values...')
    key, value = log.output()
    print(f' log entry {key}: {value}')
    key, value = log.output()
    print(f' log entry {key}: {value}')
