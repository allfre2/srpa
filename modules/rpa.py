from selenium import webdriver

class RPA():
    def __init__(self, parser):
        self.parser = parser
        self.parser.parseRPAScript()

    def exec(self):
        pass
