
# Full path to your django project directory
your_djangoproject_home="/Users/RK/Desktop/recrangers/recsite"

import sys,os

from django.core.wsgi import get_wsgi_application


sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'recsite.settings'
application = get_wsgi_application()

from homepage.models import Organization
from homepage.models import Facilities

import csv

csv_filepathname="/Users/RK/Desktop/recrangers/recsite/homepage/Organizations_API_v1.csv"
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
	if row[0] != 'LASTUPDATEDDATE,ORGABBREVNAME,ORGID,ORGIMAGEURL,ORGJURISDICTIONTYPE,ORGNAME,ORGPARENTID,ORGTYPE,ORGURLADDRESS,ORGURLTEXT':
		org = Organization()
		org.lastupdateddate = row[0]
		org.orgabbrname = row[1]
		org.orgid = row[2]
		org.orgimageurl = row[3]
		org.orgjurisdictiontype = row[4]
		org.orgname = row[5]
		org.orgparentid = row[6]
		org.orgtype = row[6]
		org.orgurladdress = row[6]
		org.orgurltext = row[7]
		org.save()


# csv_filepathname="/Users/RK/Desktop/recrangers/recsite/homepage/Facilities_API_v1.csv"
# dataReader = csv.reader(open(csv_filepathname, encoding='ISO-8859-1'), delimiter=',', quotechar='"')

# for row in dataReader:
# 	fac = Facilities()
# 	fac.facilityadaaccess = row[0]
# 	fac.facilitydescription = row[1]
# 	fac.facilitydirections = row[2]
# 	fac.facilityemail = row[3]
# 	fac.facilityid = row[4]
# 	fac.facilitylatitude = row[5]
# 	fac.facilitylongitude = row[6]
# 	fac.facilitymapurl = row[7]
# 	fac.facilityname = row[8]
# 	fac.facilityphone = row[9]
# 	fac.facilityreservationurl = row[10]
# 	fac.facilitytypedescription = row[11]
# 	fac.facilityusefeedescription = row[12]
# 	fac.keywords = row[13]
# 	fac.lastupdateddate = row[14]
# 	fac.legacyfacilityid = row[15]
# 	fac.orgfacilityid = row[16]

# 	fac.save()

# for row in dataReader:
# 	facadd = FacilityAddress()
# 	facadd.addresscountrycode = row[0]
# 	facadd.addressstatecode = row[1]
# 	facadd.city = row[2]
# 	facadd.facilityaddressid = row[3]
# 	facadd.facilityaddresstype = row[4]
# 	facadd.facilityid = row[5]
# 	facadd.facilitystreetaddress1 = row[6]
# 	facadd.facilitystreetaddress2 = row[7]
# 	facadd.facilitystreetaddress3 = row[8]
# 	facadd.postalcode = row[9]


# 	facadd.save()


# for row in dataReader:
# 	recarea = RecAreas()
# 	recarea.keywords = row[0]
# 	recarea.lastupdateddate = row[1]
# 	recarea.orgrecareaid = row[2]
# 	recarea.recareadescription = row[3]
# 	recarea.recareadirections = row[4]
# 	recarea.recareaemail = row[5]
# 	recarea.recareafeedescription = row[6]
# 	recarea.recareaid = row[7]
# 	recarea.recarealatitude = row[8]
# 	recarea.recarealongitude = row[9]
# 	recarea.recareamapurl = row[10]
# 	recarea.recareaname = row[11]
# 	recarea.recareaphone = row[12]
# 	recarea.recareareservationurl = row[13]


# 	recarea.save()





# for row in dataReader:
# 	recactivity = RecreationalActivity()
# 	recactivity.activityid = row[0]
# 	recactivity.activitylevel = row[1]
# 	recactivity.activityname = row[2]
# 	recactivity.activityparentid = row[3]


# 	recactivity.save()



# for row in dataReader:
# 	entitylink = EntityLink()
# 	entitylink.description = row[0]
# 	entitylink.entityid = row[1]
# 	entitylink.entitytype = row[2]
# 	entitylink.linktype = row[3]
# 	entitylink.title = row[4]
# 	entitylink.url = row[5]

# 	entitylink.save()



# for row in dataReader:
# 	recaddress = RecAreaAddress()
# 	recaddress.addresscountrycode = row[0]
# 	recaddress.addressstatecode = row[1]
# 	recaddress.city = row[2]
# 	recaddress.lastupdateddate = row[3]
# 	recaddress.postalcode = row[4]
# 	recaddress.recareaaddressid = row[5]
# 	recaddress.recareaaddresstype = row[6]
# 	recaddress.recareaid = row[7]
# 	recaddress.recareastreetaddress1 = row[8]
# 	recaddress.recareastreetaddress2 = row[9]
# 	recaddress.recareastreetaddress3 = row[10]

# 	recaddress.save()




# for row in dataReader:
# 	tour = Tour()
# 	tour.createddate = row[0]
# 	tour.facilityid = row[1]
# 	tour.lastupdateddate = row[2]
# 	tour.touraccessible = row[3]
# 	tour.tourdescription = row[4]
# 	tour.tourduration = row[5]
# 	tour.tourid = row[6]
# 	tour.tourname = row[7]
# 	recaddress.tourtype = row[8]

# 	tour.save()


# for row in dataReader:
# 	permitentrance = PermitEntrance()
# 	permitentrance.createddate = row[0]
# 	permitentrance.district = row[1]
# 	permitentrance.facilityid = row[2]
# 	permitentrance.lastupdateddate = row[3]
# 	permitentrance.latitude = row[4]
# 	permitentrance.longitude = row[5]
# 	permitentrance.permitentranceaccessible = row[6]
# 	permitentrance.permitentrancedescription = row[7]
# 	permitentrance.permitentranceid = row[8]
# 	permitentrance.permitentrancename = row[9]
# 	permitentrance.permitentrancetype = row[10]
# 	permitentrance.town = row[11]

# 	permitentrance.save()

