# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class StorageUpdate(models.Model):
    entry_date = models.DateField()
    entry_content = models.TextField()
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Storage Update'
        verbose_name = "Storage update"
        verbose_name_plural = "Storage updates"


class Project(models.Model):
    shortname = models.CharField(max_length=10, unique=True)
    longname = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.shortname

    class Meta:
        db_table = 'project'
        verbose_name = "project"
        verbose_name_plural = "projects"


class Container(models.Model):
    shortname = models.CharField(max_length=10, unique=True)
    longname = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.shortname

    class Meta:
        db_table = 'container'
        verbose_name = "container"
        verbose_name_plural = "containers"


class Person(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        db_table = 'persons'
        verbose_name = "person"
        verbose_name_plural = "persons"


class Analysis(models.Model):
    shortname = models.CharField(max_length=10, unique=True)
    longname = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.shortname

    class Meta:
        db_table = "analysis"
        verbose_name = "analysis"
        verbose_name_plural = "analyses"


class Material(models.Model):
    shortname = models.CharField(max_length=10, unique=True)
    longname = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.shortname

    class Meta:
        db_table = "material"
        verbose_name = "material"
        verbose_name_plural = "materials"


class Treatment(models.Model):
    shortname = models.CharField(max_length=10, unique=True)
    longname = models.CharField(max_length=20, blank=True, null=True)
    data = models.FloatField()
    comments = models.CharField(max_length=128, blank=True, null=True)
    parameter = models.ForeignKey('Parameter', models.PROTECT)

    def __str__(self):
        return self.shortname

    class Meta:
        db_table = "treatment"
        verbose_name = "treatment"
        verbose_name_plural = "treatments"


class Method(models.Model):
    shortname = models.CharField(max_length=10, unique=True)
    longname = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=128, blank=True, null=True)
    treatments = models.ManyToManyField("Treatment")

    def __str__(self):
        return self.shortname

    class Meta:
        db_table = "method"
        verbose_name = "method"
        verbose_name_plural = "methods"


class Parameter(models.Model):
    shortname = models.CharField(max_length=10, unique=True)
    longname = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=128, blank=True, null=True)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.shortname

    class Meta:
        db_table = "parameter"
        verbose_name = "parameter"
        verbose_name_plural = "parameters"


class Shelf(models.Model):
    name = models.CharField(max_length=32, unique=True)
    barcode = models.CharField(max_length=128, unique=True)
    room = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "shelf"
        verbose_name = "shelf"
        verbose_name_plural = "shelves"


class Sample(models.Model):
    name = models.CharField(max_length=128, unique=True)
    project = models.ForeignKey('Project', models.PROTECT)
    container = models.ForeignKey('Container', models.PROTECT)
    date = models.DateField()
    production_time = models.FloatField()
    amount = models.FloatField()
    amount_free = models.FloatField()
    shelf = models.ForeignKey('Shelf', models.PROTECT)
    characterisation = models.ManyToManyField('Analysis')
    material = models.ForeignKey('Material', models.PROTECT, blank=True, null=True)
    method = models.ForeignKey('Method', models.PROTECT, blank=True, null=True)
    last_user = models.ForeignKey('Person', models.PROTECT, blank=True, null=True, related_name='last_user')
    analysed_user = models.ForeignKey('Person', models.PROTECT, blank=True, null=True, related_name='analysed_user')
    barcode = models.CharField(unique=True, max_length=128)
    inert_handling = models.BooleanField()
    comments = models.CharField(max_length=256, blank=True, null=True)
    static_files = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sample'
        verbose_name = "sample"
        verbose_name_plural = "samples"
