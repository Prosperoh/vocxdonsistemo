from django.conf.urls import url

from . import views

app_name = 'vocxdonado'
urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^uzantoj/$', views.UzantojView.as_view(), name='uzantoj'),
        url(r'^(?P<pk>[0-9]+)/$', views.ProponojView.as_view(), name='detaloj'),
#        url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),
#            name='results'),
        url(r'^(?P<propono_id>[0-9]+)/vocxdoni/$', views.vocxdoni,
            name='vocxdoni'),
        url(r'^krei_proponon/$', views.krei_proponon,
            name='krei_proponon'),
    ]


