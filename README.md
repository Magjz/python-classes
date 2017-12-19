# python-classes

Create a class “Sendable”.
It has 6 attributes following the rules below:
• _body: Constructor parameter
• _subject: Constructor parameter
• _from: Constructor parameter
• _to: Constructor parameter
• _created_at: set during initialize at the current Time
• _updated_at: set during initialize at the current Time
• _sent_at: set during initialize at None

Now, you have to create two files with two classes “Email” and “Sms”.
They inherit from Sendable.
Email and Sms use the Parent constructor.
Email takes the same parameters as before, and Sms only takes “body”, “from”, and “to” parameters.
Furthermore, in Sendable, add a method “send”. It sets the attribute “sent_at” to the current Time, but only one
time.
Calling this method twice must raise an Exception “DataAlreadySent” with no message
