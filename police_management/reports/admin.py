from django.contrib import admin

from reports.models import Crime, Criminal, PoliceOfficer, Report

# Register your models here.
admin.site.register(PoliceOfficer)
admin.site.register(Criminal)
admin.site.register(Crime)
admin.site.register(Report)