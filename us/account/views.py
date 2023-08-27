from django.shortcuts import render,redirect
from .models import User
from .forms import PlayerSignUpForm,LoginForm,ClubRegistraionForm
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.models import auth
from .models import Pos_Choice, District_Choice
from datetime import date
# Create your views here.
def index(request):
    users=User.objects.all()
    usercout=users.count()
    players = User.objects.filter(is_player=True)
    player_count = players.count()
    club = User.objects.filter(is_club=True)
    club_count = club.count()
    return render(request,'index.html',
                    {"count":usercout,
                    "users":users,
                    'player':player_count,
                    'club':club_count,
                    })
def deleteUser(request,delete_id):
    delUser=User.objects.get(id=delete_id)
    delUser.delete()
    return redirect('/')
def updateStatus(request,update_id):
    updateUser=User.objects.get(id=update_id)
    if updateUser.is_active==True:
        updateUser.is_active=False
    else:
        updateUser.is_active=True
    updateUser.save()
    return redirect('/')
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
            password = form.cleaned_data.get('password')
            
            user = authenticate(email=email, password=password)
            print(user)
            
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/')
                else:
                    msg = "User is inactive"
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'
    
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
        img=request.FILES.get('img')
        print(img)
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        player_pos = request.POST.get('pos')
        district = request.POST.get('dist')
        locality = request.POST.get('loc')
        
        # Update the user's profile information
        user = request.user
        user.img=img
        user.first_name = first_name
        user.last_name = last_name
        user.email = user.email
        user.player_pos = player_pos
        user.district = district
        user.locality = locality
        user.save()

        
        return redirect('index')
    
    return render(request, 'edit-player-profile.html', {
        'user': request.user,
        'pos_choices': Pos_Choice,
        'district_choices': District_Choice,
    })



def selectType(request):
    return render(request,'selectType.html')
def player_selected(request):
    user=request.user
    user.is_player=1
    user.save()
    return redirect('CompleteProfile')
def club_selected(request):
    user=request.user
    user.is_club=1
    user.save()
    return redirect('CompleteClub')
def CompleteProfile(request):
    if request.method=='POST':
        img=request.FILES.get('img')
        dob=request.POST.get('birthdate')
        
        print(img,dob)
        user=request.user
        
        user.email=user.email
        user.img=img
        user.player_dob=dob
        user.save()
        return render(request,'index.html')
    return render(request,'CompleteProfile.html')
def CompleteClub(request):
    if request.method=='POST':
        img=request.FILES.get('img')
        club_name=request.POST.get('clubname')
        user=request.user
        user.email=user.email
        user.img=img
        user.club_name=club_name
        user.save()
        return render(request,'index.html')
    return render(request,'CompleteClub.html')
def editClub(request):
    if request.method == 'POST':
        img=request.FILES.get('img')
        club_name = request.POST.get('clubname')
        district = request.POST.get('dist')
        locality = request.POST.get('loc')

        # Update the user's profile information
        user = request.user
        user.img=img
        user.club_name = club_name
        user.email = user.email
        user.district = district
        user.locality = locality
        user.save()
        
        return redirect('index')
    
    return render(request, 'EditClub.html', {
        'user': request.user,
        'district_choices': District_Choice,
    })
def registerScout(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        district = request.POST.get('dist')
        locality = request.POST.get('loc')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('cpass')

        if User.objects.filter(email=email).exists():
            msg = 'Email already exists. Please use a different email address.'
            return render(request, 'RegisterScout.html', {
                'district_choices': District_Choice,
                'msg': msg,
            })
        elif password != confirm_password:
            msg = 'Passwords do not match.'
            return render(request, 'RegisterScout.html', {
                'district_choices': District_Choice,
                'msg': msg,
            })
        else:
            user = User(
                img=img,
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_scout=True,
                district=district,
                locality=locality,
            )
            user.set_password(password)
            user.save()
            return redirect('index')
    
    return render(request, 'RegisterScout.html', {
        'district_choices': District_Choice,
    })
# def google_login(request):
#     print("Entered")
#     return redirect('social:begin', 'google-oauth2')

# from social_django.models import UserSocialAuth
# def google_login(request):
#     return redirect('social:begin', 'google-oauth2')
# def google_callback(request):
#     print("Entered")
#     user = request.user
#     social = UserSocialAuth.objects.get(user=user, provider='google-oauth2')
#     # Do something with the social data, e.g., update user's email
#     return redirect('index')