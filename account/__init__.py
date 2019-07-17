import logging
from pyramid.config import Configurator
from account.register import RegisterController
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)


def add_route_handler(config, name, route, handler):
    config.add_route(name=name, pattern=route, request_method="POST")
    config.add_view(view=handler, route_name=name)


def main(global_config, **settings):
    config = Configurator(settings=settings)
    engine = create_engine(settings["postgres.account.url"])
    session = sessionmaker(engine)()

    def get_db_session(req):
        return session

    def get_db_engine(req):
        return engine

    config.add_request_method(get_db_session, "account_db_session", property=True)
    config.add_request_method(get_db_engine, "account_db_engine", property=True)
    register_controller = RegisterController()
    add_route_handler(config, "register", '/register', register_controller.register)

    return config.make_wsgi_app()
