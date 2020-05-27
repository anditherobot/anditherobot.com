# Generated by Django 3.0.6 on 2020-05-27 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_workaccomplishment_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_message', models.CharField(max_length=1000, verbose_name='Message')),
            ],
        ),
    ]