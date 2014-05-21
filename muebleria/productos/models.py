from django.db import models



class Categoria(models.Model):

	id=models.AutoField(primary_key=True)

	categoria=models.CharField(max_length=55)



	def __unicode__(self):

	   return self.categoria



class Producto(models.Model):

	id=models.AutoField(primary_key=True)

	nombre=models.CharField(max_length=55)

	precio=models.DecimalField(max_digits=8,     	decimal_places=2)
  
	categoria=models.ForeignKey(Categoria)



	def __unicode__(self):

	   return self.nombre
