from decimal import Decimal
from shop.models import Producto
from django.conf import settings

class Cart(object):
	def __init__(self,request):
		self.session=request.session
		self.cart=self.session.get(settings.CART_SESSION_ID)
		if not self.cart:
			self.cart=self.session[settings.CART_SESSION_ID]={}
		self.cart=self.cart	

	def add(self,producto,quantity=1, update_quantity=False):
		producto_id=str(producto.id)

		if producto_id not in self.cart:
			self.cart[producto_id] ={
				'quantity':0,
				'precio':str(producto.precio),
			}		

		if update_quantity:
			self.cart[producto_id]['quantity'] = quantity
		else:
			self.cart[producto_id]['quantity'] += quantity
		self.save()
		
	def save(self):
		self.session[settings.CART_SESSION_ID]=self.cart
		self.session.modifiel=True	
	




	def remove(self, producto):
		producto_id=str(producto.id)
		if producto_id in self.cart:
			del self.cart[producto_id]
			self.save()


	def __iter__(self):
		producto_ids=self.cart.keys()
		productos=Producto.objects.filter(id__in=producto_ids)
		for producto in productos:
			self.cart[str(producto.id)]['producto']=producto

		for item in self.cart.values():
			item['precio']=Decimal(item['precio'])
			item['precio_total']=item['precio']*item['quantity']
			yield item		

	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())


	def get_total_precio(self):
		return sum(Decimal(item['precio'])*item['quantity'] for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modifiel=True		

