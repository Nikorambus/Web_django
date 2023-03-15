from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('log')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/log.html'

    def get_success_url(self):
        return reverse_lazy('home')


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def reg(request):
    return render(request, 'main/reg.html')


def log(request):
    return render(request, 'main/log.html')


def logout_user(request):
    logout(request)
    return redirect('log')
