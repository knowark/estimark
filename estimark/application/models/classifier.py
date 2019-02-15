class Classifier:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.name = attributes['name']
        self.amount = attributes['amount']
        self.units = attributes.get('units', 'days')
