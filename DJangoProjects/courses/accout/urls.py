from django.urls import path
from accout import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	path('hi',views.msg,name='hi'),
	path('home/',views.home,name='home'),
	path('signUp/',views.signUp,name='signUp'),
	path('signIn/',auth_views.LoginView.as_view(template_name="accout/signIn.html"),name='signIn'),
	path('signOut/',auth_views.LogoutView.as_view(template_name='accout/signOut.html'),name='signOut'),
	path('addCourse/',views.addCourse,name='addCourse'),
	path('showCorseInfo/',views.showCorseInfo,name='showCorseInfo'),
]
