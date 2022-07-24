# Generated by Django 2.2.16 on 2022-06-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220629_1027'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='customuser',
            name='reserve_username_me',
        ),
        migrations.AddConstraint(
            model_name='customuser',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, username__iexact='ME'), name='reserve_username_me'),
        ),
    ]
