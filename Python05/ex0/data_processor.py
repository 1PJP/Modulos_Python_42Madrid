from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple, Union
#las clases astractas no llevan cuerpo, a diferencia de una normal
#solo llevan un pass pero obliga a cada funcion llevarla y se le poner 
#el cuerpo dentro de cada funcion

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
       if isinstance(data, list):
          return all(isinstance(i, (int, float)) for i in data)
       else:
        return isinstance(data, (int, float))
    
    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:# o podemos usar | en ligar de Union
       if not self.validate(data):
          raise ValueError('Improper numeric data')
       if isinstance(data, list):
         for i in data:
            self._data.append(str(i))#anadimos el elemento trasformsado en str a la Lista
       else:
          self._data.append(str(data))

class TextProcessor(DataProcessor):
   def validate(self, data: Any) -> bool:
      if isinstance(data, list):
         return all(isinstance(i , str) for i in data)
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
               all(isinstance(k, str) and 
                   isinstance(v, str) for k, v in i.items()) for 
                   i in data
            )
      else:
         valid_keys = all(isinstance(k, str) for k in data.keys())
         valid_value = all(isinstance(v, str) for v in data.values())
         return valid_keys and valid_value
      #toca realizar la comprovacion para una lista de dict y para un dict solo
      #se verifica que todas las listan sean dict validos y que cada dict tenga 
      #valores validos, tanto clave y valor sean str

   def ingest(self, data: list[dict[str, str]] | dict[str, str]) -> None:
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

