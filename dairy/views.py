from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Cow, MilkProduction, HealthRecord, Veterinarian
from .forms import (
    RegisterForm, CowForm, 
    MilkProductionForm, HealthRecordForm, 
    VeterinarianForm
)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    cows = Cow.objects.filter(owner=request.user)
    context = {
        'cows': cows,
        'title': 'Dashboard'
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_cow(request):
    if request.method == 'POST':
        form = CowForm(request.POST, request.FILES)
        if form.is_valid():
            cow = form.save(commit=False)
            cow.owner = request.user
            cow.save()
            return redirect('dashboard')
    else:
        form = CowForm()
    return render(request, 'add_cow.html', {'form': form})

@login_required
def cow_detail(request, pk):
    cow = get_object_or_404(Cow, pk=pk, owner=request.user)
    
    # Milk production form
    if request.method == 'POST' and 'milk_submit' in request.POST:
        milk_form = MilkProductionForm(request.POST)
        if milk_form.is_valid():
            milk = milk_form.save(commit=False)
            milk.cow = cow
            milk.save()
            return redirect('cow_detail', pk=pk)
    else:
        milk_form = MilkProductionForm()
    
    # Health record form
    if request.method == 'POST' and 'health_submit' in request.POST:
        health_form = HealthRecordForm(request.POST)
        if health_form.is_valid():
            health = health_form.save(commit=False)
            health.cow = cow
            health.save()
            return redirect('cow_detail', pk=pk)
    else:
        health_form = HealthRecordForm()
    
    context = {
        'cow': cow,
        'milk_form': milk_form,
        'health_form': health_form,
        'milk_productions': cow.milk_productions.all().order_by('-date')[:10],
        'health_records': cow.health_records.all().order_by('-date')[:10],
        'title': cow.name
    }
    return render(request, 'cow_detail.html', context)

@login_required
def vet_list(request):
    vets = Veterinarian.objects.all()
    return render(request, 'vet_list.html', {'vets': vets, 'title': 'Veterinarians'})

@staff_member_required
def add_vet(request):
    if request.method == 'POST':
        form = VeterinarianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vet_list')
    else:
        form = VeterinarianForm()
    return render(request, 'admin/add_vet.html', {'form': form, 'title': 'Add Veterinarian'})



def custom_logout(request):
    logout(request)
    request.session.flush()  # Destroy all session data
    return redirect('register')  # Redirect to registration page