class RPAException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

class RPAArgsException(RPAException):
    pass

class RPAParserException(RPAException):
    pass

class RPAExecutionException(RPAException):
    pass

class RPAInvalidInstruction(RPAException):
    pass

class RPABrowserNotSupported(RPAException):
    pass

class RPADriverNotSupported(RPAException):
    pass

class RPANotImplemented(RPAException):
    pass

class RPAInputFormatNotSupported(RPAException):
    pass