from django.conf.urls import url,include
from django.contrib import admin
from shop import urls as shopURL
from django.views.static import serve
from django.conf import settings
from cart import urls as cartUrls
from orders import urls as ordersUrls
from accounts import urls as accountURL
# from paypal.standard.ipn import urls as paypalUrls
# from payment import urls as paymentUrls

urlpatterns = [
    # url(r'^paypal/',include(paypalUrls)),
    # url(r'^payment/',include(paymentUrls,namespace='payment')),
    url(r'^orders/',include(ordersUrls,namespace='orders')),
    url(r'^cart/',include(cartUrls,namespace='cart')),
    url(r'^admin/', admin.site.urls),
    url(r'^',include(shopURL)),
    url(r'^',include(shopURL,namespace='shop')),
    url(r'^accounts/',include(accountURL)),


     url(

    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}
    	),   
]
