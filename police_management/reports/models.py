from django.db import models
from django.contrib.auth.models import User

class PoliceOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    badge_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} - {self.badge_number}'


class Criminal(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True)
    capture_by = models.ForeignKey(PoliceOfficer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Crime(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    police_officer = models.ForeignKey(PoliceOfficer, on_delete=models.SET_NULL, null=True, blank=True)
    criminals = models.ManyToManyField(Criminal)

    def __str__(self):
        return f'{self.title} - {self.date.strftime("%d-%m-%Y")}'


class Report(models.Model):
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    crimes = models.ManyToManyField(Crime)
    responsible_officer = models.ForeignKey(PoliceOfficer, on_delete=models.SET_NULL, null=True, blank=True)
    criminals_involved = models.ManyToManyField(Criminal)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.code}"
