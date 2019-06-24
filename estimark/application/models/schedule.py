class Schedule:
    def __init__(self, **attributes):
        self.id = attributes.get('id')
        self.name = attributes.get('name')
        self.state = attributes.get('state', '')
