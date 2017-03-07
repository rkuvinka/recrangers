from django.db import models

# Create your models here.
class Organization(models.Model):
	"""Organization is identified by orgid"""
	lastupdateddate = models.CharField(max_length=100)
	orgabbrname = models.CharField(max_length=10)
	orgid = models.IntegerField(primary_key=True)
	orgimageurl = models.CharField(max_length=150)
	orgjurisdictiontype = models.CharField(max_length=50)
	orgname = models.CharField(max_length=200)
	orgparentid = models.IntegerField()
	orgtype = models.CharField(max_length=200)
	orgurladdress = models.CharField(max_length=200)
	orgurltext = models.CharField(max_length=200)


		