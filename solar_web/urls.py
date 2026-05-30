from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('industrial', views.industrial_view, name='industrial'),
    path('commercial', views.commercial_view, name='commercial'),
    path('residential', views.residential_view, name='residential'),
    path('regulatory-subsidy', views.subsidy_view, name='subsidy'),
    path('engineering-epc', views.engineering_epc_view, name='engineering_epc'),
    path('operations-maintenance', views.operation_maintenance_view, name='operation_maintenance'),
    path('portfolio', views.projects_portfolio_view, name='projects_portfolio'),
    path('investors-esg', views.investor_relations_view, name='investor_relations'),
    path('contact', views.contact_desk_view, name='contact_desk'),
    path('submit_lead', views.submit_lead_view, name='submit_lead_view'),
]