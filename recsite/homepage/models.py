from django.db import models

# Create your models here.
class Organization(models.Model):
	"""Organization is identified by orgid"""
	lastupdateddate = models.DateField(max_length=100)
	orgabbrname = models.CharField(max_length=10)
	orgid = models.CharField(max_length=10,primary_key=True)
	orgimageurl = models.CharField(max_length=150)
	orgjurisdictiontype = models.CharField(max_length=50)
	orgname = models.CharField(max_length=200)
	orgparentid = models.CharField(max_length=10)
	orgtype = models.CharField(max_length=200)
	orgurladdress = models.CharField(max_length=200)
	orgurltext = models.CharField(max_length=200)

	def __str__(self):
		return self.orgname

class Facilities(models.Model):
	"""Facilities primary key is facility id"""
	facilityadaaccess = models.CharField(max_length=1000)
	facilitydescription = models.CharField(max_length=1000)
	facilitydirections = models.CharField(max_length=100)
	facilityemail = models.CharField(max_length=150)
	facilityid = models.CharField(max_length=1000)
	facilitylatitude = models.CharField(max_length=200)
	facilitylongitude = models.CharField(max_length=200)
	facilitymapurl = models.CharField(max_length=200)
	facilityname = models.CharField(max_length=200)
	facilityphone = models.CharField(max_length=200)
	facilityreservationurl = models.CharField(max_length=200)
	facilitytypedescription = models.CharField(max_length=200)
	facilityusefeedescription = models.CharField(max_length=200)
	keywords = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	legacyfacilityid = models.CharField(max_length=200)
	orgfacilityid = models.CharField(max_length=200)
	staylimit = models.CharField(max_length=200)

	def __str__(self):
		return self.facilityname

class FacilityAddress(models.Model):
	"""FacilityAddress primary key is address id"""
	addresscountrycode = models.CharField(max_length=200)
	addressstatecode = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	facilityaddressid = models.IntegerField(primary_key=True)
	facilityaddresstype = models.CharField(max_length=200)
	facilityid = models.CharField(max_length=200)
	facilitystreetaddress1 = models.CharField(max_length=200)
	facilitystreetaddress2 = models.CharField(max_length=200)
	facilitystreetaddress3 = models.CharField(max_length=200)
	postalcode = models.CharField(max_length=200)

	def __str__(self):
		return self.facilityaddressid						

class RecAreas(models.Model):
	"""docstring for RecAreas"""
	keywords = models.CharField(max_length=100)
	lastupdateddate = models.CharField(max_length=100)
	orgrecareaid = models.CharField(max_length=100)
	recareadescription = models.CharField(max_length=100000)
	recareadirections = models.CharField(max_length=100000)
	recareaemail = models.CharField(max_length=500)
	recareafeedescription = models.CharField(max_length=100000)
	recareaid = models.CharField(max_length=10,primary_key=True)
	recarealatitude = models.CharField(max_length=100)
	recarealongitude = models.CharField(max_length=100)
	recareamapurl = models.CharField(max_length=100)
	recareaname = models.CharField(max_length=1000)
	recareaphone = models.CharField(max_length=1000)
	recareareservationurl = models.CharField(max_length=1000)
	staylimit = models.CharField(max_length=20)
	
	def __str__(self):
			return self.recareaname

class RecreationalActivity(models.Model):
	"""RecreationalActivity primary key is activity id"""
	activityid = models.IntegerField(primary_key=True)
	activitylevel = models.CharField(max_length=200)
	activityname = models.CharField(max_length=200)
	activityparentid = models.CharField(max_length=200)

	def __str__(self):
		return self.activityname

class EntityLink(models.Model):
	"""EntityLink primary key is address id"""
	description = models.CharField(max_length=200)
	entityid = models.IntegerField(primary_key=True)
	entitytype = models.CharField(max_length=200)
	linktype = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class RecAreaAddress(models.Model):
	"""RecAreaAddress primary key is recareaaddressid"""
	addresscountrycode = models.CharField(max_length=200)
	addressstatecode = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	postalcode = models.CharField(max_length=200)
	recareaaddressid = models.CharField(max_length=200)
	recareaaddresstype = models.CharField(max_length=200)
	recareaid = models.CharField(max_length=200)
	recareastreetaddress1 = models.CharField(max_length=200)
	recareastreetaddress2 = models.CharField(max_length=200)
	recareastreetaddress3 = models.CharField(max_length=200)

	def __str__(self):
		return self.city

class Tour(models.Model):
	"""Tour primary key is tourid"""
	createddate = models.CharField(max_length=200)
	facilityid = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	touraccessible = models.CharField(max_length=200)
	tourdescription = models.CharField(max_length=200)
	tourduration = models.CharField(max_length=200)
	tourid = models.CharField(max_length=200)
	tourname = models.CharField(max_length=200)
	tourtype = models.CharField(max_length=200)

	def __str__(self):
		return self.tourname

