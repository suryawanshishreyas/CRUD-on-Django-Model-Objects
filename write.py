# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


# Your code starts from here:
def write_instructors():
    #adding instructors
    #creating a user
    user_john = User(first_name='John', last_name='Doe', dob=date(1992,6,15))
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=6999)
    #updating the user reference of instructor_john to be user_john
    instructor_john.user = user_john
    instructor_john.save()

    instructor_yan = Instructor(first_name = 'Yan', last_name = 'Li', dob= date(1986,2,22), full_time=True, total_learners=6999)
    instructor_yan.save()

    instructor_joy = Instructor(first_name = 'Joy', last_name = 'Boy', dob = date(1983,3,21), full_time=False, total_learners=1004)
    instructor_joy.save()

    instructor_peter = Instructor(first_name = 'Peter', last_name='Feter', dob=date(1976,4,12), full_time=True, total_learners=2002)
    instructor_peter.save()
    print("Instructor objects all saved...")

def write_courses():
    #adding courses
    course_cloud_app = Course(name = "Cloud Application development with Database",
    description="Develop and deploy application on cloud")

    course_cloud_app.save()

    course_python = Course(name = "Introduction to Python",
    description='Learn Core Concepts of python')
    course_python.save()

    print("Course objects all saved...")

def write_lessons():
#adding lessons
    lesson1 = Lesson(title='Lesson 1', content='Object-relational mapping project')
    lesson1.save()
    lesson2 = Lesson(title = 'Lesson 2', content = 'Django Full Stack Project')
    lesson2.save()
    print("Lesson objects all saved...")

def write_learners():
    #adding learners
    learner_james = Learner(first_name='James', last_name='Smith', dob=date(1982, 7, 16),
                            occupation='data_scientist',
                            social_link='https://www.linkedin.com/james/')
    learner_james.save()
    learner_mary = Learner(first_name='Mary', last_name='Smith', dob=date(1992, 6, 12),
                            occupation='student',
                            social_link='https://www.linkedin.com/mary/')
    learner_mary.save()
    leaner_robert = Learner(first_name='Robert', last_name='Lee', dob=date(1992, 1, 2),
                            occupation='student',
                            social_link='https://www.linkedin.com/robert/')
    leaner_robert.save()
    learner_david = Learner(first_name='David', last_name='Smith', dob=date(1983, 7, 16),
                            occupation='developer',
                            social_link='https://www.linkedin.com/david/')
    learner_david.save()
    learner_john = Learner(first_name='John', last_name='Smith', dob=date(1986, 3, 16),
                           occupation='developer',
                           social_link='https://www.linkedin.com/john/')
    learner_john.save()
    learner_shreyas = Learner(first_name='Shreyas', last_name='Suryawanshi',dob=date(1997,4,22),
                              occupation='student', 
                              social_link='https://www.linkedin.com/suryawanshi-shreyas-full-stack-developer')
    print("Learner objects all saved...")


def clean_data():
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()

clean_data()
write_courses()
write_instructors()
write_lessons()
write_learners()