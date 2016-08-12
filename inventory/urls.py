# from django.conf.urls import url
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from inventory.views import InventoryDetail, SaveLoginDetails

from inventory import views

urlpatterns = [
    url(r'^inventory/$', views.InventoryList.as_view()),
    url(r'^inventory/(?P<pk>[0-9]+)$', views.InventoryDetail.as_view()),
    url(r'^save_logindetails/$', views.SaveLoginDetails.as_view()),

	]

urlpatterns = format_suffix_patterns(urlpatterns)
