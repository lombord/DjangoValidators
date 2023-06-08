from django.urls import path

from .views import register, stubPage

urlpatterns = [
    path('', register, name='home'),
    path('stub-page', stubPage, name='stub-page'),
]
