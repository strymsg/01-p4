from os import path

class ValidatorError:
    def __init__(self, errtype, message, exception):
        self.errtype = errtype
        self.message = message
        self.exception = exception

    def handle_error(self, message, exception):
        if exception is not None:
            self.errtype = type(exception)
        else:
            self.errtype = 'Generic'
        self.message = message
        self.exception = exception


class ErrorStack:
    def __init__(self, stack=[]):
        self.stack = stack

    def add_error(self, validation_error: ValidatorError):
        self.stack.append(validation_error)