from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify

# Create your models here.


#######CATEGORY######
class Category(models.Model):
    name= models.CharField(max_length=255)
    slug=models.SlugField(unique=True,blank=True,null=True)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Category ,self).save(*args , **kwargs)


    
    class Meta:       
        verbose_name='Category'
        verbose_name_plural ='Categories'

    

    def __str__(self):
        return "#ID %s"%(self.name)

####COLORVARIENT##########


class Colorvarient(models.Model):
    color_name = models.CharField(max_length=255,null=True,blank=True)
    price= models.IntegerField()
    
    class Meta:
        verbose_name= 'Colorvarient'
        verbose_name_plural='Colorvarients'
    
    def __str__(self):
        return self.color_name


##########SIZEVARIENT#########

class Sizevarient(models.Model):
    size = models.CharField(max_length=255,null=True,blank=True)
    price= models.IntegerField()
    
    class Meta:
        verbose_name= 'Sizevarient'
        verbose_name_plural='Sizevarients'
    
    def __str__(self):
        return self.size






#######PRODUCT#########

class Product(models.Model):
    product_name= models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True,null=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='products')
    description = models.TextField(max_length=300,null=True,blank=True)
    price = models.IntegerField()
    color_varient= models.ManyToManyField(Colorvarient,blank=True,null=True)
    size_varient = models.ManyToManyField(Sizevarient,blank=True,null=True)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.product_name)
        super(Product ,self).save(*args , **kwargs)

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'

    def __str__(self):
        return "#ID %s-%s"%(self.product_name,self.price)


   

##CUSTOMER###########

class Customer(models.Model):
    State = (
    ('AP','Andhra Pradesh'),
    ('AR','Arunachal Pradesh'),
    ('AS','Assam'),
    ('BR','Bihar'),
    ('CT','Chhattisgarh'),
    ('GA','Goa'),
    ('GJ','Gujarat'),
    ('HR','Haryana'),
    ('HP','Himachal Pradesh'),
    ('JK','Jammu and Kashmir'),
    ('JH','Jharkhand'),
    ('KA','Karnataka'),
    ('KL','Kerala'),
    ('MP','Madhya Pradesh'),
    ('MH','Maharashtra'),
    ('MN','Manipur'),
    ('ML','Meghalaya'),
    ('MZ','Mizoram'),
    ('NL','Nagaland'),
    ('OR','Odisha'),
    ('PB','Punjab'),
    ('RJ','Rajasthan'),
    ('SK','Sikkim'),
    ('TN','Tamil Nadu'),
    ('TG','Telangana'),
    ('TR','Tripura'),
    ('UT','Uttarakhand'),
    ('UP','Uttar Pradesh'),
    ('WB','West Bengal'),
    ('AN','Andaman and Nicobar Islands'),
    ('CH','Chandigarh'),
    ('DD','Daman and Diu'),
    ('DN','Dadra and Nagar Haveli'),
    ('DL','Delhi'),
    ('LD','Lakshadweep'),
    ('PY','Puducherry'),
) 

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = PhoneNumberField()
    city = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255,null=True, blank=True)
    state = models.CharField(max_length=255,choices=State)
  
    zip_code = models.IntegerField()
    address = models.CharField(max_length=255)


    def __str__(self):
        return "#ID %s-%s" %(self.user,self.first_name)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    


#####ADD TO CART###

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name='Cart'
        verbose_name_plural='Carts'

