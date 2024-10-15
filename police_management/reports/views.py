from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PoliceOfficer, Criminal, Crime, Report
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
@login_required
def some_view(request):
    pass
    # Lógica de la vista

# Vista para la landing page
def landing_page(request):
    return render(request, 'reports/landing_page.html')



class PoliceOfficerDetailView(DetailView):
    model = PoliceOfficer
    template_name = 'reports/police_officer_detail.html'
    context_object_name = 'officer'

    # Sobrescribimos el método para incluir el usuario relacionado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object.user  # Agregamos el usuario relacionado
        return context

# PoliceOfficer Views

from django.views.generic import ListView
from .models import PoliceOfficer
from .forms import CrimeSearchForm, CriminalSearchForm, PoliceOfficerSearchForm, ReportSearchForm

class PoliceOfficerListView(ListView):
    model = PoliceOfficer
    template_name = 'reports/police_officer_list.html'
    context_object_name = 'officers'
    paginate_by = 10  # Si quieres paginación


    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(user__username__icontains=query) | queryset.filter(badge_number__icontains=query)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = PoliceOfficerSearchForm(self.request.GET or None)
        return context

# class PoliceOfficerListView(ListView):
#     model = PoliceOfficer
#     template_name = 'reports/police_officer_list.html'
#     context_object_name = 'officers'


class PoliceOfficerCreateView(CreateView):
    model = PoliceOfficer
    fields = ['user', 'badge_number']
    template_name = 'reports/police_officer_form.html'
    success_url = reverse_lazy('police_officer_list')


class PoliceOfficerUpdateView(UpdateView):
    model = PoliceOfficer
    fields = ['user', 'badge_number']
    template_name = 'reports/police_officer_form.html'
    success_url = reverse_lazy('police_officer_list')


class PoliceOfficerDeleteView(DeleteView):
    model = PoliceOfficer
    template_name = 'reports/police_officer_confirm_delete.html'
    success_url = reverse_lazy('police_officer_list')


# Criminal Views

class CriminalDetailView(DetailView):
    model = Criminal
    template_name = 'reports/criminal_detail.html'
    context_object_name = 'criminal'
    
# class CriminalListView(ListView):
#     model = Criminal
#     template_name = 'reports/criminal_list.html'
#     context_object_name = 'criminals'
class CriminalListView(ListView):
    model = Criminal
    template_name = 'reports/criminal_list.html'
    context_object_name = 'criminals'
    paginate_by = 10  # Si quieres agregar paginación

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(name__icontains=query) | queryset.filter(alias__icontains=query)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = CriminalSearchForm(self.request.GET or None)
        return context

class CriminalCreateView(CreateView):
    model = Criminal
    fields = ['name', 'alias', 'capture_by']
    template_name = 'reports/criminal_form.html'
    success_url = reverse_lazy('criminal_list')


class CriminalUpdateView(UpdateView):
    model = Criminal
    fields = ['name', 'alias', 'capture_by']
    template_name = 'reports/criminal_form.html'
    success_url = reverse_lazy('criminal_list')


class CriminalDeleteView(DeleteView):
    model = Criminal
    template_name = 'reports/criminal_confirm_delete.html'
    success_url = reverse_lazy('criminal_list')


# Crime Views

class CrimeDetailView(DetailView):
    model = Crime
    template_name = 'reports/crime_detail.html'
    context_object_name = 'crime'

    
# class CrimeListView(ListView):
#     model = Crime
#     template_name = 'reports/crime_list.html'
#     context_object_name = 'crimes'

class CrimeListView(ListView):
    model = Crime
    template_name = 'reports/crime_list.html'
    context_object_name = 'crimes'
    paginate_by = 10  # Si quieres agregar paginación

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(title__icontains=query) | queryset.filter(location__icontains=query)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = CrimeSearchForm(self.request.GET or None)
        return context

class CrimeCreateView(CreateView):
    model = Crime
    fields = ['title', 'description', 'date', 'location', 'police_officer', 'criminals']
    template_name = 'reports/crime_form.html'
    success_url = reverse_lazy('crime_list')


class CrimeUpdateView(UpdateView):
    model = Crime
    fields = ['title', 'description', 'date', 'location', 'police_officer', 'criminals']
    template_name = 'reports/crime_form.html'
    success_url = reverse_lazy('crime_list')


class CrimeDeleteView(DeleteView):
    model = Crime
    template_name = 'reports/crime_confirm_delete.html'
    success_url = reverse_lazy('crime_list')


# Report Views
class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/report_detail.html'
    context_object_name = 'report'

# class ReportListView(ListView):
#     model = Report
#     template_name = 'reports/report_list.html'
#     context_object_name = 'reports'

class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'
    paginate_by = 10  # Si quieres agregar paginación

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(code__icontains=query) | queryset.filter(description__icontains=query)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ReportSearchForm(self.request.GET or None)
        return context
class ReportCreateView(CreateView):
    model = Report
    fields = ['code', 'description', 'crimes', 'responsible_officer', 'criminals_involved']
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('report_list')


class ReportUpdateView(UpdateView):
    model = Report
    fields = ['code', 'description', 'crimes', 'responsible_officer', 'criminals_involved']
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('report_list')


class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'reports/report_confirm_delete.html'
    success_url = reverse_lazy('report_list')
