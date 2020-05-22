# Generated by Django 3.0.6 on 2020-05-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=60)),
                ('image_description', models.TextField(max_length=500)),
                ('image_location', models.CharField(max_length=60)),
                ('image_category', models.CharField(max_length=60)),
            ],
        ),
    ]