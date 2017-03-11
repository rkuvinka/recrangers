from django.core.management.base import BaseCommand, CommandError
from homepage.models import Organization,RecAreas,Facilities,FacilityAddress,RecreationalActivity,EntityLink,RecAreaAddress,Tour,Attribute,PermitEntrance,Campsite,EntityActivities,Events,Media,MemberTours,OrgEntities,PermitEntranceZone,PermittedEquipment,RecAreaFacility
import csv
from datetime import datetime

class Command(BaseCommand):
	"""docstring for Command"""
	help = 'This procedure imports data from Organization.csv to Organization table'
	
	def add_arguments(self,parser):
		parser.add_argument('file_name')
		parser.add_argument('object_type')

	def handle(self, *args, **options):

		filepath = options['file_name']
		object_ = options['object_type']

		dataReader = csv.reader(open(filepath,encoding='ISO-8859-1'), delimiter=',', quotechar='"')
		next(dataReader) # Skips header


		for row in dataReader:
			if object_ == 'organization':
				org = Organization()
				try:
					org.lastupdateddate = datetime.strptime(row[0],'%Y-%m-%d').date()
				except:
					org.lastupdateddate = None	
				org.orgabbrname = row[1]
				try:
					org.orgid = int(row[2])
				except:
					org.orgid = None	
				org.orgimageurl = row[3]
				org.orgjurisdictiontype = row[4]
				org.orgname = row[5]
				try:
					org.orgparentid = int(row[6])
				except:
					org.orgparentid = None	
				org.orgtype = row[6]
				org.orgurladdress = row[6]
				org.orgurltext = row[7]
				org.save()
			elif object_ == 'recarea':
				recarea = RecAreas()
				recarea.keywords = row[0]
				recarea.lastupdateddate = row[1]
				recarea.orgrecareaid = row[2]
				recarea.recareadescription = row[3]
				recarea.recareadirections = row[4]
				recarea.recareaemail = row[5]
				recarea.recareafeedescription = row[6]
				recarea.recareaid = row[7]
				recarea.recarealatitude = row[8]
				recarea.recarealongitude = row[9]
				recarea.recareamapurl = row[10]
				recarea.recareaname = row[11]
				recarea.recareaphone = row[12]
				recarea.recareareservationurl = row[13]
				recarea.staylimit = row[14]
				recarea.save()
			elif object_ == 'facility':
				fac = Facilities()
				fac.facilityadaaccess = row[0]
				fac.facilitydescription = row[1]
				fac.facilitydirections = row[2]
				fac.facilityemail = row[3]
				try:
					fac.facilityid = int(row[4])
				except:
					fac.facilityid = None
				try:		
					fac.facilitylatitude = float(row[5])
				except:
					fac.facilitylatitude = None
				try:		
					fac.facilitylongitude = float(row[6])
				except:
					fac.facilitylongitude = None	
				fac.facilitymapurl = row[7]
				fac.facilityname = row[8]
				fac.facilityphone = row[9]
				fac.facilityreservationurl = row[10]
				fac.facilitytypedescription = row[11]
				fac.facilityusefeedescription = row[12]
				fac.keywords = row[13]
				try:
					fac.lastupdateddate = datetime.strptime(row[14],'%Y-%m-%d').date()
				except:
					fac.lastupdateddate = None
				try:	
					fac.legacyfacilityid = int(row[15])
				except:
					fac.legacyfacilityid = None
				try:		
					fac.orgfacilityid = int(row[16])
				except:
					fac.orgfacilityid = None	
				fac.save()
			elif object_ == 'facility_address':
				facadd = FacilityAddress()
				facadd.addresscountrycode = row[0]
				facadd.addressstatecode = row[1]
				facadd.city = row[2]
				try:
					facadd.facilityaddressid = int(row[3])
				except:
					facadd.facilityaddressid = None
				facadd.facilityaddresstype = row[4]
				try:
					facadd.facilityid = int(row[5])
				except:
					facadd.facilityid = None	
				facadd.facilitystreetaddress1 = row[6]
				facadd.facilitystreetaddress2 = row[7]
				facadd.facilitystreetaddress3 = row[8]
				try:
					facadd.postalcode = int(row[9])
				except:
					facadd.postalcode = None	
				facadd.save()
			elif object_ == 'rec_activity':
				recactivity = RecreationalActivity()
				recactivity.activityid = row[0]
				recactivity.activitylevel = row[1]
				recactivity.activityname = row[2]
				recactivity.activityparentid = row[3]
				recactivity.save()	
			elif object_ == 'entity_link':
				entitylink = EntityLink()
				entitylink.description = row[0]
				entitylink.entityid = row[1]
				entitylink.entitytype = row[2]
				entitylink.linktype = row[3]
				entitylink.title = row[4]
				entitylink.url = row[5]
				entitylink.save()
			elif object_ == 'rec_addr':
				recaddress = RecAreaAddress()
				recaddress.addresscountrycode = row[0]
				recaddress.addressstatecode = row[1]
				recaddress.city = row[2]
				recaddress.lastupdateddate = row[3]
				recaddress.postalcode = row[4]
				recaddress.recareaaddressid = row[5]
				recaddress.recareaaddresstype = row[6]
				recaddress.recareaid = row[7]
				recaddress.recareastreetaddress1 = row[8]
				recaddress.recareastreetaddress2 = row[9]
				recaddress.recareastreetaddress3 = row[10]
				recaddress.save()
			elif object_ == 'tour':
				tour = Tour()
				tour.createddate = row[0]
				tour.facilityid = row[1]
				tour.lastupdateddate = row[2]
				tour.touraccessible = row[3]
				tour.tourdescription = row[4]
				tour.tourduration = row[5]
				tour.tourid = row[6]
				tour.tourname = row[7]
				tour.tourtype = row[8]
				tour.save()
			elif object_ == 'attribute':
				attr = Attribute()
				attr.attributeid = row[0]
				attr.attributename = row[1]
				attr.attributevalue = row[2]
				attr.entityid = row[3]
				attr.entitytype = row[4]
				attr.save()	
			elif object_ == 'permit_entrance':
				permitentrance = PermitEntrance()
				permitentrance.createddate = row[0]
				permitentrance.district = row[1]
				permitentrance.facilityid = row[2]
				permitentrance.lastupdateddate = row[3]
				permitentrance.latitude = row[4]
				permitentrance.longitude = row[5]
				permitentrance.permitentranceaccessible = row[6]
				permitentrance.permitentrancedescription = row[7]
				permitentrance.permitentranceid = row[8]
				permitentrance.permitentrancename = row[9]
				permitentrance.permitentrancetype = row[10]
				permitentrance.town = row[11]
				permitentrance.save()	
			elif object_ == 'campsite':
				campsite = Campsite()
				campsite.campsiteaccessible = row[0]
				campsite.campsiteid = row[1]
				campsite.campsitename = row[2]
				campsite.campsitetype = row[3]
				campsite.createddate = row[4]
				campsite.facilityid = row[5]
				campsite.lastupdateddate = row[6]
				campsite.loop = row[7]
				campsite.typeofuse = row[8]	
				campsite.save()
			elif object_ == 'entity_activity':
				entity_act = EntityActivities()
				entity_act.activitydescription = row[0]
				entity_act.activityfeeddescription = row[1]
				entity_act.activityid = row[2]
				entity_act.entityid = row[3]
				entity_act.entitytype = row[4]
				entity_act.save()
			elif object_ == 'event':
				event = Events()	
				event.entityid = row[0]
				event.entitytype = row[1]
				event.eventadaaccess = row[2]
				event.eventagegroup = row[3]
				event.eventcomments = row[4]
				event.eventdescription = row[5]
				event.eventemail = row[6]
				event.eventenddate = row[7]
				event.eventfeeddescription = row[8]
				event.eventfrequencydescription = row[9]
				event.eventid = row[10]
				event.eventname = row[11]
				event.eventregistrationrequired = row[12]
				event.eventscopedescription = row[13]
				event.eventstartdate = row[14]
				event.eventtypedescription = row[15]
				event.eventurladdress = row[16]
				event.eventurltext = row[17]
				event.lastupdateddate = row[18]
				event.sponsorclasstype = row[19]
				event.sponsoremail = row[20]
				event.sponsorname = row[21]
				event.sponsorphone = row[22]
				event.sponsorurladdress = row[23]
				event.sponsorurltext = row[24]
				event.save()
			elif object_ == 'media':
				media = Media()
				media.credits = row[0]
				media.description = row[1]
				media.embedcode = row[2]
				media.entityid = row[3]
				media.entitymediaid = row[4]
				media.entitytype = row[5]
				media.height = row[6]
				media.mediatype = row[7]
				media.subtitle = row[8]
				media.title = row[9]
				media.url = row[10]
				media.width = row[11]
				media.save()
			elif object_ == 'member_tours':
				member_tours = MemberTours()
				member_tours.membertourid = row[0]
				member_tours.tourid = row[1]
				member_tours.tourname = row[2]
				member_tours.save()
			elif object_ == 'org_entities':
				org_entities = OrgEntities()
				org_entities.entityid = row[0]
				org_entities.entitytype = row[1]
				org_entities.orgid = row[2]
				org_entities.save()	
			elif object_ == 'permit_entrance_zone':
				permit_entrance_zone = PermitEntranceZone()	
				permit_entrance_zone.permitentranceid = row[0]
				permit_entrance_zone.permitentrancezoneid = row[1]
				permit_entrance_zone.zone = row[2]
				permit_entrance_zone.save()
			elif object_ == 'permitted_equipment':
				permitted_equipment = PermittedEquipment()
				permitted_equipment.campsiteid = row[0]
				permitted_equipment.equipmentname = row[1]
				permitted_equipment.maxlength = row[2]
				permitted_equipment.save()	
			elif object_ == 'rec_area_facility':
				rec_area_facility = RecAreaFacility()
				rec_area_facility.facilityid = row[0]
				rec_area_facility.recareaid = row[1]
				rec_area_facility.save()	