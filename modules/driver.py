from .exception import RPABrowserNotSupported, RPAInvalidInstruction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Driver():
    """
    Clase que representa una entidad capaz de operar un navegador web.
    La idea es que no se dependa únicamente de Selenium.
    """

    def __init__(self):
        self.browser = CHROME
        self.driverPath = None
        self.delay = 0

    def setup(self, browser, path = None):
        self.browser = browser
        self.driverPath = path

    def getWebDriver(self):
        pass

    def setBrowser(self, browser):
        self.browser = browser
    
    def setDriverPath(self, path):
        self.driverPath = path

    def setDelay(self, delay):
        self.delay = delay
    
    def wait(self, seconds):
        time.sleep(seconds)

    def clear(self):
        pass
    
    def get(self, url):
        pass

    def input(self, str):
        pass

    def input_return(self):
        pass

    def selectBy(self, by, selector):
        pass

    def click(self):
        pass

    def backward(self):
        pass

    def forward(self):
        pass

    def close(self):
        pass


class SeleniumWebDriver(Driver):
    """
    Implementación específica utilizando Selenium.
    """

    def __init__(self):
        super().__init__()
        self.selectedElement = None

    def setup(self, browser, path = None):
        super().setup(browser, path)
        self.driver = self.getWebDriver()

    def getWebDriver(self):
        args = []
        if self.driverPath:
            args.append(self.driverPath)

        if self.browser == CHROME:
            return webdriver.Chrome(*args)
        elif self.browser == FIREFOX:
            return webdriver.Firefox(*args)
        elif self.browser == OPERA:
            return webdriver.Opera(*args)
        else:
            raise RPABrowserNotSupported("El navegador \"" + str(self.browser) + "\" no es soportado")
    
    def clear(self):
        self.wait(self.delay)
        self.selectedElement.clear()
    
    def get(self, url):
        self.wait(self.delay)
        self.driver.get(url)

    def input(self, str):
        self.wait(self.delay)
        self.selectedElement.send_keys(str)

    def input_return(self):
        self.wait(self.delay)
        self.selectedElement.send_keys(Keys.RETURN)

    def selectBy(self, by, selector):
        self.wait(self.delay)
        if by == "name":
            self.selectedElement = self.driver.find_element_by_name(selector)
        elif by == "id":
            self.selectedElement = self.driver.find_element_by_id(selector)
        elif by == "class":
            self.selectedElement = self.driver.find_element_by_class_name(selector)
        elif by == "xpath":
            self.selectedElement = self.driver.find_element_by_xpath(selector)
        elif by == "selector":
            self.selectedElement = self.driver.find_element_by_css_selector(selector)
        elif by == "tag":
            self.selectedElement = self.driver.find_element_by_tag_name(selector)
        elif by == "link_text":
            self.selectedElement = self.driver.find_element_by_partial_link_text(selector)
        else:
            raise RPAInvalidInstruction("selectBy " + str(by) + " No está implementado todavía.")

    def click(self):
        self.wait(self.delay)
        self.selectedElement.click()

    def backward(self):
        self.wait(self.delay)
        self.driver.backward()

    def forward(self):
        self.wait(self.delay)
        self.driver.forward()

    def close(self):
        self.wait(self.delay)
        self.driver.close()

# Supported Browsers
CHROME = "chrome"
FIREFOX = "firefox"
OPERA = "opera"

SUPPORTED_BROWSERS = [CHROME, FIREFOX, OPERA]