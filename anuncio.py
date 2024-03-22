# Importa la clase ABC y la función abstractmethod del módulo abc
from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

# Definición de la clase Anuncio como clase abstracta
class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str,
            url_clic: str, sub_tipo: str) -> None:
        # Inicializa los atributos del anuncio
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    # Método de propiedad para acceder al ancho
    @property
    def ancho(self) -> int:
        return self.__ancho

    # Método setter para el ancho
    @ancho.setter
    def ancho(self, ancho_nuevo: int) -> None:
        if ancho_nuevo > 0:
            self.__ancho = ancho_nuevo
        else:
            self.__ancho = 1

    # Método de propiedad para acceder al alto
    @property
    def alto(self) -> int:
        return self.__alto

    # Método setter para el alto
    @alto.setter
    def alto(self, alto_nuevo: int) -> None:
        if alto_nuevo > 0:
            self.__alto = alto_nuevo
        else:
            self.__alto = 1

    @property
    def url_archivo(self) -> str:
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url_nuevo: str) -> None:
        self.__url_archivo = url_nuevo

    @property
    def url_clic(self) -> str:
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self, url_nuevo: str) -> None:
        self.__url_clic = url_nuevo

    @property
    def sub_tipo(self) -> str:
        return self.__sub_tipo

    # Método setter para el subtipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str) -> None:
        if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS
        or isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS
        or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError("El sub tipo indicado no está permitido para este formato")
        else:
            self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos() -> None:  # Método estático para mostrar los formatos disponibles
        print("FORMATO VIDEO:")
        print("==============")
        for v in Video.SUB_TIPOS:
            print(f"- {v}")

        print("FORMATO DISPLAY:")
        print("==============")
        for d in Display.SUB_TIPOS:
            print(f"- {d}")

        print("FORMATO SOCIAL:")
        print("==============")
        for s in Social.SUB_TIPOS:
            print(f"- {s}")

    @abstractmethod
    def comprimir_anuncios(self) -> None:  # Método abstracto para comprimir los anuncios
        pass

    @abstractmethod
    def redimensionar_anuncio(self) -> None:  # Método abstracto para redimensionar los anuncios
        pass


class Video(Anuncio):
    SUB_TIPOS = ('instream', 'outstream')

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        # Ancho y alto fijos a 1 para todas las instancias de Video
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion
    
    @property
    def duracion(self) -> int:
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion_nueva: int) -> None:
        if duracion_nueva > 0:
            self.__duracion = duracion_nueva
        else:
            self.__duracion = 5

    def comprimir_anuncios(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    SUB_TIPOS = ('tradicional', 'native')

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    SUB_TIPOS = ('facebook', 'linkedin')

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
