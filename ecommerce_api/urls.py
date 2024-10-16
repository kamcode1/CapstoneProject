"""
URL configuration for ecommerce_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserRegistrationView
from core.views import api_overview
from django.http import HttpResponseRedirect

urlpatterns = [
    path("admin/", admin.site.urls),

     # Redirect root URL to /api/
    path("", lambda request: HttpResponseRedirect('/api/')),
    path('api/register/', UserRegistrationView.as_view(), name='register'),  # Add this line for registration
    # API Overview
    path('api/overview/', api_overview),

    # Users and products API
    path('api/users/', include('users.urls')), 
    path('api/products/', include('products.urls')),

    # transaction API
    path('api/transactions/', include('transaction.urls')),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
