from django.db import models

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()

    class Meta:
        db_table = 'disaster_message'