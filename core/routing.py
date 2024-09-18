# from django.urls import path
# from . import consumers

# websocket_urlpatterns = [
#     path('ws/somepath/', consumers.MyConsumer.as_asgi()),
# ]


# app2/routing.py
from django.urls import path
from .consumers import GreetingConsumer

websocket_urlpatterns = [
    path('ws/receive/', GreetingConsumer.as_asgi()),
]
