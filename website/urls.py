from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'), #index/
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact'),
    path('blogs/', views.blog, name='blog'),
    path('testimonials/', views.testimonial, name='testimonial'),
    path('services/', views.service, name='service'),
    path('services/<int:id>',views.service_details,name='service_details'),
    path('demos/', views.demo, name='demo'),
    path('programs/', views.program, name='program'),

    path('demo/data/visualization/', views.data_visualization, name='data_visualization'),
    path('demo/model/classification', views.classification_demo, name='classification_demo'),
    path('demo/model/regression',views.regression_demo,name='regression_demo'),
    path('products/', views.product, name='product'),
    path('services/collection/',views.data_collection,name='data_collection'),
    path('services/analytics/',views.data_analytics, name='data_analytics'),
    path('services/data_infrastructure/',views.data_infrastructure, name='data_infrastructure'),
    path('services/machine_learning/',views.machine_learning,name='machine_learning'),
    path('services/system_automatization/',views.system_automization,name='system_automization'),
    path('services/process_optimization/',views.process_optimization,name='process_optimization'),
    path('services/training_consultancy/', views.training_consultancy,name='training_consultancy'),
    path('services/video_surveillance/',views.video_surveillance,name='video_surveillance'),
    path('services/application_modernization/',views.application_modernization,name='application_modernization'),
    path('services/software_dev/',views.software_dev,name='software_dev'),
    path('service_details/<int:id>/',views.service_details,name='service_details'),

]

