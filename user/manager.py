from django.contrib.auth.models import BaseUserManager, AbstractUser


class Custom_manager(BaseUserManager):

    #       <-----------------General_User_Model----------------->
    def create_user(self, phone, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)

        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
#       <-----------------Super_User_Model----------------->

    def create_superuser(self, phone, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phone, email, password, **extra_fields)
