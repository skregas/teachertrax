from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	content ='<a href="teachers">Teachers</a> <br />'
	content +='<a href="courses">Courses</a> <br />'
	content += "This is the Home Page"
	return HttpResponse(content)

def teachers(request):
	content ='<a href="/teachertrax">Home</a> <br />'
	content +='<a href="../courses">Courses</a> <br />'
	content += "This is the Teachers Page"
	return HttpResponse(content)

def courses(request):
	content ='<a href="/teachertrax">Home</a> <br />'
	content +='<a href="../teachers">Teachers</a> <br />'
	content += "This is the Courses Page"
	return HttpResponse(content)
