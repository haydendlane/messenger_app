from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client
from messenger.models import Message

# Create your views here.

class ClientListView(ListView):
    model = Client
    template_name = 'clients/clients.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user).order_by('first_name')

class ClientDetailView(DetailView):
    model = Client

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        context['message_history'] = Message.objects.filter(client=self.get_object())[:5]
        return context

class ClientCreateView(SuccessMessageMixin, CreateView):
    model = Client
    template_name = 'clients/client_form.html'
    fields = ['first_name', 'last_name', 'phone_number']
    success_message = 'Client created! %(first_name)s %(last_name)s at %(phone_number)s'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Client
    fields = ['first_name', 'last_name', 'phone_number']

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        client = self.get_object()
        if self.request.user == client.user:
            return True
        return False

class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = '/'

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

    def test_func(self):
        client = self.get_object()
        if self.request.user == client.user:
            return True
        return False