from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

GRADE_CHOICES = (
    ('PK', 'Pre-Kindergarten'),
    ('K', 'Kindergarten'),
    ('1', 'Grade 1'),
    ('2', 'Grade 2'),
    ('3', 'Grade 3'),
    ('4', 'Grade 4'),
    ('5', 'Grade 5'),
    ('6', 'Grade 6'),
    ('7', 'Grade 7'),
    ('8', 'Grade 8'),
    ('9', 'Grade 9'),
    ('10', 'Grade 10'),
)


HOUSE_CHOICES = (
    ('Red', 'Spiritual Red'),
    ('Purple', 'Truthful Purple'),
    ('Blue', 'Active Blue'),
    ('Green', 'Responsible Green'),
    ('Orange', 'Studious Orange'),
)

LANGUAGE_CHOICES = (
    ('English', 'English'),
    ('Chinese', 'Chinese'),
    ('Other', 'Other'),
)

RELIGION_CHOICES = (
    ('Buddhism', 'Buddhism'),
    ('Catholic', 'Catholic'),
    ('Islam', 'Islam'),
    ('Jehovahs Witnesses', 'Jehovahs Witnesses'),
    ('Taoism', 'Taoism'),
    ('Yiguandao', 'Yiguandao'),
    ('Protestantism', 'Protestantism'),
    ('Other', 'Other'),
)


class Student(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    studentID = models.CharField(max_length=8)
    email = models.EmailField(default=' @disk.kh.edu.tw')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default='PK')
    house = models.CharField(max_length=6, choices=HOUSE_CHOICES, default='Spiritual Red')
    birthday = models.DateField(default='YYYY-MM-DD')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')
    country = CountryField(default='TW')
    motherTongue = models.CharField(max_length=7, choices=LANGUAGE_CHOICES, default='Chinese')
    religion = models.CharField(max_length=32, choices=RELIGION_CHOICES,  default='Catholic')
    guardian = models.CharField(max_length=32, default='Parent Name')
    relationship = models.CharField(max_length=32, default='Parent')
    guardianContactNumber = models.CharField(max_length=10)
    guardianEmail = models.EmailField(default='@gmail.com')
    owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE, default='dearcharlyn')

    def __str__(self):
        return self.firstname + " " + self.lastname

    def get_absolute_url(self):
        return reverse('student-details', kwargs={'pk': self.pk})
