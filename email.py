from sendable import Sendable

class Email(Sendable): 

    def __init__(self,  **kwargs):
        Sendable.__init__(self,  **kwargs)

test = Email(body="test", _from="toto", to="tata", subject="haha")
print(test._subject)
print(test._sent_at)
test.send()
print(test._sent_at)
test.send()


