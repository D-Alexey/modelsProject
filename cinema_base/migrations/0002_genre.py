# Generated by Django 5.1.2 on 2024-10-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Жанр')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('films', models.ManyToManyField(blank=True, null=True, related_name='genres', to='cinema_base.film', verbose_name='Фильмы')),
            ],
        ),
    ]
