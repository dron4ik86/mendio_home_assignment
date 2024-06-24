from .locators import *
from interactions.helper.helper import Helper


class RepositoriesPage:

    def __init__(self, context):
        self.context = context

    def is_element_visible_by_text(self, value):
        Helper(self.context).is_element_visible_by_text(value)
