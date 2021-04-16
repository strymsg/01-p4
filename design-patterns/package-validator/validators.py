from abc import ABC, abstractmethod

import os
from os import path
import re
from error_handlers import ValidatorError, ErrorStack

class AbstractValidator:
    def __init__(self, module_name, mandatory=True):
        self.module_name = module_name
        self.mandatory = mandatory
        self.error_stack = ErrorStack()

    @abstractmethod
    def validate(self):
        pass

    def add_error(self, message, exception=None):
        ve = ValidatorError(message, exception)
        self.error_stack.add_error(ve)

    def show_errors(self):
        print('Error Stack:')
        for validation_error in self.error_stack:
            print()
            validation_error.show()

class PathValidator(AbstractValidator):
    def __init__(self, regex='', type='folder'):
        self.regex = regex
        self.type = type
        self.error = None # initialize empty

    # overriding
    def validate(self):
        '''
        Validates if the path exists. If self.regex exists it
        check if some directory matches
        :return:
        '''
        if not path.exists(self.module_name):
            self.handle_error(f'Path {self.module_name} does not exist')

        if self.regex != '':
            regex = re.compile(self.regex)
            matches = False
            try:
                for root, dirs, files in os.walk(self.module_name):
                    for file in files:
                        if regex.match(file):
                            matches = True
                            break
                    if matches is True:
                        break
                if matches is False:
                    super().add_error(
                        f'Path {self.module_name} does not matches regex {self.regex}')
            except Exception as E:
                super().add_error(f'Error finding path {path}', E)

    def handle_error(self, message):
        super().add_error(f'Path {self.module_name} does not exist')

class AbstractFileValidator(AbstractValidator):
    def __init__(self, extension):
