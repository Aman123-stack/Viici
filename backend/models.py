from django.db import models
import uuid
from base.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import django.utils.timezone as timze;
# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self, email, Firstname,Lastname ,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            Firstname=Firstname,
            Lastname=Lastname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
#testing
    def create_superuser(self, email, Firstname, Lastname,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            Firstname=Firstname,
            Lastname=Lastname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    


class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True,default=uuid.uuid4, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    objects=UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Firstname','Lastname']
    class  Meta:
        db_table = 'user'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Post(models.Model):
    post_desc=models.CharField(max_length=400)
    post_title=models.CharField(max_length=150)
    post_content=models.TextField()
    post_user=models.ForeignKey(User,to_field='user_id', on_delete=models.CASCADE)
    post_created_at = models.DateTimeField(auto_now_add=True)
    class  Meta:
        db_table = 'PostUser'