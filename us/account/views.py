from django.shortcuts import render,redirect
from .models import User,InterestedClubs,ShortlistedPlayers,ShortlistedScouts,ShortlistedClubScouts,PostFeed,PostImageFeed,PostVideoFeed,Contract,NewFeeds,likes,following,Notification
from .forms import PlayerSignUpForm,LoginForm,ClubRegistraionForm
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.models import auth
from .models import Pos_Choice, District_Choice,Ability_Choice
from datetime import date
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    followingg=following.objects.filter(following_id=request.user.id).count()
    followers=following.objects.filter(followed_id=request.user.id).count()
    notifications=Notification.objects.filter(followed_id=request.user.id).count()
    print(followers)
    print(followingg)
    users=User.objects.all()
    usercout=users.count()
    players = User.objects.filter(is_player=True)
    player_count = players.count()
    club = User.objects.filter(is_club=True)
    club_count = club.count()
    scout=User.objects.filter(is_scout=True)
    ability_range = range(0, 5)
    user=request.user
    user_id=user.id
    newfeeds=NewFeeds.objects.filter(user_id=user_id).order_by('-id')
    feeds=PostFeed.objects.filter(user_id=user_id)
    post_count=newfeeds.count()
    imgfeeds=PostImageFeed.objects.filter(user_id=user_id)
    videofeeds=PostVideoFeed.objects.filter(user_id=user_id)
    print(ability_range)
    if request.method=='POST':
        feed=request.POST.get('feed')
        print(feed)
        print
        post=NewFeeds(
            feed=feed,
            user_id=user_id,
            datetime=timezone.now()
        )
        post.save()
    return render(request,'index.html',
                    {"count":usercout,
                    "users":users,
                    'playerdata':players,
                    'player':player_count,
                    'club':club_count,
                    'clubdata':club,
                    'scout':scout,
                    'abilityRange':ability_range,
                    'userfeeds':feeds,
                    'userimgfeeds':imgfeeds,
                    'uservideofeeds':videofeeds,
                    'newfeeds':newfeeds,
                    'following':followingg,
                    'followers':followers,
                    'post_count':post_count,
                    'notification':notifications
                    })
def deleteUser(request,delete_id):
    delUser=User.objects.get(id=delete_id)
    delUser.delete()
    return redirect('index')
def updateStatus(request,update_id):
    updateUser=User.objects.get(id=update_id)
    if updateUser.is_active==True:
        updateUser.is_active=False
    else:
        updateUser.is_active=True
    updateUser.save()
    return redirect('/')

from django.core.mail import EmailMessage
from django.conf import settings
def sendEmail(user_email):
    print(user_email)
    email_subject = 'Welcome to UrbanScout'
    email_body = 'Dear User, We are thrilled to welcome you to Urban! Thank you for choosing to be a part of our community. Your registration with us marks the beginning of an exciting journey. With your account, you now have access to a wide range of features and services that our website offers. Whether you are here to connect, explore, or achieve specific goals, we are here to provide you with a seamless and enriching experience. Feel free to explore our platform and take advantage of all the resources available to you. We are committed to ensuring that your time here is both enjoyable and valuable.If you have any questions, feedback, or need assistance, do not hesitate to reach out to our support team. We are here to help you every step of the way. Once again, thank you for choosing UrbanScout. We are excited to have you on board and look forward to seeing you thrive within our community.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    email = EmailMessage(email_subject, email_body, from_email, recipient_list)
    print(email)
    email.send()
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
                sendEmail(email)
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
                sendEmail(email)
                msg = 'User created'
                return redirect('login')
        else:
            msg = 'Form is not valid'
    else:
        club_form = ClubRegistraionForm()
    return render(request, 'reg-club.html', {'playerForm': club_form, 'msg': msg})
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
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
@login_required(login_url='http://127.0.0.1:8000/login/')
def playerHome(request,user_id):
    followingg=following.objects.filter(following_id=user_id).count()
    followers=following.objects.filter(followed_id=user_id).count()
    players = User.objects.filter(is_player=True)
    scout=User.objects.filter(is_scout=True)
    clubs=User.objects.filter(is_club=True)
    ability_range = range(0, 5)
    feeds=NewFeeds.objects.filter(user_id=user_id).order_by('-id')
    post_count=feeds.count()
    ability_range = range(0, 5)
    player=User.objects.filter(id=user_id)
    return render(request,'player-home.html',{'player':player,'abilityRange':ability_range,'clubdata':clubs,'playerdata':players,'scout':scout,'feeds':feeds,'followers':followers,'following':followingg,'post_count':post_count})

