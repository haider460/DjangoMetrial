from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class MyCustomeUser(BaseUserManager):

    def create_user(self, email, phonenumber, password, **extraFields):

        if not email:
            raise ValueError(_('The Email must be set'))

        email = self.normalize_email(email)
        user = self.model(
            email=email, phonenumber=phonenumber, ** extraFields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phonenumber, password, **extraFields):

        extraFields.setdefault('is_staff', True)
        extraFields.setdefault('is_superuser', True)
        extraFields.setdefault('is_active', True)

        if extraFields.get('is_staff') is not True:
            raise ValueError('For super user Is_staff must be true')
        if extraFields.get('is_superuser') is not True:
            raise ValueError('For super user Is_superuser must be true')
        if extraFields.get('is_active') is not True:
            raise ValueError('For super user Is_active must be true')

        return self.create_user(email, password, phonenumber, ** extraFields)


class NewUser(AbstractUser):
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phonenumber']

    objects = MyCustomeUser()

    def __str__(self):
        return self.email
