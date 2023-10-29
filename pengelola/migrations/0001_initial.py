# Generated by Django 4.2.6 on 2023-10-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_number', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('subjects', models.TextField(blank=True, null=True)),
                ('bookshelves', models.TextField(blank=True, default='-', null=True)),
            ],
        ),
    ]