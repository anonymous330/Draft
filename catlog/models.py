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

class number_register(models.Model):
    mob_number=models.IntegerField(primary_key=True,null=False)
    place=models.CharField(max_length=50)
    status=models.CharField(max_length=50)


    def __str__(self):
        return f"{self.mob_number}"


class farmer_register(models.Model):
    mobile_number=models.ForeignKey(number_register,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    yojna=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    place=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.mobile_number}"
