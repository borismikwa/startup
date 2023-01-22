from django.db import models

# Create your models here.
import email
from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
import os
import sys
# Create your models here.
from django.urls import reverse
from tabnanny import verbose
from unicodedata import name
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


#imprting from a parent directory
#append parent directory to path
sys.path.append('../startup')

#import from the parent directory
from startup.settings import BASE_DIR

# PRIVATE_DIR = os.path.join(BASE_DIR, 'events')
# fs = FileSystemStorage(location=PRIVATE_DIR)

# Create your models here.
class Status(models.TextChoices):
    ACTIVE = 'Active',('Active'),
    INACTIVE = 'Suspended',('Suspended'),
    NOT_STARTED = 'not_started',('Not started'),
    PROGRESS = 'progressing',('In progress'),
    COMPLETED = 'completed',('Completed'),

class PaymentMode(models.TextChoices):
    TRANSFER = 'bank',('Bank transfer'),
    CHECK= 'check',('Check'),
    VISA = 'visa',('Debit/Credit Card'),
    CASH = 'cash',("Cash"),

class Client(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=50)
    dob   = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    email = models.EmailField(("User email"), max_length=254)
    address = models.CharField(max_length=255,null=False)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    is_active = models.CharField(choices=Status.choices,max_length = 20,
                                default=Status.ACTIVE
    )
    created = models.DateTimeField(auto_now_add=True) #date created
    updated = models.DateTimeField(auto_now=True) #date updated
    
    class Meta:
        verbose_name_plural ="Clients"
        ordering = (['-created']) # how the records are sorted when fetched
    def __str__(self): #string method for the class
        return self.fname + " " + self.lname #+ '\n Address: ' + self.address 
 
class Project(models.Model):
    name = models.CharField(max_length =40)
    description = models.CharField(max_length =255)
    budjet = models.CharField(max_length=50)
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE,related_name="Client")
    status = models.CharField(max_length=20,
        choices = Status.choices,
        default = Status.NOT_STARTED
    )# are you currently benefiting
    created = models.DateTimeField(auto_now_add=True) #date created
    updated = models.DateTimeField(auto_now=True) #date updated
    
    class Meta:
        verbose_name_plural ="Projects"
        ordering = (['-created']) # how the records are sorted when fetched
    def __str__(self): #string method for the class
        return self.name + " " + self.description 

class Payment(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE,related_name="Client_payment")
    amount = models.FloatField()
    motive= models.CharField(max_length=50) #title of the payment made, purchace, service, refund
    currency = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now=True) #date updated
    description = models.CharField(max_length=255,null=True)
    payment_status=  models.BooleanField(default=True) #paid or not
    total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    payment_mode = models.CharField(choices=PaymentMode.choices,
                            default=PaymentMode.VISA, max_length=50
    )

    def __str__(self) -> str:
        return self.amount +" " + self.motive + ': '\
             +self.description + self.payment_status

class Complaint(models.Model):
    email = models.EmailField(("User email"), max_length=254)
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=255,null=True)
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    
    class Meta:
        verbose_name_plural ="Complaints"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.email +" " + self.subject 

class Refund(models.Model):
    amount = models.CharField(max_length=150) 
    motive = models.CharField(max_length=150) #summary of why refunding
    currency = models.CharField(max_length=150) 
    description = models.CharField(max_length=250)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE,related_name="Client_refund")
    complaint_id = models.ForeignKey(Complaint, on_delete=models.CASCADE,related_name="Complaint") #we need to know what precedded before a refund
    refund_mode = models.CharField(choices=PaymentMode.choices,
                            default=PaymentMode.VISA, max_length=50
    )
    date_refunded = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    
    class Meta:
        verbose_name_plural ="Refunds"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.motive +" " + self.amount + " " + self.description


class Subscription(models.Model): #payments to consume a product or service
    amount = models.CharField(max_length=150) 
    status = models.BooleanField(default=True) #active or not
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    currency = models.CharField(max_length=150) 
    product_id = models.CharField(max_length=250) #actually product or service id
    category = models.CharField(max_length=100)#specify if a product or a service
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE,related_name="Client_subscription")
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    
    class Meta:
        verbose_name_plural ="Subscriptions"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.category +" " + self.amount + " from" + self.start_date\
            + " to" + self.end_date

