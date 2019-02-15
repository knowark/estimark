class Task:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.name = attributes.get('name', '')
        self.parent_id = attributes.get('parent_id')
        self.role_id = attributes.get('role_id')
