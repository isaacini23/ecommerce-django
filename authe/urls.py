from django.urls import path, re_path
from authe import views


app_name = 'authe'

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.login_page, name='login_page'),
	path('logout/', views.logout_page, name='logout_page'),
	path('change/', views.ChangePassword2.as_view(), name='change'),
]
