# Generated by Django 5.1.5 on 2025-01-18 09:55

import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SEOImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('alt_text', models.CharField(max_length=255, verbose_name='Alternative Text')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='images/')),
                ('caption', models.CharField(blank=True, max_length=255, verbose_name='Caption')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'SEO Image',
                'verbose_name_plural': 'SEO Images',
            },
        ),
    ]
