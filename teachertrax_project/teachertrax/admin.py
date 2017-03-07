from django.contrib import admin
from teachertrax.models import Teacher, Course

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'is_available_for_invitation')
    list_filter = ('name', 'city', 'is_available_for_invitation')
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ('city', 'date')
    
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
