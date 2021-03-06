from django.shortcuts import render
from django.http import HttpResponse

from teachertrax.models import Teacher, Course
from teachertrax.forms import TeacherForm, CourseForm

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
    context = {}
    t = 'teachertrax/teachers.html'
    teachers_list = Teacher.objects.order_by('name')
    context['teachers'] = teachers_list
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, t, context)

def teacher(request, teacher_name_slug):
    context = {}
    t = 'teachertrax/teacher.html'
    # Find and display information about the teacher matching the given name
    # If we can't, raise a DoesNotExist exception
    teacher = Teacher.objects.get(slug=teacher_name_slug)
    context['teacher'] = teacher
    
    fellow_teacher = teacher.other_teacher(teacher.last_course)
    context['fellow_teacher'] = fellow_teacher
    
    # Get all the courses for the current teacher
    courses = Course.objects.filter(
                                teachers__name__contains=teacher.name).order_by('date')
   
    context['courses'] = courses
    return render(request, t, context)
    
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            t = form.save(commit=True)
            # redirect to the teacher list page
            return teachers(request)
        else:
            #errors
            print(form.errors)
    else:
        # request == 'GET'
        form = TeacherForm()
        
    # render all the things!
    return render(request, 'teachertrax/add_teacher.html', {'form': form})
    
def courses(request):
    context = {}
    t = 'teachertrax/courses.html'
    course_list = Course.objects.order_by('-date')
    context['courses'] = course_list
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, t, context)

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            c = form.save(commit=True)
            # redirect to the teacher list page
            print(c, c.city, c.date)
            return courses(request)
        else:
            #errors
            print(form.errors)
    else:
        # request == 'GET'
        form = CourseForm()
        
    # render all the things!
    return render(request, 'teachertrax/add_course.html', {'form': form})
