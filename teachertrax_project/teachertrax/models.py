from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=128, unique=True)
    city = models.CharField(max_length=50)
    is_available_for_invitation = models.BooleanField()
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        # Comment if you want the slug to change every time the name changes
        if self.id is None:
            self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Teacher, self).save(*args, **kwargs)

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