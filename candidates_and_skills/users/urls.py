from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.SignUpView.as_view(), name='register'),
]
