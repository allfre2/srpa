import json
from .dsl import RPAScript
from .exception import *

class DataSource():
    """
        Clase general para representar cualquier fuente de donde puedan venir los datos
        que va a consumir el parser
    """

    def __init__(self):
        self.data = ""

    def readStream(self):
        pass

class FileDataSource(DataSource):
    """
    La fuente de los datos es un archivo
    """

    def __init__(self, fileName):
        super().__init__()
        self.fileName = fileName

    def readStream(self):
        with open(self.fileName, "r") as stream:
            try:
                for line in stream:
                    self.data += line
            except Exception as e:
                raise RPAException(e.message)
        return self.data

class RPAParser():
    """
    Clase general para representar el parser de cualquier RPA,
    independientemente del DSL que se utilice, la fuente del script, etc
    """

    def __init__(self, dataSource = FileDataSource):
        self.dataSource = dataSource

    def parseRPAScript(self):
        self.data = self.dataSource.readStream()

class JsonParser(RPAParser):
    """
    Asume que el texto del FileDataSource estará en formato json y contruye
    un objeto RPAScript a partir del mismo. El objeto construido luego será ejecutado
    por una instancia de RPA.
    """

    def parseRPAScript(self):
        super().parseRPAScript()
        self.jsonObject = json.loads(self.data)
        print(self.jsonObject)
        self.rpaScript = RPAScript()
        self.getNonRequiredFields(self.jsonObject)
        print(self.rpaScript)

    def getNonRequiredFields(self, jsonObject):
        for field in ["name", "info", "author"]:
            if field in self.rpaScript:
                self.rpaScript[field] = jsonObject[field]

