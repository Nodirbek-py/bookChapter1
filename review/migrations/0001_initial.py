# Generated by Django 3.2 on 2021-08-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the publisher', max_length=128)),
                ('website', models.URLField(help_text="Publisher's website")),
                ('email', models.EmailField(help_text='Email of the publisher', max_length=254)),
            ],
        ),
    ]
