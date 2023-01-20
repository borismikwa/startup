from .models import Service

def service_nav(request):
    services = Service.objects.all().order_by('id')
    return {'services':services}
    
    