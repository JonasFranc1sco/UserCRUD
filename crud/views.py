from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = UserForm()
    return render(request, 'crud/create_user.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']           
            if User.objects.filter(name=name, password=password).exists():
                return redirect('list_users')
            else:
                return redirect('create_user')
    else:
        form = UserForm()
    return render(request, 'crud/login_user.html', {'form':form})

def list_users(request):
    users = User.objects.all()
    return render(request, 'crud/list_users.html', {'users': users})

def update_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'crud/update_user.html', {'form': form})

def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('list_users')