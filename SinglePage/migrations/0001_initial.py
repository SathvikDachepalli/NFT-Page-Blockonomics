# Generated by Django 4.1.6 on 2023-03-05 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFTImages',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/')),
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('walletID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoiceId', models.AutoField(primary_key=True, serialize=False)),
                ('productId', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('buyer', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
                ('status', models.IntegerField(choices=[(-1, 'Not Started'), (0, 'Not confirmed'), (1, 'Processing'), (2, 'Paid')], default=-1)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SinglePage.nftimages')),
            ],
        ),
    ]