import csv

import os
import django
import sys

your_djangoproject_home="/Users/RK/Desktop/recrangers/recsite"
sys.path.append(your_djangoproject_home)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recsite.settings")
django.setup()

from models import Facilities



with open('Facilities_API_v1.csv') as f:
	reader = csv.reader(f, encoding='ISO-8859-1')
	for row in reader:
	    _, created = Facilities.objects.get_or_create(
	        facilityadaaccess=row[0],
	        facilitydescription=row[1],
	        facilitydirections=row[2],
	        )