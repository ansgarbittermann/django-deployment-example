# Generated by Django 2.1.2 on 2018-10-25 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20181025_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio',
            new_name='portfolio_site',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='picture',
            new_name='profile_pic',
        ),
    ]
