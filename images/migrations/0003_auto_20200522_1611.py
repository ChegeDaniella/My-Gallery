# Generated by Django 3.0.6 on 2020-05-22 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20200522_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Location'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Category'),
        ),
    ]