from django.db import models
from django.contrib.auth.models import PermissionsMixin,
                                        AbstractBaseUser,
                                        BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_staff = Flase
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email_)

class CadenzaUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    company = models.CharField(max_length=75)
    title = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'company']
    USERNAME_FIELD = 'email'

    objects = CustomAccountManager()

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email
