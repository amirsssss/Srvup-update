from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path

from django.contrib import admin
from django.views.generic import TemplateView

from srvup.views import home
from accounts.views import account_home,auth_logout,auth_login,auth_register
from billing.views import upgrade,billing_history,cancel_subscription
from comments.views import comment_thread,comment_create_view
from notifications.views import get_notifications_ajax,all,read
from videos.views import category_list,category_detail,video_detail

urlpatterns =[
    re_path(r'^contact/$', TemplateView.as_view(template_name='company/contact_us.html'), name='contact_us'),
    re_path(r'^$', home, name='home'),
    re_path(r'^projects/$', category_list, name='projects'),
    re_path(r'^projects/(?P<cat_slug>[\w-]+)/$', category_detail, name='project_detail'),
    re_path(r'^projects/(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/$', video_detail, name='video_detail'),
    re_path(r'^dj/admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#auth login/logout
urlpatterns += [
    re_path(r'^upgrade/$', upgrade, name='account_upgrade'),
    re_path(r'^billing/$', billing_history, name='billing_history'),
    re_path(r'^billing/cancel/$', cancel_subscription, name='cancel_subscription'),
]
#auth login/logout
urlpatterns += [
    re_path(r'^account/$', account_home, name='account_home'),
	re_path(r'^logout/$', auth_logout, name='logout'),
    re_path(r'^login/$', auth_login, name='login'),
    re_path(r'^register/$',auth_register, name='register'),
]

#Comment Thread
urlpatterns += [
    re_path(r'^comment/(?P<id>\d+)$',comment_thread, name='comment_thread'),
    re_path(r'^comment/create/$',comment_create_view, name='comment_create'),
]
#Notifications
urlpatterns += [
    re_path(r'^notifications/$', all, name='notifications_all'),
    re_path(r'^notifications/ajax/$',get_notifications_ajax, name='get_notifications_ajax'),
    re_path(r'^notifications/(?P<id>\d+)/$',read, name='notifications_read')]