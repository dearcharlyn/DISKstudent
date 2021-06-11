# Generated by Django 3.1.5 on 2021-01-23 10:08

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('studentInformationSystem', '0004_auto_20210123_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='citizenship',
        ),
        migrations.AddField(
            model_name='student',
            name='country',
            field=django_countries.fields.CountryField(default='TW', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(default='YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default=' @disk.kh.edu.tw', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('PK', 'Pre-Kindergarten'), ('K', 'Kindergarten'), ('1', 'Grade 1'), ('2', 'Grade 2'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('5', 'Grade 5'), ('6', 'Grade 6'), ('7', 'Grade 7'), ('8', 'Grade 8'), ('9', 'Grade 9'), ('10', 'Grade 10')], default='PK', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='house',
            field=models.CharField(choices=[('Red', 'Spiritual Red'), ('Purple', 'Truthful Purple'), ('Blue', 'Active Blue'), ('Green', 'Responsible Green'), ('Orange', 'Studious Orange')], default='Spiritual Red', max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentID',
            field=models.CharField(max_length=8),
        ),
    ]
