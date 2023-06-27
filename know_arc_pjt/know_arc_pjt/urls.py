
"""
URL configuration for know_arc_pjt project.

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
# django's default
from django.contrib import admin
from django.urls import path, include

# knowark's addition
from main.views import main
from django.conf import settings
from django.conf.urls.static import static
# from keyword_chart.views import index, post_view

urlpatterns = [
    # django's default
    path('admin/', admin.site.urls),

    # knowark's addition
    path('', main, name='knowark'),
    
    # path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/', include('allauth.urls')),  # allauth path

    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),
    
    # path('index/', include('keyword_chart.urls')),

]

# 20230626 김경민 wc image추가를 위해
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# close