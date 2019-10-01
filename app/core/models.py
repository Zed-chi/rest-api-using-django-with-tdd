from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra):
        """ creates and saves a new user """
        user = self.model(
            email=self.normalize_email(email),
            **extra
        )
        user.set_password(password)
        user.save(using=self._db)

        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    """ Custom User Model with email insteead name"""
    email = models.EmailField(max_length=2555, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
