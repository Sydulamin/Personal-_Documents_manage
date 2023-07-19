from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from document_management.validators import FileValidator

class UserManager(DefaultUserManager):
    pass

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    user_permissions = None  # Set to None to prevent clashes with the default user_permissions field
    objects = UserManager()

    class Meta:
        swappable = 'AUTH_USER_MODEL'

class Document(models.Model):
    FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('docx', 'DOCX'),
        ('txt', 'TXT'),
        # Add more format choices as needed
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    shared_with = models.ManyToManyField(User, related_name='shared_documents')
    file = models.FileField(upload_to='documents/', validators=[FileValidator(allowed_formats=['pdf', 'docx', 'txt'], max_size=10485760)])
    version = models.IntegerField(default=1)

    def __str__(self):
        return self.title
