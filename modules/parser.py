import json, yaml
from .dsl import *
from .exception import *
from .args import *
import sys, logging

class DataSource():
    """
        Clase general para representar cualquier fuente de donde puedan venir los datos
        que va a consumir el parser
    """

    def __init__(self):
        self.data = ""

    def readStream(self):
        pass

    @staticmethod
    def getDataSource(options):
        if options[ARGS_INPUT_TYPE] in [ARGS_INPUT_JSON, ARGS_INPUT_YAML]:
            return FileDataSource(options[ARGS_INPUT])
        elif options[ARGS_INPUT_TYPE] == ARGS_INPUT_URL:
            return UrlDataSource(options[ARGS_INPUT])
        else:
            raise RPAInputFormatNotSupported("El formato: ." + options[ARGS_INPUT_TYPE] + " no es soportado")

class FileDataSource(DataSource):
    def __init__(self, fileName):
        super().__init__()
        self.fileName = fileName

    def readStream(self):
        try:
            with open(self.fileName, "r") as stream:
                try:
                    for line in stream:
                        self.data += line
                except Exception as e:
                    raise RPAException(e)
            return self.data
        except Exception as e:
            logging.error(e)
            sys.exit(2)

class UrlDataSource(DataSource):
    def __init__(self, url):
        raise NotImplementedError


class RPAParser():
    """
    Clase general para representar el parser de cualquier RPA,
    independientemente del DSL que se utilice, la fuente del script, etc
    """

    def __init__(self, dataSource = FileDataSource):
        self._dataSource = dataSource
        self.rpaScript = RPAScript()

    def parseRPAScript(self):
        self.data = self._dataSource.readStream()
    
    def _setNonRequiredFields(self, script):
        if RPA_NAME in script:
            self.rpaScript.name = script[RPA_NAME]
        if RPA_AUTHOR in script:
            self.rpaScript.author = script[RPA_AUTHOR]
        if RPA_INFO in script:
            self.rpaScript.info = script[RPA_INFO]
    
    def _setVariables(self, script):
        self.rpaScript.variables = script[RPA_VARIABLES]

    def _setParameters(self, script):
        self.rpaScript.paramaters = script[RPA_PARAMETERS]

    def _setScriptBody(self, script):
        self.rpaScript.script = script[RPA_SCRIPT]
    
    def _setRPAScript(self, script):
        self._setNonRequiredFields(script)
        self._setParameters(script)
        self._setVariables(script)
        self._setScriptBody(script)

    @staticmethod
    def getParser(options):
        dataSource = DataSource.getDataSource(options)

        if options[ARGS_INPUT_TYPE] == ARGS_INPUT_JSON:
            return JsonParser(dataSource)
        elif options[ARGS_INPUT_TYPE] == ARGS_INPUT_YAML:
            return YamlParser(dataSource)
        elif options[ARGS_INPUT_TYPE] == ARGS_INPUT_URL:
            return UrlParser(dataSource)
        else:
            raise RPAInputFormatNotSupported("No existe un parser para: " + options[ARGS_INPUT_TYPE])

class JsonParser(RPAParser):
    """
    Asume que el input estará en formato json y contruye
    un objeto RPAScript a partir del mismo.
    """

    def __init__(self, dataSource):
        super().__init__(dataSource)
        self._script = {}

    def parseRPAScript(self):
        super().parseRPAScript()
        self._script = json.loads(self.data)
        self._setRPAScript(self._script)

    def getScript(self):
        return self.rpaScript

class YamlParser(RPAParser):
    """
    Asume que el input estará en formato yaml y contruye
    un objeto RPAScript a partir del mismo.
    """

    def __init__(self, dataSource):
        super().__init__(dataSource)
        self._script = {}

    def parseRPAScript(self):
        super().parseRPAScript()
        self._script = yaml.load(self.data)
        self._setRPAScript(self._script)

    def getScript(self):
        return self.rpaScript

class UrlParser(RPAParser):
    def __init__(self, dataSource):
        raise NotImplementedError