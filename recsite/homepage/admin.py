from django.contrib import admin

# Register your models here.
from .models import Organization,RecAreas,Facilities,FacilityAddress,RecreationalActivity,EntityLink,RecAreaAddress,Tour,Attribute,PermitEntrance,Campsite,EntityActivities,Events,Media,MemberTours,OrgEntities,PermitEntranceZone,PermittedEquipment,RecAreaFacility

admin.site.register(Organization)
admin.site.register(RecAreas)
admin.site.register(Facilities)
admin.site.register(FacilityAddress)
admin.site.register(RecreationalActivity)
admin.site.register(EntityLink)
admin.site.register(RecAreaAddress)
admin.site.register(Tour)
admin.site.register(Attribute)
admin.site.register(PermitEntrance)
admin.site.register(Campsite)
admin.site.register(EntityActivities)
admin.site.register(Events)
admin.site.register(Media)
admin.site.register(MemberTours)
admin.site.register(OrgEntities)
admin.site.register(PermitEntranceZone)
admin.site.register(PermittedEquipment)
admin.site.register(RecAreaFacility)