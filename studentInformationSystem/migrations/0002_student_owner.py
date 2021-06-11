# Generated by Django 3.1.5 on 2021-01-23 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studentInformationSystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='auth.user'),
            preserve_default=False,
        ),
    ]