from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# User Models

class HeartBeat(models.Model):
    beat = models.BooleanField()


class CoreUserProfile(models.Model):
    user = models.OneToOneField(User, related_name='coreuserprofile', on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        CoreUserProfile.objects.create(user=instance)
    instance.coreuserprofile.save()


# Data Models

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    start_date: date = models.DateField()
    end_date: date = models.DateField()
    is_current = models.BooleanField(default=False)
    summary = models.CharField(max_length=500)
    skills = models.CharField(max_length=500)

    def __str__(self):
        return self.company_name


class WorkAccomplishment(models.Model):
    accomplishment = models.CharField(max_length=500)
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)

    def __str__(self):
        return self.accomplishment


class ContactMessage(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_message = models.CharField(max_length=1000, verbose_name="Messages")

    def __str__(self):
        return self.contact_name + self.contact_message


class SkillWidget(models.Model):
    pass

class PicturePost(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.description

class TextPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    is_draft = models.BooleanField(default=True)
    date_published = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class ResetDayCounter(models.Model):
    counter = models.IntegerField()

   







