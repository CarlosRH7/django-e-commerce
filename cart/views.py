from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Producto
from .cart import Cart
from .forms import CartAddProductForm
from django.views.generic import View



class CartAdd(View):
	def post(self,request,producto_id):
		cart=Cart(request)
		producto=get_object_or_404(Producto,id=producto_id)
		form=CartAddProductForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			cart.add(producto=producto,quantity=cd['quantity'],
				update_quantity=cd['update'])
		return redirect('cart:cart_detail')



class CartRemove(View):
	def get(self,request,producto_id):
		cart=Cart(request)
		producto=get_object_or_404(Producto,id=producto_id)
		cart.remove(producto)
		return redirect('cart:cart_detail')


class CartDetail(View):
	def get(self,request):
		cart=Cart(request)
		template="cart/detail.html"
		for item in cart:
			item['update_quantity_form']=CartAddProductForm(initial={'quantity':item['quantity'],'update':True})
		context={
		'cart':cart
		}
		return render(request,template,context)




