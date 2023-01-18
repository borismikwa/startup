from .models import Service

def service_nav(request):
    services = Service.objects.all()
    print(services)
    return {'services':services}
    
    