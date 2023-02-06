import logging

from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response

from utils import messages


def default_exception(self, e):
    logging.getLogger('apm').error('------ error in %s ------' % self.__class__, exc_info=True,
                                   extra={'error': str(e)})
    return Response({
        'error': str(e),
        "message": messages.INTERNAL_SERVER_ERROR
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class NotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'موردی یافت نشد'
    default_code = 'invalid'
