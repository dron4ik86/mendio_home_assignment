import time
from behave import step
from pages.bitbucket_dashboard.top_navigation_bar.repositories.repositories_page import RepositoriesPage


@step('I need to verify that the repository was created {repo_name}')
def is_repository_created(context, repo_name):
    RepositoriesPage(context).is_element_visible_by_text(repo_name)


@step('I press on the Branches button')
def press_the_branches_button(context):
    RepositoriesPage(context).press_the_branches_button()


@step('I press on the Create branch button')
def press_create_branch_button(context):
    RepositoriesPage(context).press_on_create_branch_button()


@step('I will get a Create branch form')
def is_create_branch_form_visible(context):
    RepositoriesPage(context).is_create_branch_form_visible()


@step('I enter the branch name {branch_name}')
def enter_branch_name(context, branch_name):
    RepositoriesPage(context).enter_branch_name(branch_name)


@step('I press Create button')
def press_create_button(context):
    RepositoriesPage(context).press_create_button()


@step('I need to verify that branch was created {branch_name}')
def is_new_branch_created(context, branch_name):
    time.sleep(2)
    RepositoriesPage(context).press_the_source_button()
    RepositoriesPage(context).press_on_branches_dropdown_menu()
    RepositoriesPage(context).choose_specific_branch_in_dropdown_menu(branch_name)


@step('I press on the Meatballs menu')
def press_on_meatballs_menu(context):
    RepositoriesPage(context).press_on_meatballs_menu()


@step('I press on the Add file menu item')
def press_on_add_file_meatballs_menu(context):
    RepositoriesPage(context).press_on_add_files_meatballs_menu()


@step('I will be redirected to the file creation screen')
def is_file_creation_screen_visible(context):
    RepositoriesPage(context).is_creation_file_screen_visible()


@step('I enter a filename {file_name}')
def enter_filename(context, file_name):
    RepositoriesPage(context).enter_filename(file_name)


@step('I entered some random text into the file')
def insert_random_text_into_file(context):
    RepositoriesPage(context).insert_random_text_into_file()


@step('I press on the Commit button')
def press_commit_button(context):
    RepositoriesPage(context).press_commit_button()
    RepositoriesPage(context).press_commit_button_commit_changes_dialog()


@step('I switch to the new branch {branch_name}')
def switch_to_specific_branch(context, branch_name):
    RepositoriesPage(context).press_on_branches_dropdown_menu()
    RepositoriesPage(context).choose_specific_branch_in_dropdown_menu(branch_name)


@step('I need to verify that new file was created {file_name}')
@step('I need to verify that new file was created {file_name} on main branch')
def is_file_created(context, file_name):
    RepositoriesPage(context).is_file_visible(file_name)


@step('I press Create button in the Branch table')
def press_on_create_button_branch_table(context):
    RepositoriesPage(context).press_create_button_branch_table()


@step('I press Create pull request button')
def press_create_pull_request_button(context):
    RepositoriesPage(context).press_create_pull_request_button()


@step('I press Approve button')
def press_approve_button(context):
    RepositoriesPage(context).press_approve_button()


@step('I press Merge button')
def press_merge_button(context):
    RepositoriesPage(context).press_merge_button()


@step('I press Merge button in dialog window')
def press_merge_button_merge_dialog_window(context):
    RepositoriesPage(context).press_merge_button_merge_dialog_window()


@step('I press on the Source button')
def press_source_button(context):
    RepositoriesPage(context).press_the_source_button()


@step('I press on the Repository settings button')
def press_repository_settings_button(context):
    RepositoriesPage(context).press_repository_settings_button()


@step('I delete the repository that was created')
def delete_repository(context):
    RepositoriesPage(context).delete_repository()


