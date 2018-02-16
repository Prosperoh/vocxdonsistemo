from django.conf.urls import url

from . import views

app_name = 'vocxdonado'
urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)/$', views.DetalojView.as_view(), name='detaloj'),
#        url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),
#            name='results'),
        url(r'^(?P<propono_id>[0-9]+)/vocxdoni/$', views.vocxdoni,
            name='vocxdoni'),
    ]


