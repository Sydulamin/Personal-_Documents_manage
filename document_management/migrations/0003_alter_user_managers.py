# Generated by Django 4.2.3 on 2023-07-20 09:17

from django.db import migrations
import document_management.models


class Migration(migrations.Migration):

    dependencies = [
        ('document_management', '0002_alter_user_managers_user_user_permissions'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', document_management.models.UserManager()),
            ],
        ),
    ]