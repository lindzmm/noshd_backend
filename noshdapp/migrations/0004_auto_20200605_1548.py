# Generated by Django 3.0.6 on 2020-06-05 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noshdapp', '0003_auto_20200516_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfollowing',
            old_name='following_user_username',
            new_name='following_user_id',
        ),
        migrations.RenameField(
            model_name='userfollowing',
            old_name='user_username',
            new_name='user_id',
        ),
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('user_id', 'following_user_id')},
        ),
    ]
