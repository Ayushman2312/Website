# Generated by Django 4.1 on 2022-12-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone_no', models.PositiveIntegerField()),
            ],
        ),
    ]
