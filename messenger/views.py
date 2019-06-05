from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages as message_alerts
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Message
from clients.models import Client
from . import send_sms
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from twilio.base.exceptions import TwilioRestException

@login_required
def dashboard(request):
    user = None
    if request.user.is_authenticated:
        user = {
            'user': request.user
        }
    return render(request, 'messenger/dashboard.html', user)

class ClientListView(ListView):
    model = Client
    template_name = 'messenger/select_client.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'clients'
    paginate_by = 5

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user).order_by('first_name')

class MessageListView(ListView):
    model = Message
    template_name = 'messenger/message_history.html' # <app>/<model>_<viewtype>.html
    paginate_by = 5

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user).order_by('-date_sent')

class MessageDetailView(DetailView):
    model = Message

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user)

@login_required
def create_message(request, pk):
# Refactor to a try/except sequence to handle issues with malformed POST requests

    queryset = Client.objects.filter(user=request.user)
    get_object_or_404(queryset, id=pk)

    if request.method == 'POST':
        client = Client.objects.get(id=pk)
        user = client.user
        send_sms.send(user_id=user, user_company=request.user.company, client_id=client, client_phone_number=int(client.phone_number) )
        message_alerts.success(request, 'Your message has been sent to %s %s at %s' % (client.first_name, client.last_name, client.phone_number))
        
        return redirect('messenger-dashboard')
    return render(request, 'messenger/message_form.html', {'client': Client.objects.get(id=pk)})

@csrf_exempt
@require_POST
def delivery(request):
    message_sid = request.POST.get('MessageSid', None)
    message_status = request.POST.get('MessageStatus', None)

    Message.objects.filter(message_sid=message_sid).update(delivery_status=message_status)

    return HttpResponse(status=204)

def privacy_policy(request):
    return render(request, 'messenger/privacy_policy.html')

def handler500(request):
    return render(request, 'messenger/500.html', status=500)