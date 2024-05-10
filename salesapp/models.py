from django.db import models

class Item(models.Model):
    item_identifier = models.CharField(max_length=50)
    item_weight = models.FloatField(null=True)  # Null=True to allow NULL values
    item_fat_content = models.CharField(max_length=20)
    item_visibility = models.FloatField()
    item_type = models.CharField(max_length=50)
    item_mrp = models.FloatField()
    outlet_identifier = models.CharField(max_length=20)
    outlet_establishment_year = models.IntegerField()
    outlet_size = models.CharField(max_length=20, null=True)  # Null=True to allow NULL values
    outlet_location_type = models.CharField(max_length=20)
    outlet_type = models.CharField(max_length=20)
    item_outlet_sales = models.FloatField()

    def __str__(self):
        return self.item_identifier
 