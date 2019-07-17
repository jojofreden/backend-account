import logging

from pyramid.response import Response

from account.models import Account

logger = logging.getLogger(__name__)


class RegisterController:

    def register(self, request):
        account = Account(
            username=request.params['username'],
        )

        request.account_db_session.add(account)
        request.account_db_session.commit()

        return Response()
