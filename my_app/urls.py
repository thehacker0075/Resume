from django.urls import path
from django.views import View
from . import views


urlpatterns = [
	path('',views.index, name='index'),
	path('contact/', views.contact, name='contact'),
]