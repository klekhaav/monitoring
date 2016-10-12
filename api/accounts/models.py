from datetime import datetime, timedelta
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.signing import TimestampSigner, b64_encode, b64_decode, SignatureExpired, BadSignature
from django.conf import settings
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import base36_to_int, int_to_base36
from django.utils.translation import ugettext_lazy as _


# extended user manager
class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.join_date = timezone.now()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name=None, last_name=None):
        user = self.create_user(email=self.normalize_email(email),
                                first_name=first_name,
                                last_name=last_name,
                                password=password)
        # Set superuser always to active
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Customer(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    join_date = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
