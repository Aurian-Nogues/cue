# Generated by Django 2.1.7 on 2019-03-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]