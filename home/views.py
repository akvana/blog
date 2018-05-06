from django.shortcuts import render,HttpResponse
# Create your views here.
def homeview(request):
    if request.user.is_authenticated:
        context={
        'Durum':'Luuwa',


        }
    else:
        context={
        'Durum':'Misafir',


        }
    return render(request,'home.html',context)
