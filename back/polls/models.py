from django.db import models

class graficas(models.Model):
	tipo = models.CharField(max_length=200)
	titulo = models.CharField(max_length=200)
	cantidad = models.IntegerField()
	nombre1 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero1 = models.IntegerField(default=None, blank=True, null=True)
	nombre2 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero2 = models.IntegerField(default=None, blank=True, null=True)
	nombre3 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero3 = models.IntegerField(default=None, blank=True, null=True)
	nombre4 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero4 = models.IntegerField(default=None, blank=True, null=True)
	nombre5 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero5 = models.IntegerField(default=None, blank=True, null=True)
	nombre6 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero6 = models.IntegerField(default=None, blank=True, null=True)
	nombre7 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero7 = models.IntegerField(default=None, blank=True, null=True)
	nombre8 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero8 = models.IntegerField(default=None, blank=True, null=True)
	nombre9 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero9 = models.IntegerField(default=None, blank=True, null=True)
	nombre10 = models.CharField(max_length=200, default=None, blank=True, null=True)
	numero10 = models.IntegerField(default=None, blank=True, null=True)
