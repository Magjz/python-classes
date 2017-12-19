import time

class Sendable: 
    def __init__(self, **kwargs):
        self._body = kwargs['body']
        self._subject = kwargs['subject']
        self._from = kwargs['_from']
        self._to = kwargs['to']
        self._created_at = time.strftime("%A %d %B %Y %H:%M:%S")
        self._updated_at = time.strftime("%A %d %B %Y %H:%M:%S")
        self._sent_at = None

    def send(self): 
        try: 
            if self._sent_at != None: 
                raise ValueError("data already sent")
        except ValueError as DataAlreadySent:
            pass
        else:
            self._sent_at = time.strftime("%A %d %B %Y %H:%M:%S")

