from behave import step
from pages.bitbucket_dashboard.top_navigation_bar.repositories.repositories_page import RepositoriesPage


@step('I need to verify that the repository was created {repo_name}')
def is_repository_created(context, repo_name):
    RepositoriesPage(context).is_element_visible_by_text(repo_name)








