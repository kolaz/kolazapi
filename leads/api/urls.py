from django.urls import path
from leads.api.views import LeadListCreate

urlpatterns = [
    path('lead/', LeadListCreate.as_view() ),
]