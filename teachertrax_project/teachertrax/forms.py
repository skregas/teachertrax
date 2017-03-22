from django import forms
from teachertrax.models import Teacher, Course

class TeacherForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label="Teacher's name:", help_text="Please enter the teacher's name")
    city = forms.CharField(max_length=50, label="Teacher's city:", help_text="Please enter the teacher's home city")
    is_available_for_invitation = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Teacher
        fields = ('name', 'city', 'is_available_for_invitation')
 
class CourseForm(forms.ModelForm):
    city = forms.CharField(max_length=50, label="Course location:",help_text="Please enter the course location")
    date = forms.DateField(label="Course date:", widget=forms.SelectDateWidget(
        empty_label=("Select Year", "Select Month", "Select Day")))
    teachers = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all(), to_field_name='name', label="Select the teachers of the course")
    
    class Meta:
        model = Course
        fields = ('city', 'date', 'teachers')
    
    
    
    