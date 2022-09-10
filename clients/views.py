from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# clients/views.py
from .models import Client, Order
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.models import AnonymousUser


def names_list(request):
    context = {}
    clients_list = Client.objects.all()
    context['clients_list'] = clients_list
    return render(request, 'clients.html', context)


class LoginView(View):
    def get(self, request):
        context = {"form": LoginForm()}
        return render(request, 'auth/sign_in.html', context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        user_login = data["username"]
        password = data["password"]
        user = authenticate(request, username=user_login, password=password)
        if user is not None:
            login(request, user)
            return redirect(products_list)
        else:
            return HttpResponse("Не верный логин или пароль")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(products_list)


class ClientListView(ListView):
    model = Client
    template_name = 'clients.html'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_delete.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"


class OrderInfoView(DetailView):
    model = Order
    template_name = "order_info.html"


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"





class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_delete.html'
    fields = ["name", "contacts", "description"]
    success_url = "/orders/"


class OrderInfoView(DetailView):
    model = Order
    template_name = "order_info.html"


