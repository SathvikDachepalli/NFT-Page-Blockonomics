# Generated by Django 4.1.6 on 2023-03-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SinglePage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='walletID',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
    ]