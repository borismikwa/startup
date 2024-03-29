from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from . import models
from .models import Contact
from django.db.models import Q
def navbar():
  ourservices = models.Service.objects.all().order_by('id')
  return ourservices

def index(request):
  short_des  = models.Service.objects.all().order_by('id')[:3]
  #ourservices = models.Service.objects.all()
  template = loader.get_template('index.html')
  #return HttpResponse(template.render({'services':navbar()}, request))
  return HttpResponse(template.render({'short_des': short_des}, request))


def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render({'services':navbar()}, request))


def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render({'services':navbar()}, request))

def testimonial(request):
  template = loader.get_template('testimonial.html')
  return HttpResponse(template.render())

def blog(request):
  template = loader.get_template('blog.html')
  return HttpResponse(template.render())

#def service(request):
  #template = loader.get_template('service.html')
  #return HttpResponse(template.render())

#def service_details(request,id):
  ##service = models.Service.get(id=id)
  #template = loader.get_template('service_details.html')
  #return HttpResponse(template.render(),{'service':service})
def demo(request):
  template = loader.get_template('demo.html')
  return HttpResponse(template.render({'services':navbar()}, request))

def program(request):
  template = loader.get_template('program.html')
  return HttpResponse(template.render())

def data_visualization(request):
  template = loader.get_template('data_visualization_demo.html')
  return HttpResponse(template.render({'services':navbar()},request))

def classification_demo(request):
  template = loader.get_template('classification_demo.html')
  return HttpResponse(template.render({'services':navbar()},request))

def regression_demo(request):
  template = loader.get_template('regression_demo.html')
  return HttpResponse(template.render({'services':navbar()},request))

def product(request):
  template = loader.get_template('product.html')
  return HttpResponse(template.render({'services':navbar()}, request))

def data_collection(request):
  template = loader.get_template('data_collection.html')
  return HttpResponse(template.render())


def data_analytics(request):
  template = loader.get_template('data_analytics.html')
  return HttpResponse(template.render())

  
def data_infrastructure(request):
  template = loader.get_template('data_infrastructure.html')
  return HttpResponse(template.render())

  
def machine_learning(request):
  template = loader.get_template('machine_learning.html')
  return HttpResponse(template.render())

def system_automization(request):
  template = loader.get_template('system_automization.html')
  return HttpResponse(template.render())


def process_optimization(request):
  template = loader.get_template('process_optimization.html')
  return HttpResponse(template.render())

  
def training_consultancy(request):
  template = loader.get_template('training_consultancy.html')
  return HttpResponse(template.render())

  
def video_surveillance(request):
  template = loader.get_template('video_surveillance.html')
  return HttpResponse(template.render())

  
def application_modernization(request):
  template = loader.get_template('application_modernization.html')
  return HttpResponse(template.render())

def software_dev(request):
  template = loader.get_template('software_dev.html')
  return HttpResponse(template.render())

#Get service details
def service_details(request,id):
  mydata = models.Service.objects.get(id=id)
  all_services = models.Service.objects.filter(~Q(id=id)).order_by('id')[:3]
  template = loader.get_template('service_details.html')
  context = {
    'myservice': mydata,'all_services':all_services,
  }
  return HttpResponse(template.render(context, request))


#pass all services to service page
def service(request):
  mydata1 = models.Service.objects.all().order_by('id')
  template = loader.get_template('service.html')
  context = {
    'myservices': mydata1,
  }
  return HttpResponse(template.render(context, request))

def store_contact(request):

  if request.method =="POST":
    #fetch data from the post
    data = request.POST
    print(data)
    email = data.get('email')
    fname = data.get('fname')
    lname = data.get('lname')
    subject = data.get('subject')
    message = data.get('message')
    print(email,fname,lname,subject,message)
    #create member object
    contact = Contact()
    contact.fname=fname
    contact.lname=lname
    contact.email=email
    contact.subject=subject
    contact.message =message
    next_link = request.POST.get('next', '/')
    try:
        contact.save()
        success = "Message sent with success."
        return HttpResponseRedirect(next_link,{'success':success})
    except Exception as e:
        print(e)
        failure = "505 An internal server error occurred!"
        return HttpResponseRedirect(next_link, {'failure':failure})
      


