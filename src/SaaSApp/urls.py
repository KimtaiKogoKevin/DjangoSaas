"""
URL configuration for SaaSApp project.

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
from django.urls import path , include
from auth import views as auth_views
from subscriptions import views as subscription_views

from .views import home_view,about_view,pw_protected_view

urlpatterns = [
    path("",home_view, name="home"),
    path('admin/', admin.site.urls),
    path('about/', about_view),
    path('pricing/', subscription_views.subscription_price_view, name="pricing"),
    path('pricing/<str:interval>/', subscription_views.subscription_price_view, name="pricing_interval"),


    # path('login/', auth_views.login_view),
    # path('register/', auth_views.register_view),
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('profiles.urls')),

    path('protected/',pw_protected_view),



    path("hello-world/",home_view),
]
