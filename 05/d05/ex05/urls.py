from django.urls import path
from .views import *


urlpatterns = [
	path('populate/', populate),
	path('display/', display),
	path('remove/', remove)
]
