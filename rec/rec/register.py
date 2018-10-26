import logging

import bcrypt
from pyramid.response import Response

from rec.models import Account

logger = logging.getLogger(__name__)


class RegisterController(object):
    def register_user(self, request):
        password = request.params['password']
        hash_pw =bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        account = Account(
            name=request.params['username'],
            password=hash_pw,
        )

        request.account_db_session.add(account)
        request.account_db_session.commit()

        return Response()
