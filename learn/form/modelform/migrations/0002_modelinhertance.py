# Generated by Django 4.2.3 on 2023-08-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelinhertance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=70)),
                ('teacher_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
