# Generated by Django 4.1.7 on 2023-05-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette_cuisine', '0002_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recette',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
