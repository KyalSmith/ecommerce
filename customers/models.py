from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from products.models import Products


# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self,email,password=None,full_name=None,is_active=True,is_staff=False,is_superuser=False):

        if not email:
            raise ValueError("User needs an email address")
        if not password:
            raise ValueError("User needs a password")

        user_obj = self.model(email = self.normalize_email(email))
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.is_superuser = is_superuser
        user_obj.full_name = full_name
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,email,password=None,full_name=None):
        user = self.create_user(email,password=password,full_name=full_name,is_staff=True)
        return user

    def create_superuser(self,email,password=None,full_name=None):
        user = self.create_user(email,password=password,full_name=full_name,is_superuser=True,is_staff=True)
        return user

class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(max_length=255,unique=True)
    full_name = models.CharField(max_length=255,blank=True,null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.superuser



    objects = UserManager()

    def __str__(self):
        return self.email


class User_Order(models.Model):

    order_id = models.CharField(max_length=100,unique=True)
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)

class User_Cart(models.Model):

    product_link = models.ForeignKey(Products,on_delete=models.CASCADE)
    order_id = models.ForeignKey(User_Order,on_delete=models.CASCADE)




