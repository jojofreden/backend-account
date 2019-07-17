from account.models import base

from pyramid.paster import bootstrap

with bootstrap('development.ini') as env:
    base.metadata.create_all(env['request'].account_db_engine)
