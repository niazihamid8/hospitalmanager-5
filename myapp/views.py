from django.shortcuts import render
from myapp.models import user, Member
from myapp.models import RSS
import feedparser
import tkMessageBox
import ctypes
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    #return HttpResponse("<h1>Welcome To My Site</h1>")
    return render(request, 'homepage/home.html')


def List (request):
    if request.method == "POST":
        R = RSS(Link = request.POST.get('L1') , Agency = request.POST.get('L2') , Category = request.POST.get('L3'))
        R.save()
    RList = RSS.objects.all()
    return render(request , 'rss/list.html' , {'RSSList' : RList})

def rssdelete (request,link):
    k = RSS.objects.filter(Link = link)
    for i in k:
        i.delete()
    return HttpResponseRedirect("/list/")


def news(request):

    if request.method=="GET":
        return render(request, 'rss/news.html')
    else :
        feed = feedparser.parse("http://www.irna.ir/fa/rss.aspx?kind=-1")
        news = feed.entries
        return render(request,'rss/shownews.html',{'News' : news})


def users(request):

    return render(request, 'user/users.html', {'Users' : user.objects.all()})



def login(request):
    """ Default view for the root """
    if request.method=="GET":
      return render(request, 'user/login.html')
    else :
        import datetime

        now = datetime.datetime.now()
        if request.POST.get('chk') == None :
            Chk = "Unchecked"
        else :
            Chk = "Checked"

        user.objects.create( un = request.POST.get('email') , pw = request.POST.get('pw') )


        return render(request, 'user/loginShow.html',{'Now':now,'OR': request.POST.get('optionsRadios'),'Email': request.POST.get('email'),
                                                    'PW': request.POST.get('pw'),'Com': request.POST.get('comment'),
                                                    'Chk': Chk,'Slt': request.POST.get('slt')})
def default(request):
    return render(request, 'user/default.html')

def reg(request):
    return render(request, 'user/register.html')

def listusers(request):
     mlist = Member.objects.all()
     return render(request, 'user/users.html',{'reglist':mlist})

def submit(request):
    k=request.POST.get('newuser')
    email = request.POST.get('email')
    pass1= request.POST.get('pass')
    pass2 = request.POST.get('pass2')
    ac = request.POST.get('ac')
    Msg=[]
    if k == 'T':
        if pass1!=pass2:
            Msg.append("your pass not match")
        if len(pass1)==0:
            Msg.append("your pass is empty")
        if len(Msg)== 0:
            R = Member(email = request.POST.get('email') , pw = request.POST.get('pass') , ac = request.POST.get('ac'))
            R.save()
        # tkMessageBox.showinfo(title="Greetings", message=" sabtenam ba moaffaghiat anjam shod!")
            return render(request , 'user/success.html')
        else:
            return render(request,'user/register.html',{'ms':Msg })
    else:
        m = Member.objects.filter(email=request.POST.get('oldemail'))[0]
        m.email=email
        m.pw=pass1
        m.ac=ac
        m.save()
        return HttpResponseRedirect("/admin/users/")
def deluser(request,em):
    m = Member.objects.filter(email = em)
    for i in m:
       i.delete()
    return HttpResponseRedirect("/admin/users/")

def edituser(request,em):
    m = Member.objects.filter(email = em)
    return render(request,'user/register.html',{'Mem':m[0]})




