# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Competition(models.Model):
    title = models.CharField(max_length=255)
    verbose_name ="Competitions"
    def __str__(self):
        return self.title
    shorthand = models.CharField(max_length=255, default="N/A", help_text="Ex: HPV, CE, Baja. If no shorthand available reenter the title.")
    description = models.TextField()
    url = models.URLField()
    picture = models.ImageField(upload_to="competitions", default="gearbg.png")
    def get_name(self):
        name = "Competitions"
        return name
    def get_type(self):
        type = "competition_individual"
        return type

class Club(models.Model):
    title = models.CharField(max_length=255)
    verbose_name = "Clubs"
    def __str__(self):
        return self.title
    shorthand = models.CharField(max_length=255, default="N/A", help_text="Ex: HPV, CE, Baja. If no shorthand available reenter the title.")
    description = models.TextField()
    url = models.URLField()
    picture = models.ImageField(upload_to="clubs", default="gearbg.png")
    def get_name(self):
        name = "Clubs"
        return name
    def get_type(self):
        type = "club_individual"
        return type

class Major(models.Model):
    title = models.CharField(max_length=255)
    verbose_name = "Majors"
    def __str__(self):
       return self.title
    shorthand = models.CharField(max_length=255, default="N/A", help_text="Ex: HPV, CE, Baja. If no shorthand available reenter the title.")
    description = models.TextField()
    url = models.URLField()
    picture = models.ImageField(upload_to="majors", default="gearbg.png")
    def get_name(self):
        name = "Majors"
        return name
    def get_type(self):
        type = "major_individual"
        return type

class OurStory(models.Model):
    description = models.TextField()
    url = models.URLField()
    picture = models.ImageField(upload_to="ourstory", default="gearbg.png")

    verbose_name = "Our Story"
    def __str__(self):
       return "OurStory"

