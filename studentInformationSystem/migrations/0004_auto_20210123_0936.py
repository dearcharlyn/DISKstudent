# Generated by Django 3.1.5 on 2021-01-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentInformationSystem', '0003_auto_20210123_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=32),
        ),
    ]
