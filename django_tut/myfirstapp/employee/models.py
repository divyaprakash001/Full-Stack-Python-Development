from django.db import models

# Create your models here.
class Employee(models.Model):
    name= models.CharField(max_length = 200)
    emp_id = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 12)
    address = models.CharField(max_length = 200)
    working  =models.BooleanField(default = True)
    department = models.CharField(max_length = 100)

    def __str__(self):
        return self.name 
    
# create another model for testimonial
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonial/")
    rating = models.IntegerField(max_length=2)

    def __str__(self):
        return self.name + " " + self.testimonial 


    
