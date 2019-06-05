from django.urls import path, include
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView
from . import views
from django.contrib.auth.decorators import login_required

'''
Clients app - Manage business clients
    * path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail')
    * path('clients/new/', ClientCreateView.as_view(), name='client-create')
    * path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update')
    * path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete')
'''

urlpatterns = [
    path('', login_required(ClientListView.as_view()), name='client-list'),
    path('<int:pk>/', login_required(ClientDetailView.as_view()), name='client-detail'),
    path('new/', login_required(ClientCreateView.as_view()), name='client-create'),
    path('<int:pk>/update', login_required(ClientUpdateView.as_view()), name='client-update'),
    path('<int:pk>/delete', login_required(ClientDeleteView.as_view()), name='client-delete'),
]