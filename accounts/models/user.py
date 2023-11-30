from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models.user_manager import UserManager

class User(AbstractUser):
    user_type_choices = (
        ("normal", "normal"),
        ("admin", "admin"),
        ("staff", "staff"),
    )
    phone_regex = RegexValidator(
        regex=r"^09\d{9}",
        message="{}\n{}".format(
            _("Phone number must be entered in the format: '09999999999'."),
            _("Up to 11 digits allowed."),
        ),
    )
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    name = models.CharField(max_length=70,null=True,blank=True)
    phone_number = models.CharField(validators=[phone_regex],max_length=11,blank=False,unique=True,null=False)
    user_type = models.CharField(max_length=10, default="normal", choices=user_type_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return str(self.phone_number) +' | '+ str(self.user_type)

