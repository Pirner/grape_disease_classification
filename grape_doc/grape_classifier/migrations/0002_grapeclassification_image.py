# Generated by Django 4.1.7 on 2023-03-18 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grape_classifier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grapeclassification',
            name='image',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
