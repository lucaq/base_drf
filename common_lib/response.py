from rest_framework.views import Response
from common_lib.exceptions import BlueDotBaseException
from common_lib.code import Code


class ErrorResponse(Response):
    def __init__(self, e=None, code=None, msg=None):
        if code is None and msg is None and e is None:
            raise ValueError()
        if e:
            if isinstance(e, BlueDotBaseException):
                super().__init__(data=e.to_dict)
            else:
                super().__init__(data={"code": 5000, "msg": 'Inernal error'})
        else:
            super().__init__(data={"code": code, "msg": msg})


class SuccessResponse(Response):
    def __init__(self, code=Code.OK.value, msg=None, data=None):
        if code is None and msg is None:
            raise ValueError()
        super().__init__(data={"code": code, "msg": msg, "data": data})
