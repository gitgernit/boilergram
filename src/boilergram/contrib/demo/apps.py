from boilergram.apps import AppConfig
from .routers import demo_router


class DemoConfig(AppConfig):
    router = demo_router
