from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class About(models.Model):
    image = models.FileField(upload_to='img')
    description = HTMLField()

    def __str__(self) -> str:
        return 'A propos de l\'entreprise'

    class Meta:
        verbose_name = 'A propos'
        verbose_name_plural = 'A propos'


class Contact(models.Model):
    CHOICES = (
        ('Subject', 'Subject'),
        ('Sales & marketing', 'Sales & marketing'),
        ('Creative Design', 'Creative Design'),
        ('UI/UX', 'UI/UX'),
        )
    name = models.CharField(verbose_name="nom", max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(
        verbose_name="sujet", 
        max_length=50, choices=CHOICES
        )
    message = models.TextField()
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
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class Address(models.Model):
    description = models.TextField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(verbose_name="téléphone", max_length=200)
    url = models.URLField(max_length=200)
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
        return self.email

    class Meta:
        verbose_name = 'Adresse'
        verbose_name_plural = 'Adresses'


class Location(models.Model):
    name = models.CharField(verbose_name="nom", max_length=200)
    address = models.TextField()
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
        verbose_name = 'emplacement'
        verbose_name_plural = 'emplacements'


class SocialNetwork(models.Model):
    icon = models.CharField(verbose_name="icône", max_length=200)
    name = models.CharField(verbose_name="nom", max_length=200)
    link = models.URLField(verbose_name="lien", max_length=200)
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
        verbose_name = 'réseau social'
        verbose_name_plural = 'réseaux sociaux'


class Employee(models.Model):
    image = models.FileField(upload_to='img')
    name = models.CharField(verbose_name="nom", max_length=200)
    job = models.CharField(max_length=200)
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
        return self.name

    class Meta:
        verbose_name = 'employé'
        verbose_name_plural = 'employés'


class EmployeeSocialNetwork(models.Model):
    icon = models.CharField(verbose_name="icône", max_length=200)
    name = models.CharField(verbose_name="nom", max_length=200)
    link = models.URLField(verbose_name="lien", max_length=200)
    employee = models.ForeignKey(
        "Employee", 
        verbose_name="employé", 
        on_delete=models.CASCADE
        )
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
        verbose_name = 'réseau social d\'un employé'
        verbose_name_plural = 'réseaux sociaux des employés'