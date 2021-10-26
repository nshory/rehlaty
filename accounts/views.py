from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import CreateUserForm
from .models import *
import adds
from adds.models import *

from django.contrib import messages
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home (request):
    pass
def registerPage (request):
    if request.user.is_authenticated:
        return redirect('list:list')
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"تم انشاء حساب " + user)
            return redirect('accounts:login')
    context = {'form':form}
    return render(request,'register1.html',context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('list:list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('list:list')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login1.html', context)

def logoutUser(request):
	logout(request)
	return redirect('list:list')


def MyAccount (request):
    if request.user.is_authenticated:

        return render(request, 'myaccount.html')

def Myadds (request):
    if request.user.is_authenticated:
        addd1 = add_detail.objects.filter(username=request.user)
        addd2 = a8sam1.objects.all()
        context = {'ad': addd1, 'tt': addd2}
        return render(request, 'myadds.html',context)