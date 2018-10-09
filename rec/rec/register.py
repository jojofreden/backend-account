import logging

from pyramid.response import Response

logger = logging.getLogger(__name__)


def register_user(request):
    logger.info("REGISTER")
    return Response()

