# Generated by Django 3.2.10 on 2021-12-13 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='texts',
        ),
    ]
