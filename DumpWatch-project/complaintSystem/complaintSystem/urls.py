"""
URL configuration for complaintSystem project.

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
from django.urls import path
from complaints import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete_complaint/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
    path('mark_complaint/<int:complaint_id>/', views.mark_complaint, name='mark_complaint'),
    path('admin_login/', views.admin_login, name='admin_login'),  # New URL pattern for admin login
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)