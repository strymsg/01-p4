#  python validator test
from python_package_validator import PythonPackageValidator

if __name__ == '__main__':
    pValidator = PythonPackageValidator('package-examples/py1')
    pValidator.validate()
    pValidator.show_errors()