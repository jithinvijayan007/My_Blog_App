# Generated by Django 3.0.3 on 2020-08-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]