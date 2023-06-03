from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('servicepacks/', views.ServicePackListView.as_view(), name='servicepacks'),
    path('servicepack/<int:pk>', views.ServicePackDetailView.as_view(), name='servicepack-detail')
]
