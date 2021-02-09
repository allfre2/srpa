from .dsl import *
from .args import *
from .parser import RPAParser
from .exception import RPADriverNotSupported
from .driver import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class RPA():
    """
    Clase encargada de interpretar, validar y ejecutar los comandos del 'DSL'
    """

    def __init__(self, script, driver):
        self.script = script
        self.delay = 0
        self.driver = driver

    def exec(self):
        for instruction in self.script:

            op = self.parseOp(instruction)

            if op[0] == RPA_DELAY:
                self.driver.setDelay(op[1])
            elif op[0] == RPA_GET:
                self.driver.get(op[1])
            elif op[0] == RPA_SELECT:
                self.driver.selectBy(op[1], op[2])
            elif op[0] == RPA_WAIT:
                self.driver.wait(op[1])
            elif op[0] == RPA_INPUT:
                self.driver.input(op[1])
            elif op[0] == RPA_INPUT_RETURN:
                self.driver.input_return()
            elif op[0] == RPA_CLICK:
                self.driver.click()
            elif op[0] == RPA_CLOSE:
                self.driver.close()
            else:
                raise RPAInvalidInstruction("La instrucción: " + str(op[0]) + " no es soportada.")
        
    def parseOp(self, op):
        """
        TODO: Check the types of the arguments too
        """

        opcode = op[0]
        parsedOp = [opcode]
        args = op[1:]
        if opcode not in RPA_INSTRUCTIONS:
            raise RPAInvalidInstruction("La instrucción: " + str(opcode) + " no es soportada")
        elif len(args) != len(RPA_INSTRUCTIONS[opcode]):
            raise RPAInvalidInstruction("La instrucción: " + str(opcode) + " toma exactamente " + str(len(RPA_INSTRUCTIONS[opcode])) + " parámetros")
        else:
            for arg in args:
                if isinstance(arg, str) and arg[:1] == "$":
                    varName = arg[1:]
                    if varName not in self.script.variables:
                        raise RPAInvalidInstruction("La variable " + str(arg) + " no está definida")
                    else:
                        parsedOp.append(self.script.variables[varName])
                else:
                    parsedOp.append(arg)
        return parsedOp

    @staticmethod
    def getRPA(options):
        print(options)
        parser = RPAParser.getParser(options)
        parser.parseRPAScript()

        driverArgs = [options[ARGS_BROWSER] if ARGS_BROWSER in options else CHROME]
        if ARGS_DRIVER_PATH in options:
            driverArgs.append(options[ARGS_DRIVER_PATH])

        if ARGS_DRIVER not in options or options[ARGS_DRIVER] == ARGS_DRIVER_SELENIUM:
            rpa = SeleniumRPA(parser.getScript())
            rpa.driver.setup(*driverArgs)
            return rpa
        else:
            raise RPADriverNotSupported("El driver: " + str(options[ARGS_DRIVER]) + " no es soportado")

class SeleniumRPA(RPA):
    def __init__(self, script, driver = SeleniumWebDriver()):
        super().__init__(script, driver)
