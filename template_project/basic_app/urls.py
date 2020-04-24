from django.conf.urls import url

from basic_app import views

#TEMPLATE TAGGING

app_name='basic_app'

urlpatterns=[
	url('register/', views.register, name='register'),
	url('user_login/', views.user_login, name='user_login'),
	url('relative/', views.relative, name='relative'),
	url('other/', views.other, name='other'),
	url('basic/', views.basic, name='basic'),
	url('index/', views.index, name='index'),

]