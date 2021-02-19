from django.conf.urls import url
from production import views
urlpatterns = [
    url(r'^api/production$',views.production_list),
    url(r'^api/production/(?P<pk>[0-9]+)$',views.production_detail),
]