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
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= len(self.script):
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
    
    def __str__(self):
        return "Script: " + self.name + "\nBy: " + self.author + "\n" + "Instructions: " + str(self.script) + "\n" 