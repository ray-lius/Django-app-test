"""
URL configuration for drinks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from drinks.router import OptionalSlashRouter
from drinks.viewsets import DrinkViewSet, CustomerViewSet, SalesViewSet
from drinks.settings import API_VERSION

api_namespace = "api"
api_version = API_VERSION
api_base = f"{api_namespace}/{api_version}/"

router = OptionalSlashRouter()
router.register(r"drinks", DrinkViewSet, basename="drinks")
router.register(r"customers", CustomerViewSet, basename="customers")
router.register(r"sales", SalesViewSet, basename="sales")

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path(api_base, include(router.urls)),
]