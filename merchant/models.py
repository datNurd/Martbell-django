from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MerchantProfile(models.Model):
    user = models.OneToOneField(User)
    shop_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user.Username
