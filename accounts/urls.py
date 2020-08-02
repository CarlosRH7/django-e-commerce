from django.conf.urls import url
from django.contrib.auth import views as djangoViews
from . import views


urlpatterns=[
	url(r'^profile/$',views.Perfil.as_view(),name="profile"),
	url(r'^login/$', djangoViews.login, name="login"),
	url(r'^logout/$', djangoViews.logout, name="logout"),
	url(r'^registration/$', views.Register.as_view(),name="registration"),
]
