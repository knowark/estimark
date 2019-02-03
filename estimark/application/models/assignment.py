class Assignment:
    def __init__(self, **attributes) -> None:
        self.id = attributes.get('id', '')
        self.executor_id = attributes['executor_id']
        self.role_id = attributes['role_id']
