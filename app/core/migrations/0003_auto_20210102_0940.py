# Generated by Django 2.1.15 on 2021-01-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210102_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