class Attribute(models.Model):
	"""Attribute """
	attributeid = models.CharField(max_length=200)
	attributename = models.CharField(max_length=200)
	attributevalue = models.CharField(max_length=200)
	entityid = models.CharField(max_length=200)
	entitytype = models.CharField(max_length=200)

	def __str__(self):
		return self.attributename

class PermitEntrance(models.Model):
	"""Permit Entrance primary key is permitentranceid"""
	createddate = models.CharField(max_length=200)
	district = models.CharField(max_length=200)
	facilityid = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	latitude = models.CharField(max_length=200)
	longitude = models.CharField(max_length=200)
	permitentranceaccessible = models.CharField(max_length=200)
	permitentrancedescription = models.CharField(max_length=200)
	permitentranceid = models.CharField(max_length=200)
	permitentrancename = models.CharField(max_length=200)
	permitentrancetype = models.CharField(max_length=200)
	town = models.CharField(max_length=200)

	def __str__(self):
		return self.permitentrancename

class Campsite(models.Model):
	"""campsite primary key is campstieid"""
	campsiteaccessible = models.CharField(max_length=200)
	campsiteid = models.CharField(max_length=200)
	campsitename = models.CharField(max_length=200)
	campsitetype = models.CharField(max_length=200)
	createddate = models.CharField(max_length=200)
	facilityid = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	loop = models.CharField(max_length=200)
	typeofuse = models.CharField(max_length=200)

	def __str__(self):
		return self.campsiteid		

class EntityActivities(models.Model):
	"""docstring for EntityActivities"""
	activitydescription = models.CharField(max_length=200)
	activityfeeddescription = models.CharField(max_length=200)
	activityid = models.CharField(max_length=200)
	entityid = models.CharField(max_length=200)
	entitytype = models.CharField(max_length=200)

	def __str__(self):
		return self.activityid
	
class Events(models.Model):
	entityid = models.CharField(max_length=200)
	entitytype = models.CharField(max_length=200)
	eventadaaccess = models.CharField(max_length=200)
	eventagegroup = models.CharField(max_length=200)
	eventcomments = models.CharField(max_length=200)
	eventdescription = models.CharField(max_length=200)
	eventemail = models.CharField(max_length=200)
	eventenddate = models.CharField(max_length=200)
	eventfeeddescription = models.CharField(max_length=200)
	eventfrequencydescription = models.CharField(max_length=200)
	eventid = models.CharField(max_length=200)
	eventname = models.CharField(max_length=200)
	eventregistrationrequired = models.CharField(max_length=200)
	eventscopedescription = models.CharField(max_length=200)
	eventstartdate = models.CharField(max_length=200)
	eventtypedescription = models.CharField(max_length=200)
	eventurladdress = models.CharField(max_length=200)
	eventurltext = models.CharField(max_length=200)
	lastupdateddate = models.CharField(max_length=200)
	sponsorclasstype = models.CharField(max_length=200)
	sponsoremail = models.CharField(max_length=200)
	sponsorname = models.CharField(max_length=200)
	sponsorphone = models.CharField(max_length=200)
	sponsorurladdress = models.CharField(max_length=200)
	sponsorurltext = models.CharField(max_length=200)

	def __str__(self):
		return self.eventname

class Media(models.Model):
	credits = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	embedcode = models.CharField(max_length=200)
	entityid = models.CharField(max_length=200)
	entitymediaid = models.CharField(max_length=200)
	entitytype = models.CharField(max_length=200)
	height = models.CharField(max_length=200)
	mediatype = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	width = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class MemberTours(models.Model):
	membertourid = models.CharField(max_length=200)
	tourid = models.CharField(max_length=200)
	tourname = models.CharField(max_length=200)

	def __str__(self):
		return self.tourname

class OrgEntities(models.Model):
	entityid = models.CharField(max_length=200)
	entitytype = models.CharField(max_length=200)
	orgid = models.CharField(max_length=200)

	def __str__(self):
		return self.entityid

class PermitEntranceZone(models.Model):
	permitentranceid = models.CharField(max_length=200)
	permitentrancezoneid = models.CharField(max_length=200)
	zone = models.CharField(max_length=200)

	def __str__(self):
		return self.permitentranceid

class PermittedEquipment(models.Model):
	campsiteid = models.CharField(max_length=200)
	equipmentname = models.CharField(max_length=200)
	maxlength = models.CharField(max_length=200)

	def __str__(self):
		return self.equipmentname

class RecAreaFacility(models.Model):
	facilityid = models.CharField(max_length=200)
	recareaid = models.CharField(max_length=200)

	def __str__(self):
		return self.facilityid