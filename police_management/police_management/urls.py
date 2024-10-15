from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reports.urls')),  # URLs de gestión de reports, police_officers, etc.



    # path('', include('landing.urls')),  # URLs de la landing page
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Vista de logout

    
]
