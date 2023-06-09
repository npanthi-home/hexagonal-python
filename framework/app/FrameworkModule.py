from injector import Module, singleton
from framework.mysql.SessionFactory import SessionFactory


class FrameworkModule(Module):
    def configure(self, binder):
        binder.bind(SessionFactory, to=SessionFactory, scope=singleton)
