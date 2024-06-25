from behave import step
from pages.bitbucket_dashboard.top_navigation_bar.user_menu.user_menu import UserMenu


@step('I complete the logout process')
def complete_logout_process(context):
    UserMenu(context).press_on_profile_button()
    UserMenu(context).press_logout_button()




