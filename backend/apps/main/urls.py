from django.urls import path
from . import views

urlpatterns = [
    path('disasters/', views.DisasterList.as_view(), name='disaster-list'),
    path('disasters/email/', views.DisasterEmail.as_view(), name='disaster-email'),
]
