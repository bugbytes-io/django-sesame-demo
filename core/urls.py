from django.urls import path
from . import views
from sesame.views import LoginView


urlpatterns = [
    path('', views.index, name='index'),
    path("sesame/login/", LoginView.as_view(), name="sesame-login"),
]
