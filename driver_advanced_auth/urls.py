from django.conf.urls import url
from . import views
from data import views as data_views

urlpatterns = [
    url('newusers/', views.UserList.as_view()),
    url('userbyid/(?P<pk>[0-9]+)/$', views.UserById.as_view()),
    url('city/', views.CityList.as_view()),
    url('org/', views.OrganizationList.as_view()),
    url('getregion/', views.GetRegion.as_view()),
    url('getcountry/', views.GetCountry.as_view()),
    url('driver-group/', views.DriverGroup.as_view()),
    url('groupbyid/(?P<pk>[0-9]+)/$', views.GroupById.as_view()),
    url('getcontentpermission/', views.GetContentTypesbyname.as_view()),
    url('getlistmodels/', views.GetContentTypes.as_view()),
    url('getpermissionbymodule/', views.permissionByContentId.as_view()),
    url('getgrouppermission/', views.GetGroupWisePermission.as_view()),
    url('requestforrole/', views.RequestForRole.as_view()),
    # new_api's
    url('get-auth-user-details-list/(?P<id>[0-9]+)/$', views.GetAuthUserListDetails.as_view()),
    url('driver-group-detail/(?P<id>[0-9]+)/$', views.DriverGroupDetail.as_view()),
    url('city-details/(?P<id>[0-9]+)/$', views.CityDetailList.as_view()),
    url('org-detail/(?P<id>[0-9]+)/$', views.OrganisationDetailList.as_view()),
    url('adv-registration/', views.AdvUserRegisterAPI.as_view()),
    url('adv-registration-detail/(?P<id>[0-9]+)/$', views.AdvUserRegisterDetailAPI.as_view()),
    url('user-info/(?P<id>[0-9]+)/$', views.UserDetails.as_view()),
    url(r'region-cities/(?P<uuids>[^/AdvUserRegisterDetailAPI]+)/$', views.RegionCities.as_view()),
    url(r'region-organization/(?P<uuids>[^/]+)/$', views.RegionOrganization.as_view()),
    url(r'get-role-detail/(?P<id>[0-9]+)/$', views.RoleDetails.as_view()),
    url(r'accept-role-request/(?P<user>[0-9]+)/$', views.AcceptRoleRequest.as_view()),
    url(r'reject-role-request/(?P<user>[0-9]+)/$', views.RejectRoleRequest.as_view()),
    url(r'region-name/(?P<uuids>[^/]+)/$', views.RegionNames.as_view()),
    url(r'check-role-requested-status/(?P<id>[0-9]+)/', views.CheckRoleStatus.as_view()),
    url(r'getcities/', views.GetCities.as_view()),
    url('weather-info/', views.WeatherInfoDetails.as_view()),
    url('weather-info-details/(?P<id>[0-9]+)/', views.WeatherInfoDetailById.as_view()),
    url('google-login/', views.RegisterGoogleUser.as_view()),
    url(r'use-as-record/', data_views.UseRecord.as_view()),
    url(r'merged-and-updated-records/(?P<uuids>[^/]+)/$', views.MergedAndUpdatedRecords.as_view()),
    url(r'find-existing-records/', views.FindExisting.as_view()),
    url(r'get-json-key/', views.GetJsonSchemaKey.as_view()),
    url(r'get-intervention-type-detail/(?P<uuid>[^/]+)/$', views.intervention_type_detail)
]
