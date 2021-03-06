# Generated by Django 3.2.3 on 2021-06-07 20:30

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='dernière modification')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'licence',
                'verbose_name_plural': 'licences',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='dernière modification')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img')),
                ('title', models.CharField(max_length=200, verbose_name='titre')),
                ('description', tinymce.models.HTMLField()),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='dernière modification')),
                ('status', models.BooleanField(default=True)),
                ('licenses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='gallery.licenses', verbose_name='licence')),
                ('tags', models.ManyToManyField(to='gallery.Tag', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'vidéo',
                'verbose_name_plural': 'vidéos',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img')),
                ('title', models.CharField(max_length=200, verbose_name='titre')),
                ('description', tinymce.models.HTMLField()),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='dernière modification')),
                ('status', models.BooleanField(default=True)),
                ('licenses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='gallery.licenses', verbose_name='licence')),
                ('tags', models.ManyToManyField(to='gallery.Tag', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
            },
        ),
    ]
