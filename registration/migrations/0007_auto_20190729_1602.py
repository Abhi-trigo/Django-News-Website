# Generated by Django 2.2.3 on 2019-07-29 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_users_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='user1',
            new_name='Userid',
        ),
    ]
