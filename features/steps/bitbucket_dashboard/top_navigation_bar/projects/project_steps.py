from behave import step
from pages.bitbucket_dashboard.top_navigation_bar.projects.projects_page import ProjectsPage


@step('I press on the projects button')
def press_on_projects_button(context):
    ProjectsPage(context).go_to_projects()


@step('I need to go to specific project')
def go_to_specific_project(context):
    ProjectsPage(context).go_to_specific_project()


@step('I press on Create repository button')
def press_create_repository_button(context):
    ProjectsPage(context).press_on_create_repository_button()


@step('I will be redirected to the Create a new repository form')
def is_create_repository_form_visible(context):
    ProjectsPage(context).is_create_repository_form_visible()


@step('I enter repository name {random_name}')
def enter_repository_name(context, random_name):
    ProjectsPage(context).enter_repository_name(random_name)


@step('I choose not to include a README file')
def ignore_readme_file(context):
    ProjectsPage(context).readme_dropdown(value='No')


@step('I press on Create repository button on the form')
def press_create_repository_on_the_form(context):
    ProjectsPage(context).press_on_create_repository_button_by_css_selector()





