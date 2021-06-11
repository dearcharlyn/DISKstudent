import django_filters
from django_filters import DateFilter, CharFilter

from.models import Student


class StudentFilter(django_filters.FilterSet):
    studentID = CharFilter(field_name='studentID', lookup_expr='icontains', label='ID')
    firstname = CharFilter(field_name='firstname', lookup_expr='icontains', label='First Name')
    lastname = CharFilter(field_name='lastname', lookup_expr='icontains', label='Last Name')
    country = CharFilter(field_name='country', lookup_expr='icontains', label='Country')
    gender = CharFilter(field_name='gender', lookup_expr='icontains', label='Gender')
    startDate = DateFilter(field_name='birthday', lookup_expr='gte', label='Birthday Start Date')
    endDate = DateFilter(field_name='birthday', lookup_expr='lte', label='End')

    class Meta:
        model = Student
        fields = ('studentID', 'firstname', 'lastname', 'gender', 'house', 'grade')

