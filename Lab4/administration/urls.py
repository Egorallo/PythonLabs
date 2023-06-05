from django.urls import path

import administration.views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'administration'


urlpatterns = [
    path('', views.index, name='list_servicepack'),
    path('create/', administration.views.ServicePackCreate.as_view(), name='create_servicepack'),
    path('delete/<int:id>/', administration.views.ServicePackDelete.as_view(), name='delete_servicepack'),
    path('edit/<int:id>/', administration.views.ServicePackEdit.as_view(), name='edit_servicepack'),
    path('createinstance/', administration.views.ServicePackInstanceCreateView.as_view(), name='create_servicepackinstance'),
]
