from django.db import models

class DisasterUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_password = models.TextField()
    user_name = models.TextField()
    user_level = models.IntegerField()
    login_status = models.TextField()
    is_banned = models.IntegerField()
    is_delete = models.IntegerField()
    is_approved = models.IntegerField()


    class Meta:
        db_table = 'disaster_user'

    def __str__(self):
        return f"User ID: {self.user_id}, User Name: {self.user_name}"