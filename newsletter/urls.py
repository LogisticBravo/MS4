from django.urls import path
from . import contexts

urlpatterns = [
    path('newsletter/', contexts.newsletter, name='newsletter'),
]
