# Generated by Django 4.1.2 on 2023-01-14 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0004_sharoyit_talim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharoyit',
            old_name='name',
            new_name='names',
        ),
        migrations.RenameField(
            model_name='sharoyit',
            old_name='rasim',
            new_name='rasims',
        ),
        migrations.RenameField(
            model_name='sharoyit',
            old_name='title',
            new_name='titles',
        ),
        migrations.RenameField(
            model_name='talim',
            old_name='name',
            new_name='namet',
        ),
        migrations.RenameField(
            model_name='talim',
            old_name='rasim',
            new_name='rasimt',
        ),
        migrations.RenameField(
            model_name='talim',
            old_name='title',
            new_name='titlet',
        ),
    ]
