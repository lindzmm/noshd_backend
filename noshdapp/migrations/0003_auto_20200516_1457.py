# Generated by Django 3.0.6 on 2020-05-16 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noshdapp', '0002_userfollowing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfollowing',
            old_name='following_user_id',
            new_name='following_user_username',
        ),
        migrations.RenameField(
            model_name='userfollowing',
            old_name='user_id',
            new_name='user_username',
        ),
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('user_username', 'following_user_username')},
        ),
    ]