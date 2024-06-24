Feature: Projects


@sanity
Scenario Outline: Create repository on BitBucket and verify that README.md file was created
  Given Navigate to login page
  When I enter the username
  And I enter the password
  When I press on the projects button
  Then I need to go to specific project
  When I press on Create repository button
  Then I will be redirected to the Create a new repository form
  When I enter repository name <repo_name>
  And I choose not to include a README file
  And I press on Create repository button on the form
  Then I need to verify that the repository was created <repo_name>
#  When I press on the Branches button
#  And I press on the Create branch button
#  Then I will get a Create branch form
#  When I enter the branch name <branch_name>
#  And I press Create button
#  Then I need to verify that branch was created <branch_name>
#  When I press on the Source button
#  And I switch to the new branch <branch_name>
#  And I press on the Meatballs menu
#  And I press on the Add file menu item
#  Then I will be redirected to the file creation screen
#  When I enter a filename <file_name>
#  And I entered some random text into the file
#  And I press on the Commit button
#  And I switch to the new branch <branch_name>
#  Then I need to verify that new file was created <file_name>
#  When I press on the Branches button
#  And I press Create button in the Branch table
#  And I press Create pull request button
#  And I press Approve button
#  And I press Merge button
#  And I press on the Source button
#  Then I need to verify that new file was created <file_name> on main branch

  Examples:
  | repo_name   | branch_name | file_name |
  | random_name | test_branch | README.md |