from django.contrib import admin
from teachertrax.models import Teacher, Course

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'is_available_for_invitation')
    list_filter = ('name', 'city', 'is_available_for_invitation')
    prepopulated_fields = {'slug':('name',)}
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ('city', 'date', 'TEACHERS')
    list_filter = ('city', 'date') 
    
    
    def TEACHERS(self, obj):
        return ", ".join([t.name for t in obj.teachers.all()])
        
    
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
