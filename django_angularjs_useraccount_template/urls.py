from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from authentication.views import LoginView
from authentication.views import LogoutView
from authentication import views
from django_angularjs_useraccount_template.views import IndexView

urlpatterns = [
    url(r'^api/v1/profile/$', views.ProfileView.as_view()),
    url(r'^api/v1/profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view()),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url('^.*$', IndexView.as_view(), name='index'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