@login_required(login_url='http://127.0.0.1:8000/login/')
def clubHome(request,user_id):
    followingg=following.objects.filter(following_id=user_id).count()
    followers=following.objects.filter(followed_id=user_id).count()
    players=User.objects.filter(is_player=True)
    clubs = User.objects.filter(is_club=True)
    scout=User.objects.filter(is_scout=True)
    ability_range = range(0, 5)
    feeds=NewFeeds.objects.filter(user_id=user_id).order_by('-id')
    post_count=feeds.count()
    ability_range = range(0, 5)
    club=User.objects.filter(id=user_id)
    return render(request,'ClubHome.html',{'club':club,'abilityRange':ability_range,'playerdata':players,'clubdata':clubs,'scout':scout,'feeds':feeds,'followers':followers,'following':followingg,'post_count':post_count})
@login_required(login_url='http://127.0.0.1:8000/login/')
def scoutHome(request,user_id):
    followingg=following.objects.filter(following_id=user_id).count()
    followers=following.objects.filter(followed_id=user_id).count()
    clubs = User.objects.filter(is_club=True)
    player=User.objects.filter(is_player=True)
    scouts=User.objects.filter(is_scout=True)
    ability_range = range(0, 5)
    feeds=NewFeeds.objects.filter(user_id=user_id).order_by('-id')
    post_count=feeds.count()
    ability_range = range(0, 5)
    scout=User.objects.filter(id=user_id)
    print(scouts)
    return render(request,'ScoutHome.html',{'scouts':scouts, 'scout':scout,'abilityRange':ability_range,'clubdata':clubs,'player':player,'feeds':feeds,'followers':followers,'following':followingg,'post_count':post_count})
def logout(request):
    auth.logout(request)
    return redirect('login')
@login_required(login_url='http://127.0.0.1:8000/login/')
def playerClub(request):
    user = request.user
    interested_clubs = InterestedClubs.objects.filter(player_id=user.id).values_list('club_id', flat=True)
    all_cont=Contract.objects.filter(player_id=user.id).values_list('club_id',flat=True)
    shortlisted_Players=ShortlistedPlayers.objects.filter(player_id=user.id).values_list('club_id',flat=True)
    cont_is_active=Contract.objects.filter(player=user.id, player_negotiating=True,contractAccepted=False).values_list('club_id', flat=True)
    cont_is_accepted=Contract.objects.filter(player=user.id,contractAccepted=True).values_list('club_id', flat=True)

    cont_is_not_active=Contract.objects.filter(player_id=user.id, player_negotiating=False,contractAccepted=False).values_list('club_id', flat=True)
    non_contract_clubs=[]
    contract_clubs=[]
    cont_accepted=[]

    all_clubs = User.objects.filter(is_club=True).values()

    interested_clubs_list = []
    not_interested_clubs_list = []
    shortlisted_Players_list=[]

    for club in all_clubs:
        club_id = club['id']
        club_data = {
            'id': club['id'],
            'club_name': club['club_name'],
            'img':club['img'],
            'district':club['district'],
            'locality':club['locality']
            # Add other fields you want to include here
        }
        
        if club_id in interested_clubs and club_id not in all_cont:
            interested_clubs_list.append(club_data)
        elif club_id in shortlisted_Players and club_id not in all_cont:
            shortlisted_Players_list.append(club_data)
        else:
            if club_id not in all_cont:
                not_interested_clubs_list.append(club_data)
        if club_id in cont_is_active:
            contract_clubs.append(club_data)
            
        elif club_id in cont_is_not_active:
            non_contract_clubs.append(club_data)
        if club_id in cont_is_accepted:
            cont_accepted.append(club_data)
    print(contract_clubs)
    print(non_contract_clubs)
    return render(request, 'player-club.html', {
        'shortlisted_players':shortlisted_Players_list,
        'interested_clubs': interested_clubs_list,
        'not_interested_clubs': not_interested_clubs_list,
        'contractedClubs':contract_clubs,
        'nonContractedClubs':non_contract_clubs,
        'contractAccepted':cont_accepted,
    })
