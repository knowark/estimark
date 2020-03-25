from .entity import Entity


class Effort(Entity):
    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.kind = attributes['kind']
        self.units = attributes['units']
        self.amount = attributes['amount']
