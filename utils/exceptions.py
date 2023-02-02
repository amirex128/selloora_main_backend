from rest_framework.exceptions import APIException
from rest_framework import status


class NotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'موردی یافت نشد'
    default_code = 'invalid'
