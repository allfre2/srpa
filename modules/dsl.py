class RPAScript():
    """
    Clase que representa un Script de automatización que será ejecutado por
    una instancia de RPA.
    """

    def __init__(self):
        self.name = ""
        self.info = ""
        self.author = ""
        self.current = 0
        self.script = []
        self.paramaters = {}
        self.variables = {}
        self.browser = ""
        self.delay = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= len(self.script):
            raise StopIteration
        else:
            self.current += 1
            return self.script[self.current - 1]
    
    def __str__(self):
        return "Script: " + self.name + "\nBy: " + self.author + "\n" + "Instructions: " + str(self.script) + "\n" + str(self.paramaters) + "\n" + str(self.variables)

# Constants
RPA_NAME = "name"
RPA_AUTHOR = "author"
RPA_INFO = "info"

RPA_PARAMETERS = "parameters"
RPA_VARIABLES = "variables"

RPA_SCRIPT = "script"
RPA_BROWSER = "browser"

RPA_NON_ESSENTIAL_FIELDS = [RPA_NAME, RPA_AUTHOR, RPA_INFO]

#Instructions
RPA_GET = "get"
RPA_INPUT = "input"
RPA_INPUT_RETURN = "return"
RPA_DELAY = "delay"
RPA_WAIT = "wait"
RPA_CLEAR = "clear"
RPA_SELECT = "select"
RPA_CLICK = "click"
RPA_CLOSE = "close"

## Types of parameters that the instructions recieve
RPA_PARAM_URL = "url"
RPA_PARAM_STRING = "string"
RPA_PARAM_NUMBER = "number"
RPA_PARAM_BY = "by"
RPA_PARAM_SELECTOR = "selector"

## The shape of every instruction
RPA_INSTRUCTIONS = {
    RPA_GET: [RPA_PARAM_URL],
    RPA_INPUT: [RPA_PARAM_STRING],
    RPA_INPUT_RETURN: [],
    RPA_DELAY: [RPA_PARAM_NUMBER],
    RPA_WAIT: [RPA_PARAM_NUMBER],
    RPA_CLEAR: [],
    RPA_SELECT: [RPA_PARAM_BY, RPA_PARAM_SELECTOR],
    RPA_CLICK: [],
    RPA_CLOSE: []
}