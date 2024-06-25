import time
from faker import Faker
from .locators import *
from interactions.helper.helper import Helper

faker = Faker()


class RepositoriesPage:

    def __init__(self, context):
        self.context = context

    def is_element_visible_by_text(self, value):
        Helper(self.context).is_element_visible_by_text(value)

    def press_the_branches_button(self):
        Helper(self.context).click_on_element_by_text(BRANCHES_BUTTON)

    def press_on_create_branch_button(self):
        Helper(self.context).click_on_element_by_id(CREATE_BRANCH_BUTTON)

    def is_create_branch_form_visible(self):
        Helper(self.context).is_element_visible_by_xpath(CREATE_BRANCH_FORM_TITLE)

    def enter_branch_name(self, branch_name):
        Helper(self.context).send_keys_by_name(BRANCH_NAME_FIELD, branch_name)

    def press_create_button(self):
        Helper(self.context).click_on_element_by_id(CREATE_BUTTON)

    def press_the_source_button(self):
        Helper(self.context).click_on_element_by_text(SOURCE_BUTTON)

    def press_on_branches_dropdown_menu(self):
        Helper(self.context).click_on_element_by_css(BRANCH_DROPDOWN_BUTTON)

    def choose_specific_branch_in_dropdown_menu(self, branch_name):
        xpath = BRANCH_NAME_DROPDOWN.format(branch_name)
        Helper(self.context).click_on_element_by_xpath(xpath)

    def press_on_meatballs_menu(self):
        Helper(self.context).click_on_element_by_css(MEATBALLS_MENU)

    def press_on_add_files_meatballs_menu(self):
        Helper(self.context).click_on_element_by_xpath(MEATBALLS_MENU_ADD_FILE)

    def is_creation_file_screen_visible(self):
        Helper(self.context).is_element_visible_by_id(FILE_NAME_FIELD)

    def enter_filename(self, value):
        Helper(self.context).send_keys_and_press_enter_by_id(FILE_NAME_FIELD, value)

    def insert_random_text_into_file(self):
        Helper(self.context).send_keys_by_script(CODE_INPUT_WINDOW, faker.text())

    def press_commit_button(self):
        Helper(self.context).click_on_element_by_css(COMMIT_BUTTON)

    def press_commit_button_commit_changes_dialog(self):
        Helper(self.context).click_on_element_by_css(COMMIT_BUTTON_COMMIT_CHANGES_DIALOG)

    def is_file_visible(self, file_name):
        Helper(self.context).is_element_visible_by_xpath(file_name)

    def press_create_button_branch_table(self):
        Helper(self.context).click_on_second_element_by_xpath(CREATE_BUTTON_BRANCH_TABLE)

    def press_create_pull_request_button(self):
        time.sleep(1)
        Helper(self.context).click_on_element_by_xpath(CREATE_PULL_REQUEST_BUTTON)

    def press_approve_button(self):
        Helper(self.context).click_on_element_by_xpath(APPROVE_BUTTON)

    def press_merge_button(self):
        Helper(self.context).click_on_element_by_xpath(MERGE_BUTTON)

    def press_merge_button_merge_dialog_window(self):
        time.sleep(1)
        Helper(self.context).press_on_element_in_dialog_window(MERGE_BUTTON_MERGE_DIALOG_WINDOW)
        time.sleep(2)

    def press_repository_settings_button(self):
        Helper(self.context).click_on_element_by_text(REPOSITORY_SETTINGS)

    def delete_repository(self):
        Helper(self.context).click_on_element_by_xpath(MANAGE_REPOSITORY_DROPDOWN_MENU)
        Helper(self.context).click_on_element_by_xpath(DELETE_REPOSITORY)
        Helper(self.context).click_on_element_by_xpath(DELETE_BUTTON)
