from nicegui import ui
#from aws_details_tab import setup_aws_details_tab
from aws_details_tab import AwsDetailsForm
from search_and_details import setup_search_and_project_details

aws_details_form = AwsDetailsForm()
setup_search_and_project_details()

form_data = {}
with ui.splitter(value=10).classes('w-full h-full') as splitter:
    with splitter.before:
        with ui.tabs().props('vertical').classes('w-full') as tabs:
            general_info = ui.tab('General Information', icon='info')
            aws_details = ui.tab('AWS Details', icon='cloud')
            network_info = ui.tab('Network Information', icon='router')
            server_details = ui.tab('Server Details', icon='dns')
            user_info = ui.tab('User Information', icon='person')
            patching_info = ui.tab('Patching Information', icon='healing')
            monitoring_info = ui.tab('Monitoring Information', icon='visibility')
            backup_info = ui.tab('Back Information', icon='backup')
            custom_spec = ui.tab('Custom Spec', icon='list')
            firewall_req = ui.tab('Firewall Requirement', icon='shield')
            # Add more tabs as needed...

    with splitter.after:
        with ui.tab_panels(tabs, value=general_info).props('vertical').classes('w-full h-full'):
            with ui.tab_panel(general_info):
                ui.label('General Information').classes('text-h4')
                ui.input('Project Name')
                ui.input('Description')
                # Add more input fields for General Information...

            with ui.tab_panel(aws_details):
                ui.label('AWS Account').classes('text-h4')
                aws_details_form.setup_aws_details_tab()
                ui.button('Save Details', on_click=aws_details_form.update_form_data)

            with ui.tab_panel(network_info):
                ui.label('Network Information').classes('text-h4')
                ui.input('VPC ID')
                ui.input('Subnet IDs')
                # Add more input fields for Network Information...

            # Define more tab panels for other tabs...

ui.run(title='Project Kickoff UI')
