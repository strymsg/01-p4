from abc import ABC, abstractmethod

import os
from os import path
import re
import py_compile
import json
from error_handlers import ValidatorError, ErrorStack

class AbstractValidator:
    '''
    Abstract File Validator Class, contains basic attributes and methods
    to be implemented.
    '''
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
    def __init__(self, module_name, mandatory=True,
                 regex='', type='folder'):
        self.module_name = module_name
        self.mandatory = mandatory
        self.error_stack = ErrorStack()
        self.regex = regex
        self.type = type
        self.error = None # initialize empty

    # overriding
    def validate(self):
        '''
        Validates if the path exists. If self.regex exists it
        check if some directory matches
        :return: Error stack
        '''
        if not path.exists(self.module_name):
            self.handle_error(f'Path {self.module_name} does not exist')
            return self.error_stack

        if not path.isdir(self.module_name):
            self.handle_error(f'{self.module_name} is not a directory')
            return self.error_stack

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
                    self.handle_error(
                        f'Path {self.module_name} does not matches regex {self.regex}'
                    )
            except Exception as E:
                self.handle_error(f'Error finding path {path}', E)
                return self.error_stack

    def handle_error(self, message, exception=None):
        super().add_error(message, exception)

class AbstractFileValidator(AbstractValidator):
    def __init__(self, module_name, extension,
                 mandatory=True):
        self.module_name = module_name
        self.mandatory = mandatory
        self.error_stack = ErrorStack()
        self.extension = extension

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def handle_error(self, message, exception):
        pass

class PythonFileValidator(AbstractFileValidator):
    def __init__(self, module_name, version='3', mandatory=True):
        self.module_name = module_name
        self.mandatory = mandatory
        self.error_stack = ErrorStack()
        self.extension = 'py'
        self.version = version

    def validate(self):
        '''
        Validates if the python file exists, if not or if an exception
        was generated it adds to the error stack
        TODO: Add validation of self.version
        :return: Error stack
        '''
        if not path.exists(self.module_name):
            self.handle_error(f'Python file {self.module_name} does not exist')
            return
        try:
            py_compile(self.module_name)
        except Exception as E:
            self.handle_error(f'python file {self.module_name} caused exception',
                              E)

    def handle_error(self, message, exception=None):
        '''
        Adds the error to the error Stack
        :param message(string): error message
        :param exception: Exception if generated
        :return: None
        '''
        super().add_error(message, exception)

class JsonFileValidator(AbstractFileValidator):
    def __init__(self, module_name, mandatory_fields=[],
                     mandatory=True):
        self.module_name = module_name
        self.mandatory = mandatory
        self.error_stack = ErrorStack()
        self.extension = 'json'
        self.mandatory_fields = mandatory_fields

    def handle_error(self, message, exception):
        '''Adds the error to the error Stack
         :param message(string): error message
        :param exception: Exception if generated
        :return: None            '''
        super().add_error(message, exception)

    def validate(self):
        '''
        Validates if the self.module_name exists and if it is a valid
        json file, also checks if the json file contains the
            self.mandatory_fields fields
            :return: Error stack
            '''
        if not path.exists(self.module_name):
            self.handle_error(f'Python file {self.module_name} does not exist')
            return

        try:
            f = open(self.module_name)
            data = json.load(f)
            for field in self.mandatory_fields:
                if field not in data:
                    self.handle_error(
                        f'"{field}" not found in file {self.module_name}'
                    )
            return self.error_stack

        except Exception as E:
            self.handle_error(
                f'Error opening Javascript file {self.module_name}',
                E)