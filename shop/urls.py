from django.conf.urls import url
from . import views

urlpatterns=[

	url(r'^busqueda/$',views.Searchs.as_view(),name="busqueda"),

	url(r'^(?P<id>\d+)/$',views.DetalleShop.as_view(),name="detalle_shop"),

	url(r'^$',views.Inicio.as_view(),name="inicio"),

	url(r'^(?P<categoria_slug>[-\w]+)/$',
		views.Inicio.as_view(),
		name='product_list_by_category'),

		url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
		views.Inicio.as_view(),
		name='product_detail'),

]