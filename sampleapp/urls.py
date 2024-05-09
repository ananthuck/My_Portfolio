from django.urls import path
from . import views


urlpatterns=[
    # path('',views.phello,name='phello'),
    path('',views.index, name="index"),
    path('loginpage2',views.loginpage2, name= 'loginpage2'),
]