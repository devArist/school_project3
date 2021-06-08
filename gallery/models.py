from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.
class Photo(models.Model):
    CHOICES = (
        ('JPG', 'JPG'),
        ('PNG', 'PNG'),
        ('JPEG', 'JPEG'),
    )
    image = models.FileField(upload_to='img')
    title = models.CharField(max_length=200, verbose_name='titre')
    description = HTMLField()
    licenses = models.ForeignKey(
        "Licenses", 
        verbose_name="licence", 
        on_delete=models.CASCADE,
        related_name='photos'
        )
    formats = models.CharField(
        max_length=50, 
        verbose_name="format",
        null=True,
        choices=CHOICES
        )
    tags = models.ManyToManyField("Tag", verbose_name="tags")
    views = models.IntegerField(default=0, null=True, verbose_name="vues")
    date_add = models.DateTimeField(
        verbose_name="date d'ajout", 
        auto_now_add=True
        )
    date_update = models.DateTimeField(
        auto_now=True, 
        verbose_name="dernière modification"
        )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class Video(models.Model):
    CHOICES = (
        ('MP4', 'MP4'),
    )
    image = models.FileField(upload_to='img')
    title = models.CharField(max_length=200, verbose_name='titre')
    description = HTMLField()
    licenses = models.ForeignKey(
        "Licenses", 
        verbose_name="licence", 
        on_delete=models.CASCADE,
        related_name='videos'
        )
    formats = models.CharField(
        max_length=50,
        choices=CHOICES,
        verbose_name='format',
        null=True
        )
    duration = models.DurationField(null=True, verbose_name="durée")
    views = models.IntegerField(default=0, null=True, verbose_name="vues")
    tags = models.ManyToManyField("Tag", verbose_name="tags")
    date_add = models.DateTimeField(
        verbose_name="date d'ajout", 
        auto_now_add=True
        )
    date_update = models.DateTimeField(
        auto_now=True, 
        verbose_name="dernière modification"
        )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'vidéo'
        verbose_name_plural = 'vidéos'


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    date_add = models.DateTimeField(
        verbose_name="date d'ajout", 
        auto_now_add=True
        )
    date_update = models.DateTimeField(
        auto_now=True, 
        verbose_name="dernière modification"
        )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Licenses(models.Model):
    description = models.TextField()
    date_add = models.DateTimeField(
        verbose_name="date d'ajout", 
        auto_now_add=True
        )
    date_update = models.DateTimeField(
        auto_now=True, 
        verbose_name="dernière modification"
        )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'licence'
        verbose_name_plural = 'licences'