from django.conf.urls import url
from teachertrax import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^teachers/', views.teachers, name='teachers'),
	url(r'^courses/', views.courses, name='courses')
]