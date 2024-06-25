import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


class Helper:

    def __init__(self, context):
        self.driver = context.driver
        self.wait = context.wait

    def navigate_to_page(self, url):
        try:
            self.driver.get(url)
        except TimeoutException:
            raise TimeoutException(f"TimeoutException: Page took too long to load - {url}")

    def send_keys_and_press_enter_by_id(self, element_id, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.ID, f"{element_id}")))
            element.send_keys(value)
            time.sleep(1)
            element.send_keys(Keys.RETURN)
        except TimeoutException:
            raise TimeoutException(f"Can't find element by ID. The ID is {element_id}")

    def is_element_clickable_by_id(self, element_id):
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, f"{element_id}")))
        except TimeoutException:
            raise TimeoutException(f"Element isn't clickable by ID. The ID is {element_id}")

    def click_on_element_by_text(self, value):
        try:
            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, f"{value}"))).click()
        except TimeoutException:
            raise TimeoutException(f"Can't find element by LINK TEXT. The text is {value}")

    def click_on_second_element_by_text(self, value):
        try:
            self.wait.until(lambda _: len(self.driver.find_elements(By.LINK_TEXT, value)) > 1)
            elements = self.driver.find_elements(By.LINK_TEXT, value)
            self.wait.until(EC.element_to_be_clickable(elements[1])).click()
        except TimeoutException:
            raise TimeoutException(f"Can't find the second element by LINK TEXT. The text is {value}")

    def is_element_visible_by_id(self, value):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, value)))
        except TimeoutException:
            raise TimeoutException(f"Element isn't visible. The element ID is {value}")

    def send_keys_by_id(self, element_id, value):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, f"{element_id}"))).send_keys(value)
        except TimeoutException:
            raise TimeoutException(f"Can't find element by ID. The ID is {element_id}")

    def select_from_dropdown_menu_by_id(self, element_id, value):
        try:
            select = Select(self.driver.find_element(By.ID, element_id))
            select.select_by_visible_text(value)
        except TimeoutException:
            raise TimeoutException(f"Can't find element by ID. The ID is {element_id}")

    def click_on_element_by_xpath(self, element):
        try:
            # self.wait.until(EC.presence_of_element_located((By.XPATH, f"{element}")))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"{element}"))).click()
        except TimeoutException:
            raise TimeoutException(f"Can't find element by XPATH. The XPATH is {element}")

    def is_element_visible_by_text(self, value):
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, value)))
        except TimeoutException:
            raise TimeoutException(f"Element isn't visible. The element TEXT is {value}")

    def click_on_element_by_id(self, element_id):
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, f"{element_id}"))).click()
        except TimeoutException:
            raise TimeoutException(f"Can't find element by ID. The ID is {element_id}")

    def is_element_visible_by_xpath(self, value):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[text()='{value}']")))
        except TimeoutException:
            raise TimeoutException(f"Element isn't visible. The XPATH is {value}")

    def send_keys_by_name(self, element_name, value):
        try:
            self.wait.until(EC.presence_of_element_located((By.NAME, f"{element_name}"))).send_keys(value)
        except TimeoutException:
            raise TimeoutException(f"Can't find element by NAME. The NAME is {element_name}")

    def click_on_element_by_css(self, element_id):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"{element_id}")))
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"{element_id}"))).click()
        except TimeoutException:
            raise TimeoutException(f"Can't find element by CSS SELECTOR. The ID is {element_id}")

    def send_keys_by_css(self, element_id, value):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"{element_id}"))).send_keys(value)
        except TimeoutException:
            raise TimeoutException(f"Can't find element by CSS. The CSS SELECTOR is {element_id}")

    def send_keys_by_xpath(self, element_id, value):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, f"{element_id}"))).send_keys(value)
        except TimeoutException:
            raise TimeoutException(f"Can't find element by ID. The ID is {element_id}")

    def send_keys_by_script(self, element, text):
        time.sleep(2)
        script = f"document.querySelector('.{element}').{element}.setValue(arguments[0]);"
        self.driver.execute_script(script, text)

    def click_on_second_element_by_xpath(self, element):
        try:
            self.wait.until(lambda _: len(self.driver.find_elements(By.XPATH, element)) > 1)
            elements = self.driver.find_elements(By.XPATH, element)
            self.wait.until(EC.element_to_be_clickable(elements[1])).click()
        except TimeoutException:
            raise TimeoutException(f"Can't find the second element by LINK TEXT. The text is {element}")

    def press_on_element_in_dialog_window(self, element):
        merge_button = self.driver.find_element(By.CSS_SELECTOR, f"{element}")
        ActionChains(self.driver).move_to_element(merge_button).click().perform()

