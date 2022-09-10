"""water_clients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clients.views import names_list
from clients.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', names_list),
path('clients/', ClientListView.as_view(), name='clients'),
    path('orders/', OrderListView.as_view(), name="order-list"),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
    path('order/<int:pk>/', OrderInfoView.as_view(), name="order-info"),
    path('signin/', LoginView.as_view(), name="sign-in"),
    path('signout/', LogoutView.as_view(), name="sign-out"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
