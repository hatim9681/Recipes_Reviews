# Generated by Django 4.1.7 on 2023-05-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('temps', models.IntegerField()),
                ('preparation', models.CharField(max_length=255)),
            ],
        ),
    ]