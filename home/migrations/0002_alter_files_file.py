# Generated by Django 3.2.9 on 2022-02-07 09:47

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=home.models.get_upload_path),
        ),
    ]
