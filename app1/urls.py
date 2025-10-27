from django.urls import path
from . import views

urlpatterns = [

    #path('', views.home_view, name='home'),
    #path('login/', views.login_view, name='login'),
    #path('logout/', views.logout_view, name='logout'),

    path('', views.home_view1, name='index'),
    path('login/', views.login_view1, name='login'),
    path('logout/', views.logout_view1, name='logout'),

    path('set-cookie/', views.set_cookie_view, name='set-cookie'),
    path('get-cookie/', views.get_cookie_view, name='get-cookie'),
    path('set-session/', views.set_session_view, name='set-session'),
    path('get-session/', views.get_session_view, name='get-session'),

    
]