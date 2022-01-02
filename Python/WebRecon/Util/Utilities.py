from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Utilities:
    def __init__(self, driver=None):
        self.driver = driver

    def checkExistsXpath(self):     # Consulta Invalida / Invalid Query
        try:
            text = self.driver.find_element(By.XPATH, "//html/body/div/main/section/div[1]/form/fieldset/p").text
            if text == "":
                return False
        except NoSuchElementException:
            return False
        return True
