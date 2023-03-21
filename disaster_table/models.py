from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class summary(models.Model):
    Dis_ID = models.IntegerField()
    Year = models.IntegerField()
    Disaster_Group = models.TextField()
    Disaster_Type = models.TextField()
    Country = models.TextField()
    ISO = models.TextField()
    Total_Affected = models.TextField()
    Total_Damages = models.TextField()

    def __str__(self):
        return self.Dis_ID, self.Year, self.Disaster_Group, self.Disaster_Type, self.Country,self.ISO, self.Total_Affected, self.Total_Damages
class details(models.Model):
    Dis_ID = models.ForeignKey('disaster_table.summary', on_delete=models.CASCADE, related_name='details')
    Seq = models.IntegerField(default=None)
    Disaster_Subgroup = models.TextField()
    Disaster_Subtype = models.TextField()
    Disaster_Subsubtype = models.TextField()
    Region = models.TextField()
    Continent = models.TextField()
    Location = models.TextField()
    OFDA_Response = models.TextField()
    Appeal = models.IntegerField()
    Declaration = models.IntegerField()
    Local_Time = models.TextField()
    Start_Year = models.IntegerField()
    Start_Month = models.IntegerField()
    Start_Day = models.IntegerField()
    End_Year = models.IntegerField()
    End_Month = models.IntegerField()
    End_Day = models.IntegerField()
    Total_Deaths = models.IntegerField()
    insured_damages_usd = models.IntegerField()
    Total_Damages_usd = models.TextField()
    CPI = models.TextField()


    def __str__(self):
        return f'{self.Dis_ID}, {self.Seq}, {self.Disaster_Subgroup}, {self.Disaster_Subtype}, {self.Region}, {self.Continent},' \
               f' {self.Location}, {self.OFDA_Response},' \
               f' {self.Appeal}, {self.Declaration}, {self.Local_Time}, {self.Start_Year}, {self.Start_Month},{self.Start_Day},' \
               f'{self.End_Year},{self.End_Month},{self.End_Day},{self.Total_Deaths},{self.CPI},{self.Total_Damages_usd},'