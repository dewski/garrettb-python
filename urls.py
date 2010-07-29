from django.conf.urls.defaults import *
from django.contrib import admin

# Posts
urlpatterns = patterns('posts.views',
    (r'^$', 'index'),
    (r'^post/(?P<slug>[A-Za-z_-]+)/$', 'show'),
)

# Admin
admin.autodiscover()
urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)