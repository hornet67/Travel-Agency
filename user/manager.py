from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomManager(BaseUserManager):
    # general User
    def create_user(self, email, password, first_name, last_name, address, **other_fields):
        if not email:
            raise ValueError(_("Pls Give an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, address=address ** other_fields)

        user.set_password(password)
        user.save()
        return user

    # Super user
    def create_superuser(self, email, password, first_name, last_name, address, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(self, email, password, first_name, last_name, address, **other_fields)
