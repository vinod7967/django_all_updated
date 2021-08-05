from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from .forms import SignupForm
from django.shortcuts import render, redirect
from .forms import Ticket_forms
from .models import TicketBookModel
from datetime import datetime,timedelta
# Create your views here.

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Succesfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Succesfully !!!')
                    return HttpResponseRedirect('/show')
        else:
            fm = AuthenticationForm()
        return render(request, 'signup.html', {'form': fm})
    else:
        return HttpResponseRedirect('/show')


def first_page(request):
        return render(request,'first_page.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


# Create your views here.
def show(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Ticket_forms(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                movie_name = form.cleaned_data['movie_name']
                email = form.cleaned_data['email']
                ticket_no = form.cleaned_data['ticket_no']
                no_of_tickets = form.cleaned_data['no_of_tickets']
                request.session['name'] = name
                request.session['movie_name'] = movie_name
                request.session.set_expiry(600)
                response = render(request, 'show.html')
                # response.set_cookie('movie_name', movie_name, expires=datetime.utcnow()+timedelta(days=2))
                response.set_signed_cookie('movie_name', movie_name, salt='movie_name', expires=datetime.utcnow()+timedelta(days=2))
                reg_data = TicketBookModel(name=name,movie_name=movie_name,email=email,ticket_no=ticket_no,no_of_tickets=no_of_tickets)
                reg_data.save()
                form = Ticket_forms()
                return response
        else:
            form = Ticket_forms()
        booking = TicketBookModel.objects.all()
        total = 100
        instance = TicketBookModel.objects.values_list('no_of_tickets')
        description = sum(map(sum, instance))
        available = total - description
        return render(request, 'show.html', {'form': form, 'book':booking,'total':total, 'booked':description, 'remain':available})
    else:
        return HttpResponseRedirect('/login')

def update_ticket(request, id):
    ticket = TicketBookModel.objects.get(pk=id)  
    form = Ticket_forms(request.POST, instance = ticket)
    if form.is_valid():  
        form.save()  
        return redirect("/show")
    else:
        pi = TicketBookModel.objects.get(pk=id)
        form = Ticket_forms(instance=pi)
    return render(request, 'show.html', {'form': form}) 

def destroy(request, id):  
    ticket = TicketBookModel.objects.get(id=id)  
    ticket.delete()  
    return redirect("/show") 

def getsession(request):
    name = request.session['name']
    movie_name = request.session['movie_name']
    # name = request.session.get('name', default = 'Guest')
    # keys = request.session.keys()
    # key = request.session.items()
    # age = request.session.setdefault('age', '36')
    request.session.modified = True
    context = {'name': name, 'movie_name': movie_name}
    return render(request, 'getsession.html',context )

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'delsession.html')

def getcookie(request):
    # name = request.COOKIES.get('name','Guest')
    movie_name = request.get_signed_cookie('movie_name', default = 'Guest',salt = 'movie_name')
    # name = request.COOKIES['name']
    return render(request, 'getcookie.html', {'movie_name':movie_name})

def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('movie_name')
    return response