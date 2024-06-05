from data import views as data_views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

urlpatterns = [
    url('recordtype/', data_views.RecordTypeViewSet.as_view()),
    url('latestrecordschema/', data_views.GetLatestRecordSchema.as_view()),
    url('latestrecordcost/', data_views.GetLatestRecordcost.as_view()),
    url('costs/', data_views.RecordCost.as_view()),
    url('getjsonb/(?P<uuids>[^/]+)/$', data_views.CreateJsonViewSet.as_view()),
    url('getbargraph', data_views.WeeklyBarGraph.as_view()),
    url('bindcrashtype/(?P<uuids>[^/]+)/$', data_views.BindCrashTypeViewSet.as_view()),
    url('addcrashorientation/', data_views.CreateCrashDiagramViewset.as_view()),
    url('getcrashorientationbymovementcode/', data_views.GetCrashDiagramOrientationViewset.as_view()),
    url('updatecrashdata/(?P<uuids>[^/]+)/$', data_views.UpdateCrashDiagramViewset.as_view()),
    url('deletemovementcode/', data_views.DeleteMovementCodeAsPerCrashTypeViewset.as_view()),
    url('savedata/', data_views.MakeZipOfData.as_view()),
    url(r'save-irap-details/', data_views.SaveIrapInformation.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
