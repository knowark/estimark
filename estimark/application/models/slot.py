class Slot:
    def __init__(self, **attributes):
        self.id = attributes.get('id')
        self.name = attributes.get('name', '')
        self.task_id = attributes['task_id']
        self.schedule_id = attributes['schedule_id']
        self.start = attributes['start']
        self.end = attributes['end']
        self.executor_id = attributes.get('executor_id')
