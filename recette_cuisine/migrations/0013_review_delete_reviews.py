# Generated by Django 4.1.7 on 2023-05-06 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recette_cuisine', '0012_rename_review_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recette_cuisine.recette')),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]