# Generated by Django 4.1.7 on 2023-09-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
