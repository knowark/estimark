class Task:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.name = attributes['name']
        self.previous = attributes.get('previous')
        self.next = attributes.get('next')
