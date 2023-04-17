"""DjangoEcommerce URL Configuration

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
from DjangoEcommerseApp import views,AdminViews
from django.conf.urls.static import static
from DjangoEcommerce import settings

urlpatterns = [
    path('admin/', views.adminLogin, name="admin_login"),
    path('demo/',views.demopage),
    path('demopage/',views.demopageTemplate),
    path('admin_login_process',views.adminLoginProcess,name="admin_login_process"),
    path('admin_logout_process',views.adminLogoutProcess,name="admin_logout_process"),
    #admin page
    path('admin_home',AdminViews.admin_home,name="admin_home"),
    #Categories
    path('category_list',AdminViews.CategoriesListView.as_view(),name="category_list"),
    path('category_create',AdminViews.CategoriesCreate.as_view(),name="category_create"),
    path('category_update/<slug:pk>',AdminViews.CategoriesUpdate.as_view(),name="category_update"),
    #SubCategories
    path('sub_category_list',AdminViews.SubCategoriesListView.as_view(),name="sub_category_list"),
    path('sub_category_create',AdminViews.SubCategoriesCreate.as_view(),name="sub_category_create"),
    path('sub_category_update/<slug:pk>',AdminViews.SubCategoriesUpdate.as_view(),name="sub_category_update"),
    #merchant User
    path('merchant_create',AdminViews.MerchantUserCreateView.as_view(),name="merchant_create"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
