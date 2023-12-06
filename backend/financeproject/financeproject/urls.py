"""
URL configuration for financeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from financeapp.views import TransactionViewSet,BudgetViewSet, GoalViewSet, AccountViewSet, register, login

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'accounts', AccountViewSet, basename='account')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/register/', register, name='api-register'),
    path('api/login/', login, name='api-login'),

]
