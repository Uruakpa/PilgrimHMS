# Generated by Django 4.2.7 on 2023-11-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('GuestID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('CNIC', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('ConfirmPassword', models.CharField(max_length=100)),
                ('ContactNo', models.CharField(max_length=100)),
            ],
        ),
    ]
