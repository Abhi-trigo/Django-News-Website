# Generated by Django 2.2.3 on 2019-07-29 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.Users')),
            ],
        ),
    ]
