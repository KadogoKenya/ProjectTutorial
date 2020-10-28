from . import views 
from django.urls import path
from django.conf.urls import url
# from .views import  ProjectCreateView, ProjectListView, ProjectDetailView
from django.conf import settings
from django.conf.urls.static import static
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('hello/', views.HelloView.as_view(), name='hello'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    # path('', ProjectListView.as_view(), name='index'),
    # path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    # url(r'^new/project$', views.new_project, name='new-project'),
    # url(r'^projects/(\d+)',views.projects,name='projects'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
