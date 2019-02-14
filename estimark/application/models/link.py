class Link:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.predecessor_id = attributes['predecessor_id']
        self.successor_id = attributes['successor_id']
