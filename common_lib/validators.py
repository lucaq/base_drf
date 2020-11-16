# from common_lib.result import Result
from cerberus import Validator
validator = Validator()


def login_validator() -> Validator:
    # Usage: login_validator(v).validate(document)
    login_schema = {
        'username': {
            'type': 'string',
            'minlength': 5,
            'maxlength': 256
        },
        'password': {
            'type': 'string',
            'minlength': 8,
            'maxlength': 256
        }
    }
    validator.schema = login_schema
    return validator


class MyValidator(Validator):
    def _validate_isodd(self, isodd, field, value):
        """ Test the oddity of a value.

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if isodd and not bool(value & 1):
            self._error(field, "Must be an odd number")

    def _validate_isdigit(self, isdigit, field, value):
        """ Test the oddity of a value.

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if isdigit and not value.isdigit():
            self._error(field, "Must be a number")

    def isodd(self):
        odd_schema = {'amount': {'isodd': True, 'type': 'integer'}}
        self.schema = odd_schema

    def isdigit(self):
        digit_schema = {'amount': {'isdigit': True, 'type': 'string'}}
        self.schema = digit_schema


def verify(v, document):
    if not v or not isinstance(v, Validator):
        raise ValueError("Missing a Validator")
    print(v)
    v.schema = {'amount': {'isdigit': True, 'type': 'string'}}
    return v.validate(document)


validator = MyValidator()

if __name__ == "__main__":
    # validator = login_validator()
    # if not validator.validate({'username': 'asdf', 'password': 'asdf'}):
    #     print(v.errors)

    # schema = {'amount': {'isodd': True, 'type': 'integer'}}
    # v = MyValidator(schema)
    # if not v.validate({'amount': 10}):
    #     print(v.errors)

    v = validator

    v.isodd()
    print(v)
    if not v.validate({'amount': 10}):
        print(v.errors)

    v.isdigit()
    print(v)
    if not v.validate({'amount': 'sss'}):
        print(v.errors)

    if not verify(v, {'amount': 'sss'}):
        print(v.errors)
