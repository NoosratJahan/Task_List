from django.urls import path
from . import views


urlpatterns = [  
    path('', views.landing_page, name='landing'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('home/', views.home, name='home'),
    path('task_view/', views.task_view, name='task_view'),
    path('delete/<int:id>/', views.delete, name='delete')
]
