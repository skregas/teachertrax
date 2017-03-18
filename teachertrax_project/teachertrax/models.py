from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class TeacherManager(models.Manager):
    # Custom manager for the Teacher class
    def _set_availablity(self):
        try:
            self.last_course
        except ObjectDoesNotExist: # What is the empty QuerySet exception?
            # no courses
            self.is_available_for_invitation = True
        else:
            if last_course is not None and last_course.city != self.city:
                self.is_available_for_invitation = True
            else: 
                self.is_available_for_invitation = False

class Teacher(models.Model):
    name = models.CharField(max_length=128, unique=True)
    city = models.CharField(max_length=50)
    is_available_for_invitation = models.BooleanField()
    slug = models.SlugField()
    
    objects = TeacherManager()
    
        
    def save(self, *args, **kwargs):
        # Override the built-in save() method to slugify a teacher's name
        # Comment if you want the slug to change every time the name changes
        if self.id is None:
            self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Teacher, self).save(*args, **kwargs)
    
    @property
    def last_course(self):
        # Return the last course
        last_course = Course.objects.all().order_by('date').last()
        return last_course
        
    @property
    def last_home_course(self):
        # Return the most recent course taught in the teacher's 
        # home city
        last_home_course = Course.objects.filter(city=self.city).order_by('date').last()
        return last_home_course
 
    @property
    def last_away_course(self):
        # Return the most recent course where this teacher was the visitor
        last_away_course = Course.objects.exclude(city=self.city).order_by('date').last()
        return last_away_course
        
    
    def other_teacher(self, course):
        # Return the name of the other teacher for a given course.
        other_teacher = course.teachers.exclude(name=self.name)
        return other_teacher.values()[0]['name']
    
    def __str__(self):
        return self.name
        
    def __unicode(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Teachers'

     
class Course(models.Model):
    teachers = models.ManyToManyField(Teacher)
    city = models.CharField(max_length=50)
    date = models.DateField()


    def __str__(self):
        return self.city + ' ' + str(self.date)
        
    def __unicode(self):
        return self.city + ' ' + str(self.date)
    
    class Meta:
        verbose_name_plural = 'Courses'