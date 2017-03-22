from django.conf.urls import url
from teachertrax import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^teacher/(?P<teacher_name_slug>[\w\-]+)/$',
        views.teacher, name='teacher'),
    url(r'^teachers/add_teacher/$', views.add_teacher, name='add_teacher'),
	url(r'^courses/', views.courses, name='courses')
]