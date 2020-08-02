from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views.generic import View

# from .tasks import order_created



class OrderCreate(View):
	def get(sefl,request):
		cart=Cart(request)
		form=OrderCreateForm()
		template='orders/order/create.html'
		context={
		'cart':cart,
		'form':form
		}
		return render(request,template,context)

	def post(self,request):
		cart=Cart(request)
		form=OrderCreateForm(request.POST)
		if form.is_valid():
			order=form.save()
			for item in cart:
				OrderItem.objects.create(order=order,
					producto=item['producto'],
					precio=item['precio'],
					quantity=item['quantity'])
			# Borrar el carrito
			cart.clear()

			request.session['order_id']=order.id
			return redirect(reverse('payment:process'))

		else:
			cart=Cart(request)
			form=OrderCreateForm(request.POST)
			template='orders/order/create.html'
			context={
			'cart':cart,
			'form':form
			}
			return render(request,template,context)



