from django.contrib import admin
from website.models import Service, Contact

# Register your models here.
class ServiceDetail(admin.ModelAdmin):
  list_display = ("service_name","currency","price", "date_included",)

class ContactAdmin(admin.ModelAdmin):
  list_display = ("fname","lname","email","subject", "message")


admin.site.register(Service,ServiceDetail)
admin.site.register(Contact,ContactAdmin)