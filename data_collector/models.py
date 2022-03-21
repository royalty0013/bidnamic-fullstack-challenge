from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
BIDDING_SETTING = (
    ("HIGH", "HIGH"),
    ("MEDIUM", "MEDIUM"),
    ("LOW","LOW"),
)

class ClientData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=500)
    surname = models.CharField(max_length=500)
    date_of_birth = models.DateField()
    company_name = models.CharField(max_length=250)
    address = models.TextField()
    telephone = models.CharField(max_length=20)
    bidding_settings = models.CharField(max_length=10, choices=BIDDING_SETTING)
    google_ads_account_id = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Client Data"

    def __str__(self):
        return f"{self.title} {self.first_name}"
    
