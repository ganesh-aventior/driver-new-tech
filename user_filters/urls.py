from django.conf.urls import url
from . import views

urlpatterns = [
    url('bindfilters/(?P<uuids>[^/]+)/$', views.BindVehicalFilterViewSet.as_view()),
    url('bindincidentdetailsfilters/(?P<uuids>[^/]+)/$', views.BindIncidentDetailFilterViewSet.as_view()),
    url(r'intervention-detail-type/', views.InterventionDetailType.as_view())
]
