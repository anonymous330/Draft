from django.db import models
from datetime import datetime,date
from rest_framework import serializers
# Create your models here.

class demand_draft(models.Model):
    dd_no=models.IntegerField(primary_key=True)
    dd_name=models.CharField(max_length=20)
    dd_bank=models.CharField(max_length=20)
    dd_amount=models.IntegerField()
    dd_date=models.DateTimeField()
    dd_image=models.ImageField(null=True,blank=True,upload_to="images/")

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


class customer_detail(models.Model):
    custmer_name=models.CharField(max_length=20)
    customer_dob=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    account_kit=models.IntegerField()
    atm_kit=models.IntegerField()
    adhaar_no=models.IntegerField()
    mobile_no=models.IntegerField()
    customer_father=models.CharField(max_length=20)
    customer_mother=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.custmer_name} {self.customer_dob}"

class kit_numbers(models.Model):
    welcome_kit_number=models.IntegerField(primary_key=True)
    customer_id=models.IntegerField()
    customer_account=models.IntegerField()


    def __str__(self):
        return f"{self.customer_id} {self.customer_account}"


class kit_numbersSerializer(serializers.Serializer):
        welcome_kit_number=serializers.IntegerField()
        customer_id=serializers.IntegerField()
        customer_account=serializers.IntegerField()


class debitCard(models.Model):
    debit_card_kit=models.IntegerField(primary_key=True)
    debit_card_number=models.IntegerField()


    def __str__(self):
        return f"{self.debit_card_kit} {self.debit_card_number}"


class debitCardSerializer(serializers.Serializer):
    debit_card_kit=serializers.IntegerField()
    debit_card_number=serializers.IntegerField()
