# Generated by Django 2.1.7 on 2019-04-14 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20190415_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='podcategory',
        ),
    ]