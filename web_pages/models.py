from django.db import models
from django.utils import timezone
from django.db.models import Sum


class Project(models.Model):
    project_title = models.CharField(max_length=200, null=True, blank=True)
    theme = models.CharField(max_length=200, null=True, blank=True)
    donor = models.CharField(max_length=200, null=True, blank=True)
    project_value = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(default=timezone.now, null=True, blank=True)
    end_date = models.DateField(default=timezone.now, null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    achievements = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.project_title

class ProjectGallery(models.Model):
	shop_image = models.ImageField(upload_to="gallery", null=True, blank=True)
	description = models.CharField(max_length=500, null=True, blank=True)
