# Generated by Django 5.0.6 on 2024-07-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='khata_transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('ammount', models.CharField(max_length=20)),
                ('catagory', models.CharField(max_length=20)),
            ],
        ),
    ]