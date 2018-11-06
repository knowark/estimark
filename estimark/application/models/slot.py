class Slot:
    def __init__(self, **attributes):
        self.id = attributes['id']
        self.task_id = attributes['task_id']
        self.schedule_id = attributes['schedule_id']
        self.start = attributes['start']
        self.end = attributes['end']
        self.executor_id = attributes['executor_id']
