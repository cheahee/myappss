from django.urls import path

from address import views

urlpatterns=[
    path("",views.home),
    path("list",views.list),
    path("write",views.write),
    path("insert",views.insert),
    path("detail",views.detail),
    path("update",views.update),
]