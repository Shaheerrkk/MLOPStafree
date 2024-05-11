from django.contrib import admin
from .models import Item
from import_export.admin import ImportExportModelAdmin 

class itemAdmin(ImportExportModelAdmin):
    list_display=['item_identifier','item_weight','item_fat_content','item_visibility','item_type','item_mrp','outlet_identifier','outlet_establishment_year','outlet_size','outlet_location_type','outlet_type','item_outlet_sales']


admin.site.register(Item,itemAdmin)
