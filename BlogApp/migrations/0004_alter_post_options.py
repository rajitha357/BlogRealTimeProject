# Generated by Django 4.1.5 on 2023-03-01 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_alter_post_options_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
    ]
