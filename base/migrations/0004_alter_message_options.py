# Generated by Django 3.2.8 on 2021-11-19 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20211118_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created']},
        ),
    ]