@login_required(login_url='http://127.0.0.1:8000/login/')
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
        if img is None:
            img=user.img
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
        if img is None:
            img=user.img
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
@login_required(login_url='http://127.0.0.1:8000/login/')
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
            sendEmail(email)
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


#email
def showInterest(request,club_id):
    user=request.user
    data=InterestedClubs(
        club_id=club_id,
        player_id=user.id
    )
    data.save()
    return redirect('player-club')

@login_required(login_url='http://127.0.0.1:8000/login/')
def clubPlayer(request):
    user = request.user
    interested_players = InterestedClubs.objects.filter(club_id=user.id).values_list('player_id', flat=True)
    shortlisted_Players=ShortlistedPlayers.objects.filter(club_id=user.id).values_list('player_id',flat=True)
    all_players = User.objects.filter(is_player=True).values()
    all_cont=Contract.objects.filter(club_id=user.id).values_list('player_id',flat=True)
    cont_is_accepted=Contract.objects.filter(club_id=user.id,contractAccepted=True).values_list('player_id', flat=True)
    cont_accepted=[]


    cont_is_active=Contract.objects.filter(club_id=user.id, player_negotiating=True,contractAccepted=False).values_list('player_id', flat=True)
    cont_is_not_active=Contract.objects.filter(club_id=user.id, player_negotiating=False,contractAccepted=False).values_list('player_id', flat=True)
    print(cont_is_active)
    contract_players=[]
    non_contract_players=[]
    interested_players_list = []
    not_interested_players_list = []
    ability_range = range(0, 5)
    shortlisted_Players_list=[]
    for player in all_players:
        player_id = player['id']
        player_data = {
            'id': player['id'],
            'first_name': player['first_name'],
            'last_name':player['last_name'],
            'img':player['img'],
            'district':player['district'],
            'locality':player['locality'],
            'scouted_by':player['scouted_by'],
            'player_ability':player['player_ability'],
            'player_potential':player['player_potential'],
            # Add other fields you want to include here
        }
        
        if player_id in interested_players and player_id not in all_cont:
            interested_players_list.append(player_data)
        elif player_id in shortlisted_Players and player_id not in all_cont:
            shortlisted_Players_list.append(player_data)
        else:
            if player_id not in all_cont:
                not_interested_players_list.append(player_data)
        if player_id in cont_is_active:
            contract_players.append(player_data)
        elif player_id in cont_is_not_active:
            non_contract_players.append(player_data)
        if player_id in cont_is_accepted:
            cont_accepted.append(player_data)
    return render(request, 'club-player.html', {
        'shortlisted_players':shortlisted_Players_list,
        'interested_players': interested_players_list,
        'not_interested_players': not_interested_players_list,
        'abilityRange':ability_range,
        'contractedPlayers':contract_players,
        'nonContractedPlayers':non_contract_players,
        'contractAccepted':cont_accepted,

    })
def shortlistPlayer(request,player_id):
    user=request.user
    data=ShortlistedPlayers(
        player_id=player_id,
        club_id=user.id
    )
    data.save()
    return redirect('ClubPlayer')
