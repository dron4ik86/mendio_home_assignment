from .locators import *
import os
from interactions.helper.helper import Helper


class LoginPage:

    def __init__(self, context):
        self.driver = context.driver
        self.wait = context.wait

    def login_bitbucket(self, username, password):
        self.driver.get("https://bitbucket.org/account/signin/")
        Helper(self.wait).send_keys(element_id='username', value=username)
        Helper(self.wait).send_keys(element_id='password', value=password)


