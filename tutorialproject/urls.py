from . import views 
from django.urls import path
from django.conf.urls import url
# from .views import  ProjectCreateView, ProjectListView, ProjectDetailView
from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views import  TutorialCreateView, TutorialDetailView,TutorialUpdateView,TutorialDeleteView,TutorialListView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('tutorial/new/', TutorialCreateView.as_view(), name='tutorial-create'),
    path('', TutorialListView.as_view(), name='index'),
    # path('', views.index, name='index'),


    path('tutorial/<int:pk>/', TutorialDetailView.as_view(), name='tutorial-detail'),
    path('tutorial/new/', TutorialCreateView.as_view(), name='tutorial-create'),
    path('tutorial/<int:pk>/update/', TutorialUpdateView.as_view(), name='tutorial-update'),
    path('tutorial/<int:pk>/delete/', TutorialDeleteView.as_view(), name='tutorial-delete'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/tutorial$', views.new_tutorial, name='new-tutorial'),
    url(r'^api/merch/$', views.MerchList.as_view()),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',views.MerchDescription.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