@login_required(login_url='http://127.0.0.1:8000/login/')
def playerScout(request):
    user = request.user
    shortlisted_scouts = ShortlistedScouts.objects.filter(player_id=user.id).values_list('scout_id', flat=True)
    all_scouts = User.objects.filter(is_scout=True).values()
    shortlisted_scout_list = []
    not_shortlisted_scout_list = []
    for scout in all_scouts:
        scout_id = scout['id']
        player_data = {
            'id': scout['id'],
            'first_name': scout['first_name'],
            'last_name':scout['last_name'],
            'img':scout['img'],
            'district':scout['district'],
            'locality':scout['locality'],
            # Add other fields you want to include here
        }
        
        if scout_id in shortlisted_scouts:
            shortlisted_scout_list.append(player_data)
        else:
            not_shortlisted_scout_list.append(player_data)
    print(shortlisted_scout_list)
    return render(request, 'player-scout.html', {
        'shortlisted_scout': shortlisted_scout_list,
        'not_shortlisted_scout': not_shortlisted_scout_list,
    })
def shortlistScout(request,scout_id):
    user=request.user
    data=ShortlistedScouts(
        scout_id=scout_id,
        player_id=user.id
    )
    data.save()
    return redirect('PlayerScout')
@login_required(login_url='http://127.0.0.1:8000/login/')
def scoutPlayer(request):
    user = request.user
    interested_players = ShortlistedScouts.objects.filter(scout_id=user.id).values_list('player_id', flat=True)
    all_players = User.objects.filter(is_player=True).values()
    fullname = "{} {}".format(user.first_name, user.last_name)
    interested_players_list = []
    ability_range = range(0, 5)
    not_interested_players_list = []
    for player in all_players:
        player_id = player['id']
        player_data = {
            'id': player['id'],
            'first_name': player['first_name'],
            'last_name':player['last_name'],
            'img':player['img'],
            'district':player['district'],
            'locality':player['locality'],
            'scouted_by':player['scouted_by'],
            'player_ability':player['player_ability'],
            'player_potential':player['player_potential'],
            
            # Add other fields you want to include here
        }
        
        if player_id in interested_players:
            interested_players_list.append(player_data)
        else:
            not_interested_players_list.append(player_data)
    print(interested_players_list)
    return render(request, 'ScoutPlayer.html', {
        'fullname':fullname,
        'interested_players': interested_players_list,
        'not_interested_players': not_interested_players_list,
        'abilityRange':ability_range,
    })
@login_required(login_url='http://127.0.0.1:8000/login/')
def clubScout(request):
    user = request.user
    shortlisted_scouts = ShortlistedClubScouts.objects.filter(club_id=user.id).values_list('scout_id', flat=True)
    all_scouts = User.objects.filter(is_scout=True).values()
    shortlisted_scout_list = []
    not_shortlisted_scout_list = []
    for scout in all_scouts:
        scout_id = scout['id']
        player_data = {
            'id': scout['id'],
            'first_name': scout['first_name'],
            'last_name':scout['last_name'],
            'img':scout['img'],
            'district':scout['district'],
            'locality':scout['locality']
            # Add other fields you want to include here
        }
        
        if scout_id in shortlisted_scouts:
            shortlisted_scout_list.append(player_data)
        else:
            not_shortlisted_scout_list.append(player_data)

    return render(request, 'ClubScout.html', {
        'shortlisted_scout': shortlisted_scout_list,
        'not_shortlisted_scout': not_shortlisted_scout_list,
    })
def shortlistClubScout(request,scout_id):
    user=request.user
    data=ShortlistedClubScouts(
        scout_id=scout_id,
        club_id=user.id
    )
    data.save()
    return redirect('ClubScout')
