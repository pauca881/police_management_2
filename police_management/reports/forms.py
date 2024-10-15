from django import forms

class PoliceOfficerSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)

class CriminalSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)


class CrimeSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)

class ReportSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)