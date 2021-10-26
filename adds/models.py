from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
city_names = (
    ('جدة','جدة'),
    ('الرياض', 'الرياض'),
)
bre_b7re = (
    ('بري','بري'),
    ('بحري', 'بحري'),
)
bre = (
    ('شاليهات','شاليهات'),
    ('مخيمات', 'مخيمات'),
    ('قوارب صيد', 'قوارب صيد'),
    ('قوارب نزهه', 'قوارب نزهه'),
    ('غوص', 'غوص'),
    ('العاب مائية', 'العاب مائية'),
    ('مخيمات شاطئية', 'مخيمات شاطئية'),
    ('دراجات', 'دراجات'),
    ('متاحف', 'متاحف'),
)
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "menu/%s.%s"%(instance.id,extension)
# Create your models here.
class a8sam1(models.Model):  # table
    title = models.CharField(max_length=15, choices=bre)
    namex =  models.CharField(max_length=100)  # column
    icon = models.ImageField(upload_to=image_upload)
    def __str__(self):
        return self.title
    pass

class add_detail(models.Model):  # table
    username = models.CharField(max_length=10,default='')
    title = models.CharField(max_length=50)  # column
    description = models.TextField(max_length=1000)
    price = models.CharField(max_length=5)
    phone = models.CharField(max_length=10,default='',validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')])
    image = models.ImageField(upload_to=image_upload)
    city = models.CharField(max_length=15, choices=city_names)
    cate = models.CharField(max_length=15, choices=bre)
    updated_at = models.DateTimeField(auto_now_add=True)
    img1 = models.ImageField(upload_to=image_upload,blank=True)
    img2 = models.ImageField(upload_to=image_upload,blank=True)
    img3 = models.ImageField(upload_to=image_upload,blank=True)
    img4 = models.ImageField(upload_to=image_upload,blank=True)
    def __str__(self):
        return self.title
    pass
