from nicegui import ui
# Import JIRA client library if not already done
from jira import JIRA
import menu



# Placeholder for getting environment variables
def get_env_var(key):
    # Implement this function to fetch environment variables
    return "Your_Value_Here"

def GetProjectList():
    userName = menu.getJsonVal("env_var", "JIRAUSER")
    passWord = menu.getJsonVal("env_var", "JIRAPASS")
    urlPath = menu.getJsonVal("env_var", "JIRAURL")
    jqlStr = menu.getJsonVal("env_var", "KICKOFF")

    jiraOptions = {'server': urlPath, 'verify': False}
    jira = JIRA(options=jiraOptions, basic_auth=(userName, passWord))

    all_issues = []
    start_at = 0
    max_results = 50  # Adjust this if needed
    while True:
        issues = jira.search_issues(jqlStr, startAt=start_at, maxResults=max_results)
        all_issues.extend(issues)
        if len(issues) < max_results:
            break  # Exit the loop if there are no more issues to fetch
        start_at += len(issues)

    issueList = [{'id': issue.key, 'summary': issue.fields.summary} for issue in all_issues]
    return issueList

    # Fetch all projects instead of searching for issues
    #unique_projects = {}

    # Iterate over each issue to extract project information
    #for issue in issues:
        #project = issue.fields.project
        #unique_projects[project.key] = project.name

    # Convert the unique projects dictionary to a list of dictionaries
    #projectList = [{'id': key, 'description': name} for key, name in unique_projects.items()]
    #return projectList


def setup_project_dropdown():
    # This is the start of the function block, everything inside needs to be indented

    def on_project_select(event):
        # This is a nested function, so it has another level of indentation
        selected_issue_key = event.value
        # More code for handling the selected project...

    # Back to the main function block indentation level
    issueList = GetProjectList()
    issue_options = [(issue['id'], f"{issue['id']} - {issue['summary']}") for issue in issueList]

    # Still within the setup_project_dropdown function block
    issue_dropdown = ui.select(label='Search Project', options=issue_options, with_input=True, on_change=on_project_select)
    # More code for the function...


# Now we're back to the outermost indentation level, indicating the end of the setup_project_dropdown function


def display_project_details(project_id):
    # Logic to display details for the selected project
    pass

# This is assuming you are calling this function to set up the UI components
setup_project_dropdown()


# Global variable to store all issues fetched once
#all_issues = []

"""def setup_search_bar():
    global all_issues
    search_results_label = ui.label('')  # This label will display search results.

    # Fetch all issues when setting up the search bar
    if not all_issues:
        all_issues = GetProjectList()

    def on_search_input(event):
        # Make sure this is the correct way to access the input's value in nicegui
        search_term = event.value.lower().strip()
        if search_term:
            matching_issues = [issue for issue in all_issues if search_term in issue['summary'].lower()]
            if matching_issues:
                # Update the label's text with the matching issues
                search_results_label.set_text('\n'.join(f"{issue['id']} - {issue['summary']}" for issue in matching_issues))
            else:
                search_results_label.set_text('No matching issues found.')
        else:
            search_results_label.set_text('')  # Reset the label text to empty

    search_input = ui.input(placeholder='Search Project...')
    # Bind the event handler to the 'input' event
    search_input.on('input', on_search_input)




# ... inside your main UI setup code ...
setup_search_bar()
# ... rest of your UI setup ..."""

