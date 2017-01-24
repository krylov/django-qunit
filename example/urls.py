from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^qunit/', include('django_qunit.urls'))
)
