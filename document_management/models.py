from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from document_management.validators import FileValidator

class UserManager(DefaultUserManager):
    pass

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Document(models.Model):
    
    
    FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('docx', 'DOCX'),
        ('txt', 'TXT'),
        ('file', 'FILE'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    file = models.FileField(upload_to='documents/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    shared_with = models.ManyToManyField(User, related_name='shared_documents')
    version = models.IntegerField(default=1)

    def __str__(self):
        return self.title
