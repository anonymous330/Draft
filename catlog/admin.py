from django.contrib import admin
from .models import demand_draft,number_register,farmer_register
# Register your models here.
admin.site.register(demand_draft)
admin.site.register(number_register)
admin.site.register(farmer_register)
