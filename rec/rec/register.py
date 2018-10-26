import logging

import bcrypt
from pyramid.response import Response

from rec.models import Account

logger = logging.getLogger(__name__)


class RegisterController(object):
    def register_user(self, request):
        password = request.params['password']
        hash_pw =bcrypt.hashpw(password, bcrypt.gen_salt())
        account = Account(
            name=request.params['name'],
            password=hash_pw,
        )
        req.account_db_session.add_all(account)
        req.account_db_session.commit()
        return Response()
