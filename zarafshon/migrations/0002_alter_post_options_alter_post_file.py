# Generated by Django 4.0.5 on 2022-06-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zarafshon', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to='media/files'),
        ),
    ]
