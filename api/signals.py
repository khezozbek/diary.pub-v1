from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Teacher, Student

@receiver(post_save, sender=Teacher)
@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(username=instance.username, password=instance.username)
