"""
URL configuration for project_resume project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),

    # Personal Info
    path('personal/', personal, name='personal'),
    path('pers_create/', pers_create, name='pers_create'),
    path('pers_update/<id>/', pers_update, name='pers_update'),
    path('pers_delete/<id>/', pers_delete, name='pers_delete'),

    # Work Experience
    path('we/', we, name='we'),
    path('we_create/', we_create, name='we_create'),
    path('we_update/<id>/', we_update, name='we_update'),
    path('we_delete/<id>/', we_delete, name='we_delete'),

    # Education
    path('edu/', edu, name='edu'),
    path('edu_create/', edu_create, name='edu_create'),
    path('edu_update/<id>/', edu_update, name='edu_update'),
    path('edu_delete/<id>/', edu_delete, name='edu_delete'),

    # Training
    path('pt/', pt, name='pt'),
    path('pt_create/', pt_create, name='pt_create'),
    path('pt_update/<id>/', pt_update, name='pt_update'),
    path('pt_delete/<id>/', pt_delete, name='pt_delete'),

    # Skills
    path('skl/', skl, name='skl'),
    path('skl_create/', skl_create, name='skl_create'),
    path('skl_update/<id>/', skl_update, name='skl_update'),
    path('skl_delete/<id>/', skl_delete, name='skl_delete'),

    # Portfolio
    path('port/', port, name='port'),
    path('port_create/', port_create, name='port_create'),
    path('port_update/<id>/', port_update, name='port_update'),
    path('port_delete/<id>/', port_delete, name='port_delete'),

    # Platform
    path('plat/', plat, name='plat'),
    path('plat_create/', plat_create, name='plat_create'),
    path('plat_update/<id>/', plat_update, name='plat_update'),
    path('plat_delete/<id>/', plat_delete, name='plat_delete'),

    # Language
    path('lang/', lang, name='lang'),
    path('lang_create/', lang_create, name='lang_create'),
    path('lang_update/<id>/', lang_update, name='lang_update'),
    path('lang_delete/<id>/', lang_delete, name='lang_delete'),

    # Reference
    path('ref/', ref, name='ref'),
    path('ref_create/', ref_create, name='ref_create'),
    path('ref_update/<id>/', ref_update, name='ref_update'),
    path('ref_delete/<id>/', ref_delete, name='ref_delete'),

]
