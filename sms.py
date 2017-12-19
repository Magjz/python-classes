from sendable import Sendable

class Sms(Sendable): 
    def __init__(self, **kwargs): 
        self._body = kwargs['body']
        self._from = kwargs['_from']
        self._to = kwargs['to']


test = Sms(body="test", _from="toto", to="tata")
print(test._to)
