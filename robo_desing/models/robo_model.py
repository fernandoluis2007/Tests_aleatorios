from contextlib import contextmanager

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@contextmanager
def driver_chrome(driver : webdriver):
    driver.maximize_window()
    driver.implicitly_wait(1)
    try:
        yield driver
    finally:
        driver.quit()

class Acoes_Robo:
    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotInteractableException,
                StaleElementReferenceException
            ]
        )


    def element(self, locator : tuple | WebElement) -> WebElement:
        if isinstance(locator, WebElement):
            return locator

        self.wait.until(lambda driver: driver.find_element(*locator)) #*locator --> desempacotar a tupla que vem (By.CSS_SELECTOR, '.class_div')
        return self.driver.find_element(*locator)

    def elements(self, locator : tuple) -> list[WebElement]:
        self.wait.until(lambda driver : driver.find_elements(*locator))
        return self.driver.find_elements(*locator)

    def select_element(self, locator : tuple) -> Select:
        select_element = self.element(locator=locator)
        select = Select(select_element)
        return select

    def select_by_visible_text(self, locator : tuple, text : str) -> WebElement:
        select = self.select_element(locator=locator)
        select.select_by_visible_text(text)
        return select._el # WebElement por trás do objeto Select

    def element_send_keys(self, locator : tuple | WebElement, text : str) -> None:
        element = self.element(locator)
        element.send_keys(text.lower())

    def click_element(self, locator : tuple | WebElement):
        element = self.element(locator=locator)
        element.click()

    def text_element(self, locator : tuple) -> str:
        element = self.element(locator=locator)
        return element.text







