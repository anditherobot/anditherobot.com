# Generated by Django 3.0.7 on 2020-08-09 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicturePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='SkillWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='contact_message',
            field=models.CharField(max_length=1000, verbose_name='Messages'),
        ),
    ]
