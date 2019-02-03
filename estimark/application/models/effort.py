class Effort:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.kind = attributes['kind']
        self.units = attributes['units']
        self.amount = attributes['amount']
