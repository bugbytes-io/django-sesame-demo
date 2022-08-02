from django.urls import path
from . import views
from sesame.views import LoginView


urlpatterns = [
    path('', views.index, name='index'),
    path('secret/', views.secret_view, name='secret'),
    path('secret-report/', views.secret_report_view, name='secret-report'),
    path('profile/<int:pk>/', views.user_profile, name='user-profile'),
    path("sesame/login/", LoginView.as_view(), name="sesame-login"),
]
