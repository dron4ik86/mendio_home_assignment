from .locators import *
from interactions.helper.helper import Helper
import time


class UserMenu:

    def __init__(self, context):
        self.context = context

    def press_on_profile_button(self):
        time.sleep(1)
        Helper(self.context).click_on_element_by_css(PROFILE_BUTTON)

    def press_logout_button(self):
        Helper(self.context).click_on_element_by_text(LOGOUT_BUTTON)



