from .models import Service

def service_nav(request):
    services = Service.objects.all()
    return {'services':services}
    
    