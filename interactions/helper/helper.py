from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Helper:

    def __init__(self, context):
        self.driver = context.driver
        self.wait = context.wait

    def navigate_to_page(self, url):
        try:
            self.driver.get(url)
        except TimeoutException:
            raise TimeoutException(f"TimeoutException: Page took too long to load - {url}")

    def send_keys_by_id(self, element_id, value):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, f"{element_id}"))).send_keys(value + Keys.RETURN)
        except TimeoutException:
            raise TimeoutException(f"Can't find element by ID the is {element_id}")

    def is_element_clickable_by_id(self, element_id):
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, f"{element_id}")))
        except TimeoutException:
            raise TimeoutException(f"Element isn't clickable by ID the is {element_id}")

