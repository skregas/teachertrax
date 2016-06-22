from django.conf.urls import url
from teachertrax import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^teachers/', views.teachers, name='teachers'),
	url(r'^courses/', views.courses, name='courses')
]