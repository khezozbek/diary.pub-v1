from importlib.resources import _

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class Student(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_(
            "Ushbu foydalanuvchining ruxsatlari. Foydalanuvchi barcha ruxsatlarni oladi \n"
            "ularning har bir guruhiga beriladi."
        ),
        related_name='student_user_set',  # Add a related_name to avoid clash
        related_query_name='student',
    )
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    img = models.ImageField(upload_to='student_img/')
    groups = models.ManyToManyField('Group', blank=True, null=True)
    achieved_results = models.TextField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=5, decimal_places=2,  blank=True, null=True)
    is_staff = models.BooleanField(default=False,  blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=100)


class CompletedTopic(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100)


class Lesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    unit = models.CharField(max_length=100)
    grammar = models.TextField()
    vocabulary = models.TextField()
    homework = models.TextField()


class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()


class Teacher(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_(
            "Ushbu foydalanuvchining ruxsatlari. Foydalanuvchi barcha ruxsatlarni oladi \n"
            "ularning har bir guruhiga beriladi."
        ),
        related_name='teacher_user_set',
        related_query_name='teacher',
    )
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='teachers/')
    groups = models.ManyToManyField(Group, blank=True, null=True)
    class_start_time = models.TimeField(blank=True, null=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