@login_required(login_url='http://127.0.0.1:8000/login/')
def scoutClub(request):
    user = request.user
    interested_Clubs = ShortlistedClubScouts.objects.filter(scout_id=user.id).values_list('club_id', flat=True)
    all_clubs = User.objects.filter(is_club=True).values()
    fullname = "{} {}".format(user.first_name, user.last_name)
    print(fullname)
    ability_range = range(0, 5)
    interested_Clubs_list = []
    not_interested_Clubs_list = []
    for Club in all_clubs:
        Club_id = Club['id']
        Club_data = {
            'id': Club['id'],
            'club_name': Club['club_name'],
            'img':Club['img'],
            'district':Club['district'],
            'locality':Club['locality'],
            'club_reputation':Club['club_reputation'],
            'scouted_by':Club['scouted_by'],
            # Add other fields you want to include here
        }
        
        if Club_id in interested_Clubs:
            interested_Clubs_list.append(Club_data)
        else:
            not_interested_Clubs_list.append(Club_data)
    print(interested_Clubs_list)
    return render(request, 'ScoutClub.html', {
        'fullname':fullname,
        'abilityRange':ability_range,
        'interested_Clubs': interested_Clubs_list,
        'not_interested_Clubs': not_interested_Clubs_list,
    })
def acceptRequest(request,req_id):
    user=request.user
    print(user.id,req_id)
    data=ShortlistedPlayers(
        club_id=user.id,
        player_id=req_id,
    )

    data.save()
    club_id=user.id
    player_id=req_id
    deleteByRequest(player_id,club_id)
    return redirect('ClubPlayer')
def deleteByRequest(player_id,club_id):
    delete_data=InterestedClubs.objects.filter(player_id=player_id,club_id=club_id)
    delete_data.delete()
    return redirect('ClubPlayer')
from joblib import load
def scoutPlayerEdit(request, update_id):
    potential_model=load('./player model/model.joblib')
    ability_model=load('./player model/ability_model.joblib')
    print(potential_model)
    updateUser = User.objects.get(id=update_id)
    user = request.user
    username = "{} {}".format(user.first_name, user.last_name)
    print(username)
    
    if request.method == 'POST':
        pace = request.POST.get('pace')
        shooting = request.POST.get('shooting')
        passing = request.POST.get('passing')
        dribbling = request.POST.get('dribbling')
        defending = request.POST.get('defending')
        physical = request.POST.get('physical')
        age = request.POST.get('age')
        
        # Print input data for debugging
        print(f"Input Data: Pace={pace}, Shooting={shooting}, Passing={passing}, Dribbling={dribbling}, Defending={defending}, Physical={physical}, Age={age}")
        

            
            # Prepare input data as a list of lists
        input_data = [[int(age), int(pace), int(shooting), int(passing), int(dribbling), int(defending), int(physical)]]

            # Make predictions
        predictions = potential_model.predict(input_data)
        ability_prediction=ability_model.predict(input_data)
        print(predictions)
        print(ability_prediction)

            # Extract ability and potential from predictions
        potential =int(predictions)
        print(potential)
        ability=int(ability_prediction)
        print(ability)
        if potential>=5:
            potential=5
        if ability>=5:
            ability=5
        updateUser.player_ability=ability
        updateUser.player_potential=potential
        updateUser.scouted_by=username
        updateUser.save()
        return redirect('ScoutPlayer')

    return render(request, 'ScoutPlayerEdit.html', {
        'updateUser': updateUser,
        'abilityChoices': Ability_Choice,
    })

def scoutClubEdit(request,update_id):
    updateUser=User.objects.get(id=update_id)
    user=request.user
    username = "{} {}".format(user.first_name, user.last_name)
    print(username)
    if request.method=='POST':
        
        club_reputation=request.POST.get('reputation')
        desc=request.POST.get('desc')
        updateUser.club_reputation=club_reputation
        updateUser.desc=desc
        updateUser.scouted_by=username
        updateUser.save()
        print('saved')
        return redirect('ScoutClub')
    return render(request,'ScoutClubEdit.html',{
        'updateUser':updateUser,
        'abilityChoices':Ability_Choice,
        })
