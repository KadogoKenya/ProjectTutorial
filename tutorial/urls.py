"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views
from django.urls import path, include
from django.conf.urls import url
from users import views as user_views
from django.contrib.auth import views as auth_views
# from rest_framework.authtoken.views import obtain_auth_token
from tutorialproject import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt import views as jwt_views

from tutorialproject.views import MerchList


# from projectreviews.views import MerchList, profileList




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tutorialproject.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('display_profile/', user_views.display_profile, name='display_profile'),
    url(r'^tinymce/', include('tinymce.urls')),
    path('tutorialproject-api/', views.MerchList.as_view(), name='tutorialproject_api'),
    

    url(r'api-token-auth/', obtain_jwt_token),
    url(r'api-token-refresh/', refresh_jwt_token),
    
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='obtain_jwt_token'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    # path('projector-api/', views.MerchList.as_view(), name='projector_api'),
    # path('profiler-api/', views.profileList.as_view(), name='profiler_api'),
    # url(r'^api-token-auth/', obtain_auth_token),
    # path('ratings/', include('star_ratings.urls', namespace='ratings')),
    # url(r'^tinymce/', include('tinymce.urls')),

    
]