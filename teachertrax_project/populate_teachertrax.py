import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teachertrax_project.settings')

import django
django.setup()

from datetime import date, timedelta
from teachertrax.models import Teacher, Course

def populate():
    t_sr = add_teacher(name='Sri Ravi',
                city='Torreon',
                is_available=True)
                
    t_a = add_teacher(name='Avalokiteshvara',
                city='Torreon',
                is_available=True)
    
    t_d = add_teacher(name='Devima',
                city='Veracruz',
                is_available=False)
                
    t_m = add_teacher(name='Madhavi',
                city='Monterrey',
                is_available=False)
    
    add_course(city='Torreon',
                date=date.today(),
                teachers=[t_sr, t_a])
                
    add_course(city='Monterrey',
                date=date.today() - timedelta(days=20),
                teachers=[t_sr, t_m])

    add_course(city='Veracruz',
                date=date.today() + timedelta(days=40),
                teachers=[t_sr, t_d])
    
    # Print out what we have added to the user.
    for t in Teacher.objects.all():
        for c in Course.objects.filter(teachers=t):
            print("- {0} - {1}".format(str(c), str(t)))    
    
def add_teacher(name, city, is_available):
    t = Teacher.objects.get_or_create(name=name, 
                                      city=city,
                                      is_available_for_invitation = is_available)[0]
    # t.is_available_for_invitation = is_available
    t.save()
    return t

def add_course(city, date, teachers):
    c = Course.objects.get_or_create(city = city,
                                       date = date)[0]
    c.save()
    c.teachers.add(teachers[0], teachers[1])
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting TeacherTrax population script...")
    populate()