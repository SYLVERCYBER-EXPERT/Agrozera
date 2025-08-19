from django.contrib import admin
from FarmerInfo.models import FarmerData, FarmSupply

# Register Famer Data models
admin.site.register(FarmerData)

# Register Farm Supply models
admin.site.register(FarmSupply)