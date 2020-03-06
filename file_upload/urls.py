from django.conf.urls import include, url
from django.contrib import admin
from share.views import HomeView, DispalyView, MyView, SearchView

urlpatterns = [
    # Examples:
    # url(r'^$', 'file_upload.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^s/(?P<code>\d+)/$', DispalyView.as_view()),
    url(r'^search/', SearchView.as_view(), name="search"),
    url(r'^my/$', MyView.as_view(), name="MY"),
]
