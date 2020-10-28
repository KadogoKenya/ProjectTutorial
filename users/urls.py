from django.conf.urls import url
from tutorial.users import views as tutorial_views

urlpatterns = [
    # url(r'^signup/$', insta_views.signup, name='signup'),
    url(r'^signup/$', tutorial_views.signup, name='signup'),
]
