from django.urls import path
from . import views


urlpatterns=[
    # path('',views.phello,name='phello'),
    path('',views.index, name="index"),
    path('loginpage2',views.loginpage2, name= 'loginpage2'),
    path('contact_mail',views.contact_mail, name= 'contact_mail'),
]