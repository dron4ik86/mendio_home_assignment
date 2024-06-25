from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


@fixture
def set_up_driver(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.wait = WebDriverWait(context.driver, 10)
    context.driver.maximize_window()


def before_all(context):
    """
    """
    ...


def before_feature(context, feature):
    """
    """
    ...


def before_scenario(context, scenario):
    """
    """
    use_fixture(set_up_driver, context)


def after_scenario(context, scenario):
    """
    """
    ...


def after_feature(context, feature):
    """
    """
    ...


def before_step(context, step):
    """
    """
    ...


def after_step(context, step):
    """
    """
    pass


def after_all(context):
    """
    """
    pass


