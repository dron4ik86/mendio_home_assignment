from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Helper:

    def __init__(self, driver=None, wait=None):
        self.driver = driver
        self.wait = wait

    def send_keys(self, element_id, value):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, f"{element_id}"))).send_keys(value + Keys.RETURN)
        except TimeoutException:
            raise TimeoutException(f"Can't find element by ID the is {element_id}")



