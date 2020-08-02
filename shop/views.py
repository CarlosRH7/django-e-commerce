from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from .models import Producto, Categoria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm
from django.db.models import Q

# class Inicio(View):
# 	def get(self,request):
# 		productos=Producto.objects.all()
# 		return render(request,'shop/inicio.html',{'productos':productos})









class Inicio(View):
	def get(self,request,categoria_slug=None):
		categoria=None
		categorias=Categoria.objects.all()
		productos=Producto.objects.filter(available=True)
		if categoria_slug:
			categoria=get_object_or_404(Categoria,slug=categoria_slug)
			productos=productos.filter(categoria=categoria)
		paginator=Paginator(productos,12)
		page=request.GET.get('page')
		try:
			prods=paginator.page(page)
		except PageNotAnInteger:
			prods=paginator.page(1)
		except EmptyPage:
			prods=paginator.page(paginator.num_pages)
		template='shop/inicio.html'
		context={
		'categoria':categoria,
		'categorias':categorias,
		'productos':prods,
		'page':page
		}
		return render(request,template,context)	

# metodo de busqueda de un producto

class Searchs(View):
	def get(self, request):
	    query = request.GET.get('b', '')
	    if query:
	        qset = (
	            Q(nombre__icontains=query) 
	        )
	        results = Producto.objects.filter(qset).distinct()
	    else:
	        results = []
	    template='shop/busqueda.html'
	    context={
	    	"results": results,
	        "query": query
	    }
	    return render(request,template,context)		

class DetalleShop(View):
	def get(self,request,id):
		producto=Producto.objects.get(id=id)
		template_name='shop/detalle_shop.html'
		form=CartAddProductForm()
		context={
			'producto':producto,
			'form':form,
		}
		return render(request,template_name,context)
				