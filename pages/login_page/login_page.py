from .locators import *
import os
from interactions.helper.helper import Helper


class LoginPage:

    def __init__(self, context):
        self.context = context

    def navigate_to_login_page(self):
        Helper(self.context).navigate_to_page(os.getenv("BITBUCKET_SIGNIN_URL"))

    def enter_username(self):
        Helper(self.context).send_keys_and_press_enter_by_id(USERNAME_FIELD, os.getenv("USERNAME"))

    def enter_password(self):
        Helper(self.context).is_element_clickable_by_id(PASSWORD_FIELD)
        Helper(self.context).send_keys_and_press_enter_by_id(PASSWORD_FIELD, os.getenv("PASSWORD"))



