from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context = {'boldmessage': "I'm bold from the the context"}
	t = 'teachertrax/index.html'
	# Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	return render(request, t, context)

def teachers(request):
	context = {'boldmessage': "I'm bold from the the context"}
	t = 'teachertrax/teachers.html'
	# Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	return render(request, t, context)

def courses(request):
	context = {'boldmessage': "I'm bold from the the context"}
	t = 'teachertrax/courses.html'
	# Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	return render(request, t, context)

