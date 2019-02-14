class Task:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.name = attributes.get('name', '')
        self.role_id = attributes.get('role_id')
