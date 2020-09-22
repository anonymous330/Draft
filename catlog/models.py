from django.db import models

# Create your models here.

class demand_draft(models.Model):
    dd_no=models.IntegerField(primary_key=True)
    dd_name=models.CharField(max_length=20)
    dd_bank=models.CharField(max_length=20)
    dd_amount=models.IntegerField()
    dd_date=models.DateTimeField()

    def __str__(self):
        return f"{self.dd_no} {self.dd_name}"
