from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def account(request):
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('account')
    else:
        u_form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'u_form': u_form,
    }

    return render(request, 'users/account.html', context)