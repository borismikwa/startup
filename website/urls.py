from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #index/
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact'),
    path('blogs/', views.blog, name='blog'),
    path('testimonials/', views.testimonial, name='testimonial'),
    path('services/', views.service, name='service'),
    path('demos/', views.demo, name='demo'),
    path('programs/', views.program, name='program'),

    path('demo/data/visualization/', views.data_visualization, name='data_visualization'),
    path('demo/model/classification', views.classification_demo, name='classification_demo'),
    path('demo/model/regression',views.regression_demo,name='regression_demo'),
    path('products/', views.product, name='product'),
    
]