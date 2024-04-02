from nicegui import ui
with ui.row():
    with ui.card().classes("w-full"):
        NewAccount = ui.checkbox('New VPC?', value=True).classes('w-60')
        with ui.column().bind_visibility_from(NewAccount, 'value').classes("w-full"):
            ui.input(label = 'AWS Account Number: ').classes('w-full')
            ui.input(label = 'Region: ').classes('w-full')
            ui.input(label = 'Client Code: ').classes('w-full')
            ui.input(label = 'Client Env: ').classes('w-full')
            ui.input(label = 'Availability Zones: ').classes('w-full')
            ui.input(label = 'Hosted Zone: ').classes('w-full')

            ui.button('Save Changes')
        with ui.column().bind_visibility_from(NewAccount, 'value', value=False).classes("w-full"):
            ui.input(label = 'VPC Name: ').classes('w-full')
            ui.input(label = 'VPC ID: ').classes('w-full')
            ui.input(label = 'IPv4 CIDR Block: ').classes('w-full')
            ui.input(label = 'AWS Public CIDR: ').classes('w-full')
            ui.input(label = 'AWS Private CIDR: ').classes('w-full')

            ui.button('Save Changes')



ui.run()
