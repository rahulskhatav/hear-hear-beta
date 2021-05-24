from django.shortcuts import render, redirect
from . forms import CreateUserForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {{ username }}')
            return redirect('user-login')
        else:
            messages.warning(request, f'Please fill in correct details.')
    form = CreateUserForm()
    return render(request, 'user/register.html', {
        "form": form
    })

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success("Profile changed successfully")
    form = ProfileUpdateForm()
    context = {
        "form": form,
    }
    return render(request, 'user/profile.html',context)
