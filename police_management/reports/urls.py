from django.urls import path

from reports.views import landing_page
from .views import (
    CrimeDetailView, CriminalDetailView, PoliceOfficerDetailView, PoliceOfficerListView, PoliceOfficerCreateView, PoliceOfficerUpdateView, PoliceOfficerDeleteView,
    CriminalListView, CriminalCreateView, CriminalUpdateView, CriminalDeleteView,
    CrimeListView, CrimeCreateView, CrimeUpdateView, CrimeDeleteView, ReportDetailView,
    ReportListView, ReportCreateView, ReportUpdateView, ReportDeleteView
)

urlpatterns = [
    path('', landing_page, name='landing_page'),

    # PoliceOfficer URLs
    path('police_officers/', PoliceOfficerListView.as_view(), name='police_officer_list'),
    path('police_officer/create/', PoliceOfficerCreateView.as_view(), name='police_officer_create'),
    path('police_officer/<int:pk>/update/', PoliceOfficerUpdateView.as_view(), name='police_officer_update'),
    path('police_officer/<int:pk>/delete/', PoliceOfficerDeleteView.as_view(), name='police_officer_delete'),
    path('police_officer/<int:pk>/', PoliceOfficerDetailView.as_view(), name='police_officer_detail'),

    # Criminal URLs
    path('criminals/', CriminalListView.as_view(), name='criminal_list'),

    path('criminals/', CriminalListView.as_view(), name='criminal_list'),
    path('criminal/create/', CriminalCreateView.as_view(), name='criminal_create'),
    path('criminal/<int:pk>/update/', CriminalUpdateView.as_view(), name='criminal_update'),
    path('criminal/<int:pk>/delete/', CriminalDeleteView.as_view(), name='criminal_delete'),
    path('criminal/<int:pk>/', CriminalDetailView.as_view(), name='criminal_detail'),  # Vista detallada


    # Crime URLs
    path('crimes/', CrimeListView.as_view(), name='crime_list'),
    path('crime/create/', CrimeCreateView.as_view(), name='crime_create'),
    path('crime/<int:pk>/update/', CrimeUpdateView.as_view(), name='crime_update'),
    path('crime/<int:pk>/delete/', CrimeDeleteView.as_view(), name='crime_delete'),
    path('crime/<int:pk>/', CrimeDetailView.as_view(), name='crime_detail'),  # Vista detallada

    # Report URLs
    path('reports/', ReportListView.as_view(), name='report_list'),
    path('report/create/', ReportCreateView.as_view(), name='report_create'),
    path('report/<int:pk>/update/', ReportUpdateView.as_view(), name='report_update'),
    path('report/<int:pk>/delete/', ReportDeleteView.as_view(), name='report_delete'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),  # Vista detallada

]
