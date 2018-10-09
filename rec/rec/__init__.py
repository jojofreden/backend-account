import logging

#from oauthlib.oauth2 import BearerToken, AuthorizationCodeGrant
from pyramid.config import Configurator

from rec.register import register_user

logger = logging.getLogger(__name__)

def init_oauth(config):
    """Integration with OAuthLib is as smooth as possible."""
    # Validator callback functions are passed Pyramid request objects so
    # you can access your request properties, database sessions, etc.
    # The request object is populated with accessors for the properties
    # referred to in the OAuthLib docs and used by its built in types.
    validator = MyRequestValidator()

    # Register response types to create grants.
    config.add_response_type('oauthlib.oauth2.AuthorizationCodeGrant',
                             name='code',
                             request_validator=validator)

    # Register grant types to validate token requests.
    config.add_grant_type('oauthlib.oauth2.AuthorizationCodeGrant',
                          name='authorization_code',
                          request_validator=validator)

    # Register the token types to use at token endpoints.
    # The second parameter to all registrations may be left out to set it
    # as default to use when no corresponding request parameter specifies
    # the grant, response or token type. Be aware that the built in types
    # will fail if a matching request parameter is missing, though.
    config.add_token_type('oauthlib.oauth2.BearerToken',
                          request_validator=validator)

def add_route_handler(config, name, route, handler):
	config.add_route(name=name, pattern=route, request_method="POST")
	config.add_view(view=handler, route_name=name)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    add_route_handler(config, "register", '/register', register_user)
    config.scan()
    # init_oauth(config)
    return config.make_wsgi_app()

