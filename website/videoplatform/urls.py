from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from home import views as home_views
from upload import views as upload_views
from myuploads import views as myuploads_views
from video import views as video_views


urlpatterns = [
    url(r'^$', home_views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^upload/$',upload_views.upload , name='upload'),
    url(r'^myuploads/$',myuploads_views.uploads , name='myuploads'),
    url(r'^video/(?P<fileHash>Qm([a-z|A-Z|0-9])+)$',video_views.view_video , name='view_video'),
    url(r'^delete/$',myuploads_views.delete_video , name='delete_video'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^admin/', admin.site.urls),
]
