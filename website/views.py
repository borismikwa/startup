from django.http import HttpResponse
from django.template import loader
from . import models

def index(request):
  #
  services  = models.Service.objects.all()[3:]
  template = loader.get_template('index.html')
  return HttpResponse(template.render(),{'services',services})


def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())


def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def testimonial(request):
  template = loader.get_template('testimonial.html')
  return HttpResponse(template.render())

def blog(request):
  template = loader.get_template('blog.html')
  return HttpResponse(template.render())

def service(request):
  template = loader.get_template('service.html')
  return HttpResponse(template.render())

def service_details(request,id):
  service = models.Service.get(id=id)
  template = loader.get_template('service_details.html')
  return HttpResponse(template.render(),{'service':service})
def demo(request):
  template = loader.get_template('demo.html')
  return HttpResponse(template.render())

def program(request):
  template = loader.get_template('program.html')
  return HttpResponse(template.render())

def data_visualization(request):
  template = loader.get_template('data_visualization_demo.html')
  return HttpResponse(template.render())

def classification_demo(request):
  template = loader.get_template('classification_demo.html')
  return HttpResponse(template.render())

def regression_demo(request):
  template = loader.get_template('regression_demo.html')
  return HttpResponse(template.render())

def product(request):
  template = loader.get_template('product.html')
  return HttpResponse(template.render())

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


