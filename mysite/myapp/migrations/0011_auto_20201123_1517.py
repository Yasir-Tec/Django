# Generated by Django 3.1.3 on 2020-11-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20201123_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='Email not found', max_length=150, unique=True),
        ),
    ]
