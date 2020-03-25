from .entity import Entity


class Role(Entity):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.name = attributes['name']
