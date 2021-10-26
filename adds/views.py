from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
##@login_required(login_url='accounts:login')
from .form import adForm


def list(request):
    addd1 = add_detail.objects.all()
    addd2 = a8sam1.objects.all()
    context = {'ad': addd1 , 'tt': addd2}
    return render(request,'list.html',context)
    pass

def SectionsModel(request):
    addd2 = a8sam1.objects.all()
    context = {'tt': addd2}
    return render(request,'Sections.html',context)
    pass
def create_ad(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('accounts:login')
    form = adForm()
    user = request.user
    if request.method == 'POST':
        print('form-data :',request.POST)
        updated_request = request.POST.copy()
        updated_request.update({'username': user})
        form = adForm(updated_request, request.FILES)


       # print(form['username'].value(),'======',user)
        if form.is_valid():
            form.save()
            form.user = request.user
            print('ad created !!')

            return redirect('/')
        else:
            print('add not create')


    context = {'form': form}
    return render(request,'create_ad.html',context)
    pass
def detail(request,id):

    detail = add_detail.objects.get(id=id)

    context= {'ad_details': detail}
    return render(request,'dd_detail.html',context)

    pass



def sub_1(request,title):
    addd1 = add_detail.objects.filter(cate=title)
    addd2 = a8sam1.objects.all()
    context = {'ad': addd1, 'tt': addd2}
    return render(request, 'list.html', context)
    pass

def sub_land(request):
    addd1 = add_detail.objects.filter(cate='مخيمات')
    addd2 = a8sam1.objects.all()
    context = {'ad': addd1, 'tt': addd2}
    return render(request, 'list.html', context)
    pass
def myadds_view(request):
    addd1 = add_detail.objects.filter(cate='مخيمات')
    addd2 = a8sam1.objects.all()
    context = {'ad': addd1, 'tt': addd2}
    return render(request, 'list.html', context)
    pass
def update_add(request,id):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('accounts:login')
    add_21 = add_detail.objects.get(id=id)

    user = request.user
    form = adForm(instance=add_21)

    context = {'form': form}
    return render(request,'ad_update.html',context)
    pass
