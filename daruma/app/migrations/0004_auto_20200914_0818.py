# Generated by Django 3.1.1 on 2020-09-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to='company'),
        ),
    ]
