from django import forms
from disaster_table.models import summary

class DataForm(forms.ModelForm):
    class Meta:
        model = summary
        fields = ('Dis_ID', 'Year', 'Disaster_Group', 'Disaster_Type', 'Country', 'ISO', 'Total_Affected', 'Total_Damages')

    # # Here is the data names' details
    # Dis_ID = models.IntegerField()
    # Year = models.IntegerField()
    # Disaster_Group = models.TextField()
    # Disaster_Type = models.TextField()
    # Country = models.TextField()
    # ISO = models.TextField()
    # Total_Affected = models.TextField()
    # Total_Damages = models.TextField()
    # is_delete = models.IntegerField(default=0) # This one will not be used here, since it has been used in disaster_list app.