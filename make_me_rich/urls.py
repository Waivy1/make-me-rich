from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index_page'),
    path('pay/<int:amount>', views.Pay.as_view(), name='pay'),
    path('sign_up', views.SignUp.as_view(), name='sign_up'),
    path('exit', views.Exit.as_view(), name='exit'),
    path('login', views.Login.as_view(), name='login'),
    path('features', views.Features.as_view(), name='features'),
    path('about', views.About.as_view(), name='about'),
    path('history', views.History.as_view(), name='history'),


]
