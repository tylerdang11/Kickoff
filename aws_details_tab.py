from nicegui import ui

# Assuming form_data and other necessary imports or global variables are managed appropriately
#account_type = None
class AwsDetailsForm:
    def __init__(self):
        self.form_data = {}
        self.outlook_distribution_list = None
        self.account_type = None
        self.dl_members = None
        self.account_admin = None
        self.cloud_health_users = None
        self.cost_center = None
        self.primary_contact = None
        self.secondary_contact = None
        self.technical_contact = None
        self.client_ID = None
        self.environment_type = None
        self.gm_approval = None


    # Mock function to retrieve stored data for Subscriptions
    @staticmethod
    def get_stored_data():
        return {
            'Outlook Distribution list': 'Azure-VANG-DEV@epsilon.com',
            'DL Members': 'user1@example.com, user2@example.com',
            'Account Admins': 'admin@gmail.com',
            'Cloud Health Users': 'health@gmail.com',
            'Accounting Cost Center': 'US1802:4210100000:1A6F010198:B1A6F-002683-00:::P01017',
            'Primary contact': 'primary@gmail.com',
            'Secondary contact': 'secondary@gmail.com',
            'Technical contact': 'technical@gmail.com',
            'Four Digit Client ID': 'RUDY',
            'Environment Type': 'DEV',
            'GM Approval': 'gm@gmail.com',
            # ... [other fields]
        }

    def update_form_data(self, event=None):
        # Implementation to update form_data based on the input fields
        self.form_data['Outlook Distribution list'] = self.outlook_distribution_list.value
        self.form_data['DL Members'] = self.dl_members.value
        self.form_data['Account Admins'] = self.account_admin.value
        self.form_data['Cloud Health Users'] = self.cloud_health_users.value
        self.form_data['Accounting Cost Center'] = self.cost_center.value
        self.form_data['Primary contact'] = self.primary_contact.value
        self.form_data['Secondary contact'] = self.secondary_contact.value
        self.form_data['Technical contact'] = self.technical_contact.value
        self.form_data['Four Digit Client ID'] = self.client_ID.value
        self.form_data['Environment Type'] = self.environment_type.value
        self.form_data['GM Approval'] = self.gm_approval.value


    def update_aws_details(self, event):
        # Update form_data with the values from inputs
        self.form_data['aws_details'] = {  # Collect all AWS details
            'account_type': self.account_type.value,
            # ... [other fields as needed]
        }

    def on_account_type_change(self, event):
        #global account_type
        if self.account_type.value == 'New Account':
            # Show input fields for New Account
            self.outlook_distribution_list.value = ''
            self.dl_members.value = ''
            self.account_admin.value = ''
            self.cloud_health_users.value = ''
            self.cost_center.value = ''
            self.primary_contact.value = ''
            self.secondary_contact.value = ''
            self.technical_contact.value = ''
            self.client_ID.value = ''
            self.environment_type.value = ''
            self.gm_approval.value = ''
            # ... [reset other fields as needed]
        elif self.account_type.value == 'Subscriptions':
            # Pre-fill input fields with stored data
            stored_data = self.get_stored_data()
            self.outlook_distribution_list.value = stored_data.get('Outlook Distribution list', '')
            self.dl_members.value = stored_data.get('DL Members', '')
            self.account_admin.value = stored_data.get('Account Admins', '')
            self.cloud_health_users.value = stored_data.get('Cloud Health Users', '')
            self.cost_center.value = stored_data.get('Accounting Cost Center', '')
            self.primary_contact.value = stored_data.get('Primary contact', '')
            self.secondary_contact.value = stored_data.get('Secondary contact', '')
            self.technical_contact.value = stored_data.get('Technical contact', '')
            self.client_ID.value = stored_data.get('Four Digit Client ID', '')
            self.environment_type.value = stored_data.get('Environment Type', '')
            self.gm_approval.value = stored_data.get('GM Approval', '')

            # ... [set other fields with stored data]

    def setup_aws_details_tab(self):
        #global account_type
        self.account_type = ui.select(['New Account', 'Subscriptions'], label='Account Type', on_change=self.on_account_type_change)
        self.outlook_distribution_list = ui.input(label='Outlook Distribution list')
        self.dl_members = ui.textarea(label='DL Members')
        self.account_admin = ui.input(label='Account Admins')
        self.cloud_health_users = ui.input(label='Cloud Health Users')
        self.cost_center = ui.input(label='Accounting Cost Center')
        self.primary_contact = ui.input(label='Primary contact')
        self.secondary_contact = ui.input(label='Secondary contact')
        self.technical_contact = ui.input(label='Technical contact')
        self.client_ID = ui.input(label='Four Digit Client ID')
        self.environment_type = ui.input(label='Environment Type')
        self.gm_approval = ui.input(label='GM Approval')
        # ... [other input fields]
        ui.button('Save Details', on_click=self.update_aws_details)
