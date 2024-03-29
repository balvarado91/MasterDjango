from django.db import models

from productos.models import Producto

from clientes.models import Cliente



class Venta(models.Model):

	id=models.AutoField(primary_key=True)

	factura=models.IntegerField()

	fecha=models.DateTimeField(auto_now=False, auto_now_add=False)

	cliente=models.ForeignKey(Cliente)

	productos=models.ManyToManyField(Producto)



	def __unicode__(self):

	   return unicode(self.factura)