def postImage(request):
    user=request.user
    user_id=user.id
    if request.method=='POST':
        feed=request.POST.get('feed')
        img=request.FILES.get('img')
        print(feed,img)
        post=NewFeeds(
            feed=feed,
            img=img,
            user_id=user_id,
            datetime=timezone.now()
        )
        post.save() 
        return redirect('index')
    return render(request,'PostImage.html')
def postVideo(request):
    user=request.user
    user_id=user.id
    if request.method=='POST':
        feed=request.POST.get('feed')
        video=request.FILES.get('video')
        print(feed,video)
        post=NewFeeds(
            feed=feed,
            video=video,
            user_id=user_id,
            datetime=timezone.now()
        )
        post.save() 
        return redirect('index')
    return render(request,'PostVideo.html')
def contract(request,user_id):
    player_id=user_id
    user=request.user
    club_id=user.id
    if request.method=='POST':
        wage=request.POST.get('wage')
        fees=request.POST.get('fee')
        bonus=request.POST.get('bonus')
        cont=Contract(
            wage=wage,
            fees=fees,
            bonus=bonus,
            player_id=player_id,
            club_id=club_id,
            player_negotiating=True,
            contractAccepted=False,
        )
        cont.save()
        return redirect('ClubPlayer')
        print(wage,fees,bonus,player_id,club_id)
    return render(request,'Contract.html')
def contractNegotiation(request,user_id):
    club_id=user_id
    user=request.user
    player_id=user.id
    updateCont=Contract.objects.get(player_id=player_id,club_id=club_id)
    cont=Contract.objects.filter(player_id=player_id,club_id=club_id)
    if request.method=='POST':
        wage=request.POST.get('wage')
        fees=request.POST.get('fee')
        bonus=request.POST.get('bonus')
        updateCont.wage=wage
        updateCont.fees=fees
        updateCont.bonus=bonus
        updateCont.player_negotiating=False
        
        updateCont.save()
        return redirect('player-club')
        print(wage,fees,bonus,player_id,club_id)
    return render(request,'EditContract.html',{'cont':cont})
def contractNegotiationClub(request,user_id):
    player_id=user_id
    user=request.user
    club_id=user.id
    updateCont=Contract.objects.get(player_id=player_id,club_id=club_id)
    cont=Contract.objects.filter(player_id=player_id,club_id=club_id)
    if request.method=='POST':
        wage=request.POST.get('wage')
        fees=request.POST.get('fee')
        bonus=request.POST.get('bonus')
        updateCont.wage=wage
        updateCont.fees=fees
        updateCont.bonus=bonus
        updateCont.player_negotiating=True
        
        updateCont.save()
        return redirect('ClubPlayer')
        print(wage,fees,bonus,player_id,club_id)
    return render(request,'EditContractClub.html',{'cont':cont})
def acceptContract(request,user_id):
    user=request.user
    player_id=user.id
    club_id=user_id
    updateCont=Contract.objects.get(player_id=player_id,club_id=club_id)
    updateCont.contractAccepted=True
    updateCont.save()
    return redirect('player-club')
def acceptContractClub(request,user_id):
    user=request.user
    club_id=user.id
    player_id=user_id
    updateCont=Contract.objects.get(player_id=player_id,club_id=club_id)
    updateCont.contractAccepted=True
    updateCont.save()
    return redirect('ClubPlayer')
def rejectContract(request,user_id):
    user=request.user
    player_id=user.id
    club_id=user_id
    deleteCont=Contract.objects.get(player_id=player_id,club_id=club_id)
    deleteCont.delete()
    return redirect('player-club')
def rejectContractClub(request,user_id):
    user=request.user
    club_id=user.id
    player_id=user_id
    print(club_id,player_id)
    deleteCont=Contract.objects.get(player_id=player_id,club_id=club_id)
    deleteCont.delete()
    return redirect('ClubPlayer')

