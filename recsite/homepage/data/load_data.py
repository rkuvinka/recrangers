# Full path and name to your csv file
csv_filepathname="/Users/Proxima/Documents/capstone/recrangers/recsite/homepage/data/Organizations_API_v1.csv"
# Full path to your django project directory
your_djangoproject_home="/Users/Proxima/Documents/capstone/recrangers/recsite"

# import sys,os
# sys.path.append(your_djangoproject_home)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from homepage.models import Organization

import csv
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