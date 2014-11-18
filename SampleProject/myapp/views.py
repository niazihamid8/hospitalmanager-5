from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/home.html')





def login(request):
    """ Default view for the root """
    if request.method=="GET":
      return render(request, 'user/login.html')
    else :
      return render(request, 'user/loginShow.html',{'Email': request.POST.get('email'),'PW': request.POST.get('pw')})
