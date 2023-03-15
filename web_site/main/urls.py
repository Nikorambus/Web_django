from django.urls import path
from . import views
from .views import LoginUser, RegisterUser


urlpatterns = [
    # Здесь мы отслеживаем адреса
    # Также вызываем соответствующие функции из файла views и даём им name
    path('news', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('reg/', RegisterUser.as_view(), name='reg'),
    path('log', LoginUser.as_view(), name='log'),
    path('logout', views.logout_user, name='logout'),
]