class Service(models.Model): #services offered like the different programs
    service_name = models.CharField(max_length=150) 
    status = models.BooleanField(default=True) #active or not
    short_service = models.CharField(max_length=255) #Get short description of a service to be displayed on the home page and services page
    description = models.TextField() #Takes text that fully describes a service to be displayd on service detail page
    date_included = models.DateTimeField() #when did we start offering the service
    price = models.CharField(max_length=30)
    currency = models.CharField(max_length=150) #needed for conversion purposes
    on_promotion = models.BooleanField(default=False) # discounting?
    discount = models.CharField(max_length=20)#percentage set when on promotion
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    promotion_end_date = models.DateTimeField(null=True)
    avatar = models.ImageField(upload_to="img/services/") #adjust accordingly 
    
    class Meta:
        verbose_name_plural ="Services"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.service_name #+" " + self.price + " from" + self.description #displays only service name in admin dashbaord
            
        

class Newsletter(models.Model): #subscribers to newsletters
    email = models.EmailField(("User email"), max_length=254)
    status = models.BooleanField(default=True) #is the user active or not
    fname = models.CharField(max_length=55) #name of the subscripbet
    lname = models.CharField(max_length=60)
    date_unsubscribed = models.DateTimeField() #when did the person discontinue? This can help us determine the volume over a given time and find out if there is an issue arising
    phone = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    
    class Meta:
        verbose_name_plural ="Newsletters"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.fname +" " + self.lname + " " + self.email + " ,tel: "\
            + self.phone
    
class Promotion(models.Model): #products and services on promtion
    category = models.CharField(max_length=254) #product or service or program?
    status = models.BooleanField(default=True) #is the promo active or not
    start_date = models.DateTimeField() #when did promotion start
    end_date = models.DateTimeField() #when did promotion start
    discount = models.CharField(max_length=30)
    client_type = models.CharField(max_length=40)#is the promotion for all clients or a particular subset?
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    product_id = models.CharField(max_length=50)#should hold id for program, service, product

    class Meta:
        verbose_name_plural ="Promotions"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.category +" " + self.start_date+ " for" + self.client_type+ " ,discount "\
            + self.discount

class Contact (models.Model):
    email = models.EmailField(("User email"), max_length=254)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=60)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=255) #message from the visitor or client
    phone = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    
    class Meta:
        verbose_name_plural ="Contacts"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.fname +" " + self.lname + " " + self.email + " ,tel: "\
            + self.phone

       
class Program(models.Model):
    program_name = models.CharField(max_length=100)
    discipline = models.CharField(max_length=150) #the broader field to which it belongs in a taxonomy
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    link_to_content = models.CharField(max_length=255)#pointer to where training materials are located
    expert_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="User")#who is controlling the program content
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    
    class Meta:
        verbose_name_plural ="Programs"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.program_name +" " + self.title + " "
        
class Trainee(models.Model):
    email = models.EmailField(("User email"), max_length=254)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    status = models.CharField(max_length=30)#active trainee, unsubscribed, Interested
    class Meta:
        verbose_name_plural ="Trainees"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.fname +" " + self.lname + " " + self.email + " "
            

class Training(models.Model):
    name = models.CharField(max_length=50)
    vanue = models.CharField(max_length=60)
    subject = models.CharField(max_length=100)
    description= models.CharField(max_length=255) #message from the visitor or client
    trainee_id = models.ForeignKey(Trainee, on_delete=models.CASCADE,related_name="Expert")#who is controlling the program content
    start_date = models.DateTimeField(auto_now_add=True) # date created
    end_date = models.DateTimeField(auto_now=True)#date updated
    status = models.CharField(max_length=70)#completed,abandoned, certified,certificate not paid,
    cohort_code = models.CharField(max_length=150) #identify the trainee with a cohort
    condition = models.CharField(max_length=50)#Free, paid, scholarship training
    created = models.DateTimeField(auto_now_add=True) # date created
    updated = models.DateTimeField(auto_now=True)#date updated
    
    class Meta:
        verbose_name_plural ="Trainings"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.fname +" " + self.lname + " " + self.email + " "
            

class Events(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    event_type = models.CharField(max_length=200) #what kind of eent is it?
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural ="Events"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.name +" at" + self.venue + " on" + self.start_date + " "
            

class EventAttendance(models.Model):
    email = models.EmailField()
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural ="EventAttendances"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.fname +" " + self.lname + ", " + self.email + " "
            


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural ="Products"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.name +" " + self.price + ", " + self.currency + " "


class ProgramContent(models.Model):
    description = models.CharField(max_length=255)
    content_type = models.CharField(max_length=200) #video, text
    program_id = models.ForeignKey(Program,on_delete=models.CASCADE,related_name="Program")
    order = models.IntegerField() #this will be used to decide on how the content is arranged
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural ="ProgramContent"
        ordering = (['-created']) # how the records are sorted when fetched
  
    def __str__(self) -> str:
        return self.description  
 