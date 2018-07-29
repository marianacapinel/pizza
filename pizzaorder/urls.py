"""pizzaorder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from pizza import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^orders/$', views.OrderList.as_view(), name='order_list'),
    url(r'^orders/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyOrder.as_view(), name='order_detail'),
    url(r'^clients/$', views.ClientList.as_view(), name='client_list'),
    url(r'^clients/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyClient.as_view(), name='client_detail')
]


