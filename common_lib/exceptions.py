from common_lib.code import Code


class BlueDotBaseException(Exception):
    def __init__(self, description=""):
        super().__init__()
        self._desc = description

    @property
    def code(self):
        return Code.OK.value

    @property
    def msg(self):
        return 'Success'

    @property
    def description(self):
        return self._desc

    @property
    def to_dict(self):
        return {
            'code': self.code,
            'message': self.msg,
            'description': self.description
        }


# 初始化失败
class InitFail(BlueDotBaseException):
    def __init__(self, description=""):
        super().__init__(description)

    @property
    def code(self):
        return Code.ERR_INIT_FAIL.value

    @property
    def msg(self):
        return 'Init failure'


# 登陆用户验证错误
class InvalidLoginUserException(BlueDotBaseException):
    def __init__(self, description=""):
        super().__init__(description)

    @property
    def code(self):
        return Code.ERR_INVALID_PARAMS.value

    @property
    def msg(self):
        return 'Invalid user login information fail'

    # @property
    # def description(self):
    #     return self._desc if self._desc else 'Your login information is not correct please double confirm...'


# Params参数验证错误
# from rest_framework.exceptions import APIException, ValidationError


# class InvalidParamsException(ValidationError):
class InvalidParamsException(BlueDotBaseException):
    def __init__(self, description=""):
        super().__init__(description)

    @property
    def code(self):
        return Code.ERR_INVALID_PARAMS.value

    @property
    def msg(self):
        return 'Invalid params fail'


class InvalidPageException(BlueDotBaseException):
    def __init__(self, description=""):
        super().__init__(description)

    @property
    def code(self):
        return Code.ERR_INVALID_PAGE.value

    @property
    def msg(self):
        return 'Invalid page'


# 转换错误
class ConvertException(BlueDotBaseException):
    def __init__(self, description=""):
        super().__init__(description)

    @property
    def code(self):
        return Code.ERR_CONVERT.value

    @property
    def msg(self):
        return 'Convert error'

    @property
    def description(self):
        return self._desc if self._desc else 'The parameters of the you validation failed...'


# 用户名或密码错误
class UsernamePasswordFail(BlueDotBaseException):
    def __init__(self, description=""):
        super().__init__(description)

    @property
    def code(self):
        return Code.ERR_USERNAME_PASSWORD_FAIL.value

    @property
    def msg(self):
        return 'Username or password fail'


# 创建用户参数错误 create_user_params_validator
class CreateUserParamsException(BlueDotBaseException):
    def __init__(self, description=""):
        super().__init__(description)

    @property
    def code(self):
        return Code.ERR_CREATE_DATA_FAIL.value

    @property
    def msg(self):
        return 'Failed to create user information'


# 更新用户参数错误
class UpdateUserParamsException(BlueDotBaseException):
    def __init__(self, description=""):
        super().__init__(description)

    @property
    def code(self):
        return Code.ERR_UPDATE_DATA_FAIL.value

    @property
    def msg(self):
        return 'Failed to update user information'


# 数据不存在
class DataNotExistException(BlueDotBaseException):
    def __init__(self, description=""):
        super().__init__(description)
        self._code = Code.ERR_DATA_NOT_EXIST.value

    @property
    def code(self):
        return self._code

    @property
    def msg(self):
        return "Data Not Exist"
