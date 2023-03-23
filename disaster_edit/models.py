# from django.db import models
from django.db import models
from disaster_table.models import details
from disaster_table.models import summary
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

# Create your models here.

# def get_absolute_url(self):
#         return reverse('summary_edit', {'pk': self.pk})