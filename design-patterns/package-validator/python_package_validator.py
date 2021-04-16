from validators import PathValidator, PythonFileValidator, JsonFileValidator

import os

class PythonPackageValidator:
    '''Implements the python package validator
    TODO: Add the python file validator for all python fles
    '''
    def __init__(self, module_name):
        self.paths = [
            PathValidator('applications'),
            PathValidator('configurations'),
            PathValidator(module_name)
        ]
        self.pythonFiles = [
            # TODO: add all python files
        ]
        self.jsonFiles = [
            JsonFileValidator('config',
                              mandatory_fields=['platform_version', 'package_goal'])
        ]

    def validate(self):
        for path in self.paths:
            path.validate()
        for pyfile in self.pythonFiles:
            pyfile.validate()
        for jsonfile in self.jsonFiles:
            jsonfile.validate()

    def show_errors(self):
        for path in self.paths:
            path.error_stack.show_errors()
        for pyfile in self.pythonFiles:
            pyfile.error_stack.show_errors()
        for jsonfile in self.jsonFiles:
            jsonfile.error_stack.show_errors()