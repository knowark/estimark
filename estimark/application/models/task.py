from .entity import Entity


class Task(Entity):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.name = attributes.get('name', '')
        self.summary = attributes.get('summary', False)
        self.parent_id = attributes.get('parent_id')
        self.role_id = attributes.get('role_id')
        self.state = attributes.get('state', 'open')
