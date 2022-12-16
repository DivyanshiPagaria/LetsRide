from django.db import models
from django.utils.timezone import now 
from django.contrib.auth.models import User

# Create your models here.
class requester(models.Model):
    ASSET_TYPE = (
    ('BAG', 'travel_bag'),
    ('PKG', 'package'),
    ('LPT', 'laptop')
    )

    ASSET_SENSITIVITY = (
        ('HIGH', 'highly_sensitive'),
        ('NRML', 'sensitive'),
        ('LOW', 'normal')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_from = models.CharField(max_length = 20, null = False)
    location_to = models.CharField(max_length = 20, null = False)
    quantity = models.IntegerField(default = 1, null = False)
    date = models.DateTimeField(default=now)
    asset_type = models.CharField(max_length=3, choices=ASSET_TYPE, null = False)
    asset_sensitivity = models.CharField(max_length=4, choices=ASSET_SENSITIVITY, null = False)
    receiver = models.CharField(max_length=100, null = False)

class rider(models.Model):
    TRAVEL_MEDIUM = (
    ('BUS', 'bus'),
    ('CAR', 'car'),
    ('TRN', 'train')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_from = models.CharField(max_length = 20, null = False)
    location_to = models.CharField(max_length = 20, null = False)
    quantity = models.IntegerField(default = 1, null = False)
    date = models.DateTimeField(default=now)
    travel_medium = models.CharField(max_length=3, choices=TRAVEL_MEDIUM, null = False)