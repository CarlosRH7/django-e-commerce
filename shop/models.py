from django.db import models
from django.core.urlresolvers import reverse



class Categoria(models.Model):
	nombre=models.CharField(max_length=200,db_index=True)
	slug=models.SlugField(max_length=200,db_index=True,unique=True)
	img=models.ImageField(blank=True,null=True)


	class Meta:
		ordering=('nombre',)
		verbose_name='categoria'
		verbose_name_plural='categorias'

	def __str__(self):
		return self.nombre
	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args=[self.slug])


class Producto(models.Model):
	categoria=models.ForeignKey(Categoria,related_name='productos')
	nombre=models.CharField(max_length=140)
	slug=models.SlugField(max_length=200,db_index=True)
	desc=models.TextField()
	precio=models.CharField(max_length=10)
	img=models.ImageField(blank=True,null=True)
	clave=models.CharField(max_length=30)
	marca=models.CharField(max_length=50)
	stock=models.PositiveIntegerField()
	available=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)


	class Meta:
		ordering=('nombre',)
		index_together=(('id','slug'),)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('shop:product_detail',
			args=[self.id,self.slug])

