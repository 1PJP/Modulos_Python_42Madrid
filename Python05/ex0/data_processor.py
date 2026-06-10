from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple, Union

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: List = []
        self._count: int = 0
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
     pass  #valida el dato para que sea un int o un float
    
    @abstractmethod
    def ingest(self, data: Any) -> None:
       pass # pasa el parametro por validate, lanza la excepcion y guarda el dato hecho str
    
    def output(self) -> Tuple[int, str]:
        temp = self._data.pop(0) #saca el dato/numero mas antigupo
        data = self._count      #guarda el numero de orden
        self._count += 1        #suma una al contador 
        return (data, temp) #retorna un numero y el str
    
class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
       if isinstance(data, List):
          return all(isinstance(i, (int, float)) for i in data)
       else:
        return isinstance(data, (int, float))
    
    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:# o podemos usar | en ligar de Union
       if not self.validate(data):
          raise ValueError('Improper numeric data')
       if isinstance(data, List):
         #for i in data:
         self._data.append(str(i) for i in data)#anadimos el elemento trasformsado en str a la Lista
       else:
          self._data.append(str(data))