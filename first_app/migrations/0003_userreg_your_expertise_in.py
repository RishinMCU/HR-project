# Generated by Django 3.2 on 2021-05-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_userreg_imagenow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='Your_expertise_in',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
