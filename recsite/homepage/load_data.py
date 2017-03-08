
# Full path to your django project directory
your_djangoproject_home="/Users/RK/Desktop/recrangers/recsite"

import sys,os

from django.core.wsgi import get_wsgi_application


sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'recsite.settings'
application = get_wsgi_application()

from homepage.models import Organization

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


csv_filepathname="/Users/RK/Desktop/recrangers/recsite/homepage/Facilities_API_v1.csv"
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
	next(dataReader)
	fac = Facilities()
	fac.facilityadaaccess = row[0]
	fac.facilitydescription = row[1]
	fac.facilitydirections = row[2]
	fac.facilityemail = row[3]
	fac.facilityid = row[4]
	fac.facilitylatitude = row[5]
	fac.facilitylongitude = row[6]
	fac.facilitymapurl = row[7]
	fac.facilityname = row[8]
	fac.facilityphone = row[9]
	fac.facilityreservationurl = row[10]
	fac.facilitytypedescription = row[11]
	fac.facilityusefeedescription = row[12]
	fac.keywords = row[13]
	fac.lastupdateddate = row[14]
	fac.legacyfacilityid = row[15]
	fac.orgfacilityid = row[16]
	fac.staylimit = row[17]
	fac.save()