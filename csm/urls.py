"""
URL configuration for csm project.

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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from employee.views import dashboard,loginpage
#from employee.views import MyLoginView,MyLogoutView
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',dashboard,name='index-page'),
    path('product/',include('product.urls'),name='product'),
    path('doctor/',include('doctor.urls'),name='doctor'),
    path('deals/',include('deals.urls'),name='deals'),
    path('employee/',include('employee.urls'),name='employee'),
    path('',auth_view.LoginView.as_view(template_name='base/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout')
    
    #path('',loginpage,name='login'),
]

if settings:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)