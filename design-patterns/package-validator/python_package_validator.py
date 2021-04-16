from validators import PathValidator, PythonFileValidator, JsonFileValidator

import os

class PythonPackageValidator:
    '''Implements the python package validator
    '''
    def __init__(self, module_name):
        self.module_name = module_name
        curdirmodule = os.path.join(os.path.curdir, module_name)
        self.paths = [
            # TODO: Make that a package could be validated being outside the curdir
            PathValidator(os.path.join(curdirmodule, 'applications')),
            PathValidator(os.path.join(curdirmodule,'configurations')),
            PathValidator(os.path.join(curdirmodule, module_name))
        ]

        self.pythonFiles = []
        _pythonFiles = self.__get_python_files()
        for name in _pythonFiles:
            self.pythonFiles.append(PythonFileValidator(name))

        self.jsonFiles = [
            JsonFileValidator(os.path.join(curdirmodule, 'config'),
                              mandatory_fields=['platform_version', 'package_goal'])
        ]

    def __get_python_files(self):
        python_files = []
        curdirmodule = os.path.join(os.path.curdir, self.module_name, self.module_name)
        for root, dirs, files in os.walk(curdirmodule):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(file)
        return python_files

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