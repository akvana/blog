from django.shortcuts import render,redirect
from .forms import login_form,register_form
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def login_view(request):
    form=login_form(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data.get('user_name')
        password=form.cleaned_data.get('password')
        user=authenticate(username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Kullanıcı Adı veya Şifresi Yanlış.')
    return render(request ,'account/login_form.html',{'form':form})


def register_view(request):
    form=register_form(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username,password=password)
        login(request,new_user)
        return redirect('home')
    return render(request ,'account/register_form.html',{'form':form})
def logout_view(request):
    logout(request)
    return redirect('home')
