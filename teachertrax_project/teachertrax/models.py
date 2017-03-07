from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=128, unique=True)
    city = models.CharField(max_length=50)
    is_available_for_invitation = models.BooleanField()

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