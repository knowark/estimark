from .entity import Entity


class Assignment(Entity):
    def __init__(self, **attributes) -> None:
        super().__init__(**attributes)
        self.executor_id = attributes['executor_id']
        self.role_id = attributes['role_id']
