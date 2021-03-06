# Generated by Django 3.1.1 on 2020-09-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_home_team_link_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('meta_description', models.CharField(max_length=150)),
                ('hero_title', models.CharField(max_length=100)),
                ('hero_subtitle', models.CharField(max_length=250)),
                ('team_title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Team',
            },
        ),
    ]
