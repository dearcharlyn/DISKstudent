# Generated by Django 3.1.5 on 2021-01-14 01:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentInformationSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(default='last name', max_length=32)),
                ('studentID', models.CharField(default='20031', max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('grade', models.CharField(default='PK', max_length=32)),
                ('house', models.CharField(default='Spiritual Red', max_length=32)),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('gender', models.CharField(default='Male', max_length=6)),
                ('citizenship', models.CharField(default='Taiwanese', max_length=32)),
                ('motherTongue', models.CharField(default='Chinese', max_length=32)),
                ('religion', models.CharField(default='Catholic', max_length=32)),
                ('guardian', models.CharField(default='Parent Name', max_length=32)),
                ('relationship', models.CharField(default='Parent', max_length=32)),
                ('guardianContactNumber', models.CharField(default='0958450028', max_length=10)),
                ('guardianEmail', models.EmailField(default='guardian@gmail.com', max_length=254)),
            ],
        ),
    ]
