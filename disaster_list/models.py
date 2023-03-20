from django.db import models

class DisasterList(models.Model):
    dis_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    disaster_group = models.CharField(max_length=50)
    disaster_type = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    iso = models.CharField(max_length=3)
    total_affected = models.IntegerField()
    total_damages_usd = models.FloatField()
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'disaster_list'

    def __str__(self):
        return f"{self.disaster_type} - {self.country} - {self.year}"
    