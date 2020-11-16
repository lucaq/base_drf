from rest_framework.views import exception_handler
from common_lib.response import ErrorResponse


def custom_exception_handler(exc, context):
    # 按照所有异常全部http200，data里定义异常code
    # settings中配置 'EXCEPTION_HANDLER': 'common_lib.rest_framework.custom_exception_handler'
    return ErrorResponse(exc)
