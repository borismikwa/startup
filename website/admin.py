from django.contrib import admin
from website.models import Service

# Register your models here.
class ServiceDetail(admin.ModelAdmin):
  list_display = ("service_name","currency","price", "date_included",)

admin.site.register(Service,ServiceDetail)
