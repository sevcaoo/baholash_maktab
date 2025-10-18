from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, telefon_raqam, password=None, **extra_fields):
        if not telefon_raqam:
            raise ValueError("Telefon raqam kiritilishi shart.")
        user = self.model(telefon_raqam=telefon_raqam, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, telefon_raqam, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(telefon_raqam, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    otasining_ismi = models.CharField(max_length=50, blank=True, null=True)
    mutaxassisligi = models.CharField(max_length=100, blank=True, null=True)
    viloyat = models.CharField(max_length=50, blank=True, null=True)
    tuman = models.CharField(max_length=50, blank=True, null=True)
    maktab_raqami = models.CharField(max_length=10, blank=True, null=True)
    telefon_raqam = models.CharField(max_length=15, unique=True)
    sinf = models.CharField(max_length=20, blank=True, null=True)
    fan = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "telefon_raqam"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.telefon_raqam})"
