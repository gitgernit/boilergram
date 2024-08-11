from routers import demo_router

from boilergram.apps import AppConfig


class DemoConfig(AppConfig):
    router = demo_router
