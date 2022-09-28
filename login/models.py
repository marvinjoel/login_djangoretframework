from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from login.manager import MyUserManager


class User(AbstractBaseUser):

    contry_choices = (
        ('P', 'PERU'),
        ('B', 'BOLIVIA'),
    )
    email = models.EmailField(verbose_name='email address', max_length=255,  unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    contry = models.CharField(max_length=7, choices=contry_choices, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin