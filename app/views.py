from django.shortcuts import render
from django.shortcuts import redirect
from app.models import car, bookvehicle
from django.http import HttpResponse
from app.form import RegistrationForm,EditProfileForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic
from .models import contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.form import contactForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def index(request):  
    Car = car.objects.all()  
    return render(request,"index.html",{'car':Car})  


#car list


# generic view to fetch the data then show in a list 
class IndexView(generic.ListView):
    
    # a name to refer to the object_list(to be used in the index.html)
    context_object_name = 'car_list'
    template_name = 'genericviews/index.html'
 
    def get_queryset(self):
        return car.objects.all()
 
 
# generic view to show the details of a particular object 
class DetailsView(generic.DetailView):
    model = car
    template_name = 'genericviews/detail.html'

#list view django
def vehiclelist(request):
    car_list = car.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(car_list, 20)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    return render(request, 'car_list.html', { 'cars': cars })


def carrent(request):  
    Car = car.objects.all()
    paginator = Paginator(Car, 120)
    return render(request,"rental.html",{'car':Car})  

def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  


def about(request):  
    return render(request,"about.html")  

def contact(request):  
    return render(request,"contact.html")  

def contactus(request):  
    stu = contactForm()  
    return render(request,"contactus.html",{'form':stu})  

def contactnow(request):
    cname=request.GET['']
    
    c=contact()
    c.name = vid
    c.email = uid
    r.save()
    html='''<meta http-equiv="refresh" content="3;URL='/viewbuys'" />  '''
    return HttpResponse(html+"added ({},{})".format(vid,uid))



def show(request):
	return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return redirect('/register/')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


def read_csv(request):
    from app import dbimport
    return HttpResponse("imported success"+str(dbimport))  

def dboperation(request):
    from app import dboperation
    return HttpResponse("DB run success"+str(dboperation))  



class CarDetailView(DetailView):

    model = car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


#@login_required
def book_now(request):
    vid=request.GET['vid']
    uid=request.user.username;
    r=bookvehicle()
    r.Vehicle_ID = vid
    r.used_email = uid
    r.save()
    html='''<meta http-equiv="refresh" content="3;URL='/viewbuys'" />  '''
    return HttpResponse(html+"added ({},{})".format(vid,uid))


@login_required
def viewbuys(request):
    uid=request.user.username
    buys=rent.objects.filter(used_email=uid)
    #return HttpResponse("<br>".join(["v={},u={}".format(b.Vehicle_ID,b.used_email) for b in buys]))
    atrs=['Vehicle_ID','Make','Short_Model','Long_Model','Trim','Derivative','Year_introduced','Year_discontinued','Currentl_Available']
    for b in buys:
        v=b.Vehicle_ID
        c=car.objects.get(Vehicle_ID=v)
        for a in atrs:setattr(b,a,getattr(c,a))
    args = {'bookings': buys}
    return render(request, 'view_booking.html', args)
    return HttpResponse(str(dir(b)))