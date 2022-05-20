from django.urls import path
from . import views

app_name = 'ck_main_app'

urlpatterns = [
    path('', views.users_view, name='users'),
    path('<int:user_id>/', views.user_details, name='user_details'),
    path('your_account/', views.your_account, name='your_account'),
    path('add_skills/', views.add_skills, name='add_skills'),
]
