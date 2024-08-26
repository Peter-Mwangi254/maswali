import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.public_id, filename)


class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError) :
            return Http404
        
    def create_user(self, username, email, password=None, **kwargs):
        '''
        Create and return a `User` with an email, username and password
        '''
        if username is None:
            raise TypeError('Users must have a username. ')
        if email is None:
            raise TypeError('Users must have an email and password')
        if password is None:
            raise TypeError('Users must have an email and password')
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, password=None, **kwargs):
        '''
        Create and return a `User` with superuser (admin) permissions
        '''
        if password is None or email is None:
            raise TypeError('Superuser must have a password and email.')
        if username is None:
            raise TypeError('Superusers must have a username')
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    website_url = models.URLField(blank=True, max_length=2000)
    bio = models.TextField(blank=True)
    twitter_url = models.URLField(blank=True, max_length=2000)
    github_url = models.URLField(blank=True, max_length=2000)
    linkedin_url = models.URLField(blank=True, max_length=2000)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"