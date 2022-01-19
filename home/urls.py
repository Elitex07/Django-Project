from django.urls import path
from . import views
from .admin import *

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register',views.register, name='register'),
    path('login',views.log_in, name='login'),
    path('session_end',views.log_out,name='logout'),
    path('home',views.log_in,name='home'),
    path('new_connection',views.newc,name='newc'),
    path('bookgas',views.bookgas,name='bookgas'),
    path('pay',views.pay,name='pay'),
    path('delivery',views.delivery,name='delivery'),
    path('bill_history',views.billhistory,name='billhistory'),
    path('about',views.about,name='about'),
    path('success',views.pay,name='success'),
    path('tnc',views.tnc,name='tnc')
]

#admin text
admin.site.site_header = "EZ gas Admin"
admin.site.site_title = "EZ gas Admin Portal"
admin.site.index_title = "Welcome to EZ gas"