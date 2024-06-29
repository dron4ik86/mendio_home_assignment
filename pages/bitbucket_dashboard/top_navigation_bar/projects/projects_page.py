import time

from .locators import *
from interactions.helper.helper import Helper


class ProjectsPage:

    def __init__(self, context):
        self.context = context

    def go_to_projects(self):
        Helper(self.context).click_on_element_by_text(PROJECTS_BUTTON)

    def go_to_specific_project(self):
        Helper(self.context).click_on_second_element_by_text(MINDIO_PROJECT)

    def press_on_create_repository_button(self):
        Helper(self.context).click_on_element_by_xpath(CREATE_REPOSITORY_BUTTON)

    def verify_repository_form_is_visible(self):
        Helper(self.context).is_element_visible_by_id(NEW_REPOSITORY_FORM)

    def enter_repository_name(self, repo_name):
        Helper(self.context).send_keys_by_id(REPOSITORY_NAME_FIELD, repo_name)

    def readme_dropdown(self, value):
        Helper(self.context).select_from_dropdown_menu_by_id(README_SELECT, value)

    def press_on_create_repository_button_in_form(self):
        Helper(self.context).click_on_element_by_xpath(CREATE_REPOSITORY_BUTTON_IN_FORM)

