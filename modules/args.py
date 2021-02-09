import sys, logging, getopt, os
from urllib.parse import urlparse
from .exception import RPAArgsException, RPAInputFormatNotSupported
from .driver import SUPPORTED_BROWSERS

class RPAArgs():
    """
    Clase que va a representar los argumentos pasados a la herramienta.
    """

    def __init__(self, argv):
        self.argv = argv
        self.options = {}
        self.requiredParams = [ARGS_INPUT]
    
    def getOptions(self):
        self.__parseCLArguments()
        if self.__validateOptions():
            return self.options
        else:
            raise RPAArgsException(ARGS_ERROR_MALFORMED)

    def __validateOptions(self):
        # TODO: Mejor validación de las opciones
        if any(param not in self.options for param in self.requiredParams):
            raise RPAArgsException(ARGS_ERROR_MALFORMED)
        return True

    def __parseCLArguments(self):
        try:
            options, arguments = getopt.getopt(self.argv, "i:b:d:p:h", [
                ARGS_INPUT + "=",
                ARGS_BROWSER + "=",
                ARGS_DRIVER + "=",
                ARGS_DRIVER_PATH + "=",
                ARGS_HELP
            ])
        except getopt.GetoptError:
            raise RPAArgsException(ARGS_ERROR_MALFORMED)

        for option, argument in options:
            if option in ["-i", "--" + ARGS_INPUT]:
                self.options[ARGS_INPUT_TYPE] = self.getInputType(argument)
                self.options[ARGS_INPUT] = argument
            elif option in ["-h", "--" + ARGS_HELP]:
                print(self.usage())
                sys.exit(0)
            elif option in ["-b", "--" + ARGS_BROWSER]:
                self.options[ARGS_BROWSER] = argument
            elif option in ["-d", "--" + ARGS_DRIVER]:
                self.options[ARGS_DRIVER] = argument
            elif option in ["-p", "--" + ARGS_DRIVER_PATH]:
                self.options[ARGS_DRIVER_PATH] = argument

        return self.options
    
    def getInputType(self, arg):
        if self.isUrl(arg):
            return ARGS_INPUT_URL
        else:
            extension = self.getExtension(arg)

            if extension not in ARGS_SUPPORTED_FILE_TYPES:
                raise RPAInputFormatNotSupported("Los archivos ." + str(extension) + " no son soportados")

            return extension

    def isUrl(self, arg):
        try:
            result = urlparse(arg)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
    
    def getExtension(self, arg):
        name, extension = os.path.splitext(arg)
        return extension and extension[1:]

    def usage(self):
        usageMessage = """
            [ srpa ]

                -h, --help
                    Muestra este texto de ayuda
                -i, --input
                    Especifíca la ruta del archivo que contiene el script de automatización (requerido)
                    Tipos de entrada soportados: {0}
                -b, --browser
                    Indica cual navegador se desea utilizar (default chrome)
                    Navegadores soportados: {1}
                -d --driver
                    Indica cual librería se desea usar para manejar la automatización
                    Drivers soportados: {2}
                -p, --path
                    Indica la ruta de los binarios de webdriver
                    Por default se utilizan los encontrados en el PATH
        """

        return usageMessage.format(str(ARGS_SUPPORTED_INPUTS), str(SUPPORTED_BROWSERS), str(ARGS_SUPPORTED_DRIVERS))

#constants
ARGS_HELP = "help"

ARGS_INPUT = "input"
ARGS_INPUT_TYPE = "input_type"
ARGS_INPUT_JSON = "json"
ARGS_INPUT_YAML = "yml"
ARGS_INPUT_URL = "url"

ARGS_SUPPORTED_FILE_TYPES = [ARGS_INPUT_JSON, ARGS_INPUT_YAML]
ARGS_SUPPORTED_INPUTS = ARGS_SUPPORTED_FILE_TYPES

ARGS_BROWSER = "browser"

ARGS_DRIVER = "driver"
ARGS_DRIVER_SELENIUM = "selenium"
ARGS_DRIVER_PATH = "path"
ARGS_SUPPORTED_DRIVERS = [ARGS_DRIVER_SELENIUM]

ARGS_ERROR_MALFORMED = "Los argumentos están mal formados. Usar --help para un texto de ayuda"
ARGS_ERROR_MISSING = "Hay argumentos faltantes"