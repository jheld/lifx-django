from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lifx_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from lifx_management import views
urlpatterns += patterns('',
                        url(r'^$',views.ScheduleCycleView.as_view(),name='schedule_cycle'),
                        )
