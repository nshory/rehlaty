from django.forms import ModelForm
from .models import add_detail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

class adForm(ModelForm):

    class Meta:
        enctype = "multipart/form-data"
        model = add_detail

        fields = ['title','description','price','phone','username','city',"cate",'img1','img2','img3','img4','image']


