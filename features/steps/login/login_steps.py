import time

from behave import step
from pages.login_page.login_page import LoginPage


@step('Navigate to login page')
def complete_login_process(context):
    LoginPage(context).navigate_to_login_page()


@step('I enter the username')
def enter_username(context):
    LoginPage(context).enter_username()


@step('I enter the password')
def enter_password(context):
    LoginPage(context).enter_password()



