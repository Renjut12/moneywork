from django.urls import path
from financialapp import views


urlpatterns = [

    path('',views.index,name='index'),
    path('Home/',views.Home,name='Home'),
    path('Login/',views.Login,name='Login'),
    path('Register/',views.Register,name='Register'),
    path('new/',views.new,name='new'),
    path('drop/',views.drop,name='drop'),
    path('Message/',views.Message,name='Message')


]