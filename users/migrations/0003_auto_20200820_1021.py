# Generated by Django 2.0.13 on 2020-08-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usersearchtweetslocationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearchtweetslocationmodel',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
