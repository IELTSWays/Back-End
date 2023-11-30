from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models.user_manager import UserManager

class User(AbstractUser):

    phone_regex = RegexValidator(
        regex=r"^09\d{9}",
        message="{}\n{}".format(
            _("Phone number must be entered in the format: '09999999999'."),
            _("Up to 11 digits allowed."),
        ),
    )

    username = None
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex],max_length=11,blank=False,unique=True,null=False)
    email = models.EmailField(max_length=70,null=True,blank=True,unique=True)
    first_Language = models.CharField(max_length=50,null=True,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    #province =
    #city =
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return str(self.phone_number) +' | '+ str(self.first_name) +' | '+ str(self.last_name)

