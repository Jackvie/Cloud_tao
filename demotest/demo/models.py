from django.db import models

# Create your models here.
class JD(models.Model):
	id = models.IntegerField(primary_key=True)
	t = models.DateTimeField()

class AD(models.Model):
	id = models.IntegerField(primary_key=True)
	class Meta:
		db_table='test2'

class One(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40)
	class Meta:
		db_table = 'one'

class Many(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40)
	fk = models.ForeignKey('demo.One', on_delete=models.SET_NULL,null=True, blank=True)
	class Meta:
		db_table = 'many'

	
