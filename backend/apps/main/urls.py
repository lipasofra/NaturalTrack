from django.urls import path
from . import views

urlpatterns = [
    path('disasters/', views.DisasterList.as_view(), name='disaster-list'),
]
