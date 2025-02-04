from django.contrib import admin
from .models import Flight, Category, Belt, Services, PayloadCompartment
# Register your models here.



admin.site.register(Flight)
admin.site.register(Category)

admin.site.register(Belt)
admin.site.register(Services)
admin.site.register(PayloadCompartment)