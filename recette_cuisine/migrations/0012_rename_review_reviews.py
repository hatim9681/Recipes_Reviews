# Generated by Django 4.1.7 on 2023-05-06 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recette_cuisine', '0011_review_recette'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Reviews',
        ),
    ]
