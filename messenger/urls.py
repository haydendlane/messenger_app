from django.urls import path, include
from .views import MessageDetailView, MessageListView, ClientListView
from clients.models import Client
from . import views
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

'''
Messenger app - Main features - This is the homepage
    * path('', views.dashboard, name='messenger-dashboard')
    * path('message/new/', MessageCreateView.as_view(), name='message-create')
    * path('message/<int:pk>/', MessageDetailView.as_view(), name='message-detail')
    * path('message/history/<int:pk>', MessageListView.as_view(), name='message-history')
'''

urlpatterns = [
    path('', views.dashboard, name='messenger-dashboard'),
    path('message/', login_required(ClientListView.as_view()), name='select-client'),
    path('message/new/<int:pk>/', csrf_exempt(views.create_message), name='message-create'),
    path('message/history/', login_required(MessageListView.as_view()), name='message-history'),
    path('message/<slug:pk>/', login_required(MessageDetailView.as_view()), name='message-detail'),
    # path('delivery/', views.delivery, name='delivery-status'),
]