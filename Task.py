class Task(object):
    def __init__(self, _id, _title, _desc, _done):
        self.id = _id
        self.title = _title
        self.desc = _desc
        self.done = _done


    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'desc': self.desc,
            'done': self.done
            }
