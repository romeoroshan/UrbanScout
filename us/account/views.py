from django.shortcuts import render,redirect
from .models import User
from .forms import PlayerSignUpForm,LoginForm,ClubRegistraionForm
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.models import auth
from .models import Pos_Choice, District_Choice
from datetime import date
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def registerPlayer(request):
    msg = None
    if request.method == 'POST':
        player_form = PlayerSignUpForm(request.POST,request.FILES)
        if player_form.is_valid():
            email = player_form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                msg = 'Email already exists. Please use a different email address.'
            else:
                user = player_form.save(commit=False) 
                user.is_player = True 
                user.save()  
                msg = 'User created'
                return redirect('login')
        else:
            msg = 'Form is not valid'
    else:
        player_form = PlayerSignUpForm()
    return render(request, 'register.html', {'playerForm': player_form, 'msg': msg})
def registerClub(request):
    msg = None
    if request.method == 'POST':
        club_form = ClubRegistraionForm(request.POST,request.FILES)
        if club_form.is_valid():
            email = club_form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                msg = 'Email already exists. Please use a different email address.'
            else:
                user = club_form.save(commit=False) 
                user.is_club = True 
                user.save()  
                msg = 'User created'
                return redirect('login')
        else:
            msg = 'Form is not valid'
    else:
        club_form = ClubRegistraionForm()
    return render(request, 'reg-club.html', {'playerForm': club_form, 'msg': msg})
def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            print(email)
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                print("entered")
                auth_login(request, user)
                return redirect('index')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})
def playerHome(request):
    return render(request,'player-home.html')
def clubHome(request):
    return render(request,'club-home.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
def playerClub(request):
    clubs=User.objects.filter(is_club=1).values()
    return render(request,'player-club.html',{'clubs':clubs})
def editPlayerProfile(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        player_pos = request.POST.get('pos')
        district = request.POST.get('dist')
        locality = request.POST.get('loc')

        # Update the user's profile information
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.player_pos = player_pos
        user.district = district
        user.locality = locality
        user.save()

        
        return redirect('player-home')
    
    return render(request, 'edit-player-profile.html', {
        'user': request.user,
        'pos_choices': Pos_Choice,
        'district_choices': District_Choice,
    })