# Generated by Django 4.2.3 on 2023-09-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='createview_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='namee')),
                ('email', models.EmailField(max_length=254, verbose_name='emaill')),
                ('password', models.CharField(max_length=50, verbose_name='passwordd')),
            ],
        ),
    ]
