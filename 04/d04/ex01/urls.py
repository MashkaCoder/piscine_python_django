from django.urls import path
from .views import *

urlpatterns=[
	# path('ex01', display),
	path('ex01/display', display),
	path('ex01/django', django),
	path('ex01/templates', templates),
]
