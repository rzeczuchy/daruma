# Generated by Django 3.1.1 on 2020-09-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_privacypolicy'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacypolicy',
            name='subtitle',
            field=models.CharField(default='Privacy Policy', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='title',
            field=models.CharField(default='Lorem ipsum dolor sit amet', max_length=50),
            preserve_default=False,
        ),
    ]