from django.http import JsonResponse

def like_feed_ajax(request, feed_id):
    user = request.user
    post = NewFeeds.objects.get(id=feed_id)
    current_likes = post.likes_cout
    liked = likes.objects.filter(user=user, feed=post).count()

    if not liked:
        likes.objects.create(user=user, feed=post)
        current_likes += 1
        
    else:
        likes.objects.filter(user=user, feed=post).delete()
        current_likes -= 1

    post.likes_cout = current_likes
    post.save()
    updated_likes_count = post.likes_cout
    print(updated_likes_count)

    # Return the updated like count as JSON
    return JsonResponse({'likes_count': updated_likes_count})
def check_like_status(request, feed_id):
    user = request.user
    post = NewFeeds.objects.get(id=feed_id)
    liked = likes.objects.filter(user=user, feed=post).exists()
    return JsonResponse({'liked': liked})
def is_following(request, followed_id):
    user_id=request.user.id
    is_following=following.objects.filter(following_id=user_id,followed_id=followed_id).exists()
    return JsonResponse({'is_following': is_following})
    
def following_funtion(request,followed_id):
    user_id=request.user.id
    following_obj = following.objects.filter(following_id=user_id,followed_id=followed_id)
    if not following_obj:
        follow=following(
            following_id=user_id,
            followed_id=followed_id
        )
        notification=Notification(
            followingg_id=user_id,
            followed_id=followed_id
        )
        notification.save()
        follow.save()
        return JsonResponse({'message': 'followed'})
    else:
        following.objects.filter(following_id=user_id,followed_id=followed_id).delete()
        Notification.objects.filter(followingg_id=user_id,followed_id=followed_id).delete()
        return JsonResponse({'message': 'unfollowed'})
    
def following_feeds(request):
    user = request.user
    following_users = following.objects.filter(following=user).values_list('followed_id', flat=True)
    
    # Get feeds from the following users, ordered by datetime in descending order
    feeds = NewFeeds.objects.filter(user__in=following_users).order_by('-datetime')
    
    context = {'feeds': feeds}
    return render(request, 'FollowingFeeds.html', context)
#email verification
from django.core import serializers
from django.db.models import Q
def searchByName(request,name):
    
    # name=name.lower()
    users = User.objects.filter(Q(first_name__icontains=name) | Q(club_name__icontains=name) | Q(player_pos__icontains=name) | Q(district__icontains=name) | Q(locality__icontains=name))
    user_data = serializers.serialize('json', users)

    # Return the serialized data as JSON response
    return JsonResponse(user_data, safe=False)
def notificationUsers(request,user_id):

    users = Notification.objects.filter(followed_id=user_id)

    data = []

    # Loop through notifications and include user details
    for notification in users:
        user=User.objects.filter(id=notification.followingg_id)

        
        data.extend(user)

    data=serializers.serialize('json',data)

    # Return the serialized data as JSON response
    return JsonResponse(data, safe=False)
def follower(request,user_id):
    users=following.objects.filter(followed_id=user_id)
    
    return render(request,'follower.html',{'follower':users})
def followingUsers(request,user_id):
    users=following.objects.filter(following_id=user_id)
    
    return render(request,'following.html',{'follower':users})
def likesUsers(request,feed_id):
    users=likes.objects.filter(feed_id=feed_id)
    
    return render(request,'likes.html',{'likes':users})
def deleteNotification(request,user_id):
    print(user_id)
    Notification.objects.get(followingg_id=user_id,followed_id=request.user.id).delete()
    notificationUsers(request,request.user.id)
    count=Notification.objects.filter(followed_id=request.user.id).count()
    return JsonResponse({'message': 'success','notification_count':count})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def validate_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        data = {'is_taken': User.objects.filter(email=email).exists()}
        return JsonResponse(data)
    else:
        # Handle GET requests or other methods if needed
        return JsonResponse({'error': 'Invalid request method'})
