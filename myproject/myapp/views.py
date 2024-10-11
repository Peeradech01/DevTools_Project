from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from .forms import CustomUserCreationForm
from .models import *

class indexView(View):
    def get(self, request):
        return render(request, 'index.html')

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # patient = form.save()
            # Patient.objects.create(
            #     user = patient,
            #     phone_number = form.cleaned_data["phone_number"],
            #     health_detail = form.cleaned_data["health_detail"]
            # )
            return redirect('url_login')
        return render(request, 'register.html', {'form': form})
    
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request,user)
            return redirect('index')
        return render(request, 'login.html', {'form': form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('url_login')

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')

class HistoryView(View):
    def get(self, request):
        return render(request, 'history.html')

class MedicationView(View):
    def get(self, request):
        return render(request, 'medication.html')

class AddMedicationView(View):
    def get(self, request):
        return render(request, 'add_medication.html')
    

class DoctorView(View):
    def get(self, request):
        return render(request, 'doctor.html')
    


