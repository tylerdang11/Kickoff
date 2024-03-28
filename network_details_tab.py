from nicegui import ui

# Assuming form_data and other necessary imports or global variables are managed appropriately
#account_type = None
class NetworkDetailsForm:
    def __init__(self):
        self.form_data = {}
        self.AWS_acct_number = None
        self.Region = None
        self.Client_Code = None
        self.Client_Env = None
        self.Avail_zones = None
        self.Hosted_Zones = None
        self.VPC_Name = None
        self.VPC_ID = None
        self.IPv4_CIDR_Blk = None
        self.AWS_Public_CIDR = None
        self.AWS_Private_CIDR = None



    # Mock function to retrieve stored data for Subscriptions
    @staticmethod
    def get_stored_data():
        return {
            'Outlook Distribution list': 'Azure-VANG-DEV@epsilon.com',
            'DL Members': 'user1@example.com, user2@example.com',
            'Account Admins': 'admin@gmail.com',
            'Cloud Health Users': 'health@gmail.com',
            'Accounting Cost Center': 'US1802:4210100000:1A6F010198:B1A6F-002683-00:::P01017',

            #'GM Approval': 'gm@gmail.com',
            # ... [other fields]
        }

    def update_form_data(self, event=None):
        # Implementation to update form_data based on the input fields
        self.form_data['AWS Account Number:'] = self.AWS_acct_number.value
        self.form_data['Region:'] = self.Region.value
        self.form_data['Client Code:'] = self.Client_Code.value
        self.form_data['Client Env:'] = self.Client_Env.value
        self.form_data['Availability Zones'] = self.Avail_zones.value
        self.form_data['Hosted Zone'] = self.Hosted_Zones.value
        self.form_data['VPC Name:'] = self.VPC_Name.value
        self.form_data['VPC ID:'] = self.VPC_ID.value
        self.form_data['IPv4 CIDR Block:'] = self.IPv4_CIDR_Blk.value
        self.form_data['AWS Public CIDR:'] = self.AWS_Public_CIDR.value
        self.form_data['AWS Private CIDR:'] = self.AWS_Private_CIDR.value


    def update_network_details(self, event):
        # Update form_data with the values from inputs
        self.form_data['network_details'] = {  # Collect all AWS details
            'account_type': self.account_type.value,
            # ... [other fields as needed]
        }

    def on_account_type_change(self, event):
        #global account_type
        if self.account_type.value == 'Yes':
            # Show input fields for New Account
            self.AWS_acct_number = ui.input(label='AWS Account Number:')
            self.Region = ui.input(label = 'Region:')
            self.Client_Code = ui.input(label = 'Client Code:')
            self.Client_Env = ui.input(label = 'Client Env:')
            self.Avail_zones = ui.input(label = 'Availability Zones:')
            self.Hosted_Zones = ui.input(label = 'Hosted Zones:')
            # ... [reset other fields as needed]
        elif self.account_type.value == 'No':
            # Pre-fill input fields with stored data
            #stored_data = self.get_stored_data()
            self.VPC_Name = ui.input(label = 'VPC Name:')
            self.VPC_ID = ui.input(label = "VPC ID:")
            self.IPv4_CIDR_Blk = ui.input(label = 'IPv4 CIDR Block:')
            self.AWS_Public_CIDR = ui.input(label = 'AWS Public CIDR')
            self.AWS_Private_CIDR = ui.input(label = 'AWS Private CIDR')
            # ... [set other fields with stored data]

    def setup_network_details_tab(self):
        #global account_type
        self.account_type = ui.select(['Yes', 'No'], label='New VPC?', on_change=self.on_account_type_change).classes('w-40')
        '''self.outlook_distribution_list = ui.input(label='AWS Account Number:')
        self.dl_members = ui.textarea(label='Region:')
        self.account_admin = ui.input(label='Client Code:')
        self.cloud_health_users = ui.input(label='Client Env:')
        self.cost_center = ui.input(label='Availability Zones:').classes('auto')
        self.primary_contact = ui.input(label='Hosted Zones:')
        self.secondary_contact = ui.input(label='VPC Name:')
        self.technical_contact = ui.input(label='VPC ID:')
        self.client_ID = ui.input(label='IPv4 CIDR Block:')
        self.environment_type = ui.input(label='AWS Public CIDR:')
        self.gm_approval = ui.input(label='AWS Private CIDR:')
        # ... [other input fields]'''
        ui.button('Save Details', on_click=self.update_network_details)
