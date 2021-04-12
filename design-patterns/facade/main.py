# facade example

class File:
    def __init__(self, name, size=1000, content='Test....', file_id=0):
        self.name = name
        self.size = size
        self.content = content
        self.file_id = file_id

    def change_name(self, name:str):
        self.name = name

class Sms:
    def __init__(self, reciever_number:int, sender_number:int, contents:str):
        self.reciever_number = reciever_number
        self.sender_number = sender_number
        self.contents = contents

    def send_message(self):
        print('Sending sms...')
        print(f'To: {self.reciever_number}\nFrom: {self.sender_number}\nContents:{self.contents}')
        print()

class Email:
    def __init__(self, to, _from, subject, contents, attachments:[]):
        self.to = to
        self._from = _from
        self.subject = subject
        self.contents = contents
        self.attachments = attachments

    def forward(self, to):
        print(f'Forwarding message to {to}')

    def send_email(self):
        print('Sending email...')
        print(f'To: {self.to}')
        print(f'from: {self._from}')
        print(f'subject: {self.subject}')
        print(f'contents: {self.contents}')
        print(f'attachments: {self.attachments}')
        print()

class InstantMessage:
    def __init__(self, reciever, sender, contents, attachments:[]):
        self.reciever = reciever
        self.sender =sender
        self.contents = contents
        self.attachments = attachments

    def send_message(self):
        print('Sending instant message...')
        print(f'to: {self.reciever}')
        print(f'sender: {self.sender}')
        print(f'contents: {self.contents}')
        print(f'attachments: ({len(self.attachments)}): {self.attachments}')
        print()

class MessageFacade:
    def __init__(self, destination, source, content, type:str, file_ids=[], emailSubject=''):
        self.destination = destination
        self.source = source
        self.content = content
        self.type = type
        self.file_ids = file_ids
        self.emailSubject = emailSubject

        self.email = None
        self.instantMessage = None
        self.sms = None

        files = []
        if len(file_ids) > 0:
            for file_id in file_ids:
                files.append(File(name='File#' + str(file_id), file_id=file_id))
        # defining behavior from type
        if type == 'email':
            self.email = Email(to=self.destination, _from=self.source, subject=self.emailSubject,
                               contents=self.content, attachments=files)
        elif type == 'instant_message':
            self.instantMessage = InstantMessage(reciever=self.destination, sender=self.source,
                                                 contents=self.content, attachments=files)
        elif type == 'sms':
            self.sms = Sms(reciever_number=self.destination, sender_number=self.source,
                           contents=self.content)
        else:
            print('Not implemented.')

    def send_message(self):
        if self.type == 'email':
            self.email.send_email()
        elif self.type == 'instant_message':
            self.instantMessage.send_message()
        elif self.type == 'sms':
            self.sms.send_message()

#### main program #####
if __name__ == '__main__':
    m1 = MessageFacade(destination='7110111', source='7098851',
                       content='This is a test sms', type='sms')
    m1.send_message()

    m2 = MessageFacade(destination='@hyemma', source='@nyco',
                       content='Hello friend, you recieve it?',
                       type='instant_message')
    m2.send_message()

    m3 = MessageFacade(destination='dom@example.org', source='luen@example.com',
                       content='Task facade done...', type='email',
                       file_ids=[100, 101], emailSubject='Test email.')
    m3.send_message()