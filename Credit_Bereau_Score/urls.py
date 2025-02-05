from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_score.as_view(), name='index')
]
