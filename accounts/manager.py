
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
        custom user manager.for creating users in django shell we must enter username, phone, email and password
        gender is optional
    
    """
    def create_user(self, username, phone_number, email, password,gender=3):
        if not username:
            raise ValueError('username is not entered!!!')
        if not phone_number:
            raise ValueError('phone number is not entered!!!')
        if not email:
            raise ValueError('email is not entered!!!')
        if not password:
            raise ValueError('password is not entered!!!')
        user = self.model(
            username=username, phone_number=phone_number, email=self.normalize_email(email),gender=gender)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, email, password,gender=3):
        user = self.create_user(
            username=username, phone_number=phone_number, email=email, password=password,gender=gender)
        user.superuser = True
        user.staff = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, phone_number, email, password,gender=3):
        user = self.create_user(
            username=username, phone_number=phone_number, email=email, password=password,gender=3)
        user.staff = True
        user.save(using=self._db)
        return user
