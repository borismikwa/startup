from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

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
