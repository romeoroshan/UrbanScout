from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

# Create your models here.

Pos_Choice = (
    ("GoalKeeper", "GoalKeeper"),
    ("Left Back", "Left Back"),
    ("Right Back", "Right Back"),
    ("Centre Back", "Centre Back"),
    ("Centre Defensive Midfielder", "Centre Defensive Midfielder"),
    ("cm", "Centre Midfielder"),
    ("Centre Attackin Midfielder", "Centre Attackin Midfielder"),
    ("Left Midfileder", "Left Midfileder"),
    ("Right Midfielder", "Right Midfielder"),
    ("Left Winger", "Left Winger"),
    ("Right Winger", "Right Winger"),
    ("Striker", "Striker"),
)

Foot_Choice = (
    ("Left", "Left"),
    ("Right", "Right"),
    ("Both", "Both")
)

Ability_Choice = (
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)
District_Choice=(
    ("Thiruvananthapuram", "Thiruvananthapuram"),
    ("Kollam", "Kollam"),
    ("Pathanamthitta", "Pathanamthitta"),
    ("Alappuzha", "Alappuzha"),
    ("Kottayam", "Kottayam"),
    ("Idukki", "Idukki"),
    ("Ernakulam", "Ernakulam"),
    ("Thrissur", "Thrissur"),
    ("Palakkad", "Palakkad"),
    ("Malappuram", "Malappuram"),
    ("Kozhikkod", "Kozhikkod"),
    ("Wayanad", "Wayanad"),
    ("Kannur", "Kannur"),
    ("Kasaragod", "Kasaragod"),
)

def validate_dob(value):
    if value > date(2016, 1, 1):
        raise ValidationError("Date of Birth cannot be later than 2016.")
class User(AbstractUser):
    username=models.CharField(max_length=32, blank=True, null=True)
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    img=models.ImageField(upload_to='pics',default='https://img.freepik.com/free-icon/man_318-677829.jpg',null=True)
    is_player=models.BooleanField('is_player',default=False)
    is_club=models.BooleanField('is_club',default=False)
    is_scout=models.BooleanField('is_scout',default=False)
    player_dob = models.DateField(("Date of Birth"), default=date.today, validators=[validate_dob])
    player_pos = models.CharField(("Position"),default='',max_length=30,choices=Pos_Choice)
    district = models.CharField(("District"),default='',max_length=20,choices=District_Choice)
    locality = models.CharField(("Locality"),default='',max_length=50,blank=True)
    player_foot = models.CharField(("Prefered Foot"),default='',max_length=10,choices=Foot_Choice)
    player_ability = models.IntegerField(("Ability"),default=0,choices=Ability_Choice)
    club_reputation = models.IntegerField(("Club Reputation"),default=0,choices=Ability_Choice)
    player_potential = models.IntegerField(("Potential"),default=0,choices=Ability_Choice)
    desc=models.CharField(("Description"),max_length=100, default='')
    club_name=models.CharField((("Club Name")),default='',max_length=30)
    scouted_by=models.CharField(max_length=30,default='')
    REQUIRED_FIELDS = [] 
    
class Player(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    player_dob = models.DateField(("Date of Birth"), default=date.today, validators=[validate_dob])
    player_pos = models.CharField(("Position"),default='',max_length=30,choices=Pos_Choice)
    district = models.CharField(("District"),default='',max_length=20,choices=District_Choice)
    locality = models.CharField(("Locality"),default='',max_length=50,blank=True)
    player_foot = models.CharField(("Prefered Foot"),default='',max_length=10,choices=Foot_Choice)
    player_ability = models.IntegerField(("Ability"),default=0,choices=Ability_Choice)
class InterestedClubs(models.Model):
    club=models.ForeignKey(User, on_delete=models.CASCADE, related_name='interested_clubs_as_club')
    player=models.ForeignKey(User, on_delete=models.CASCADE, related_name='interested_clubs_as_player')
class ShortlistedPlayers(models.Model):
    club=models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortlisted_players_as_club')
    player=models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortlisted_players_as_player')
class ShortlistedScouts(models.Model):
    scout=models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortlisted_scouts_as_scout')
    player=models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortlisted_scouts_as_player')
class ShortlistedClubScouts(models.Model):
    scout=models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortlisted_club_scouts_as_scout')
    club=models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortlisted_club_scouts_as_player')
class PostFeed(models.Model):
    feed=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_feed_as_user')
class PostImageFeed(models.Model):
    feed=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_image_feed_as_user')
class PostVideoFeed(models.Model):
    feed=models.CharField(max_length=200)
    video = models.FileField(upload_to='pics',
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_video_feed_as_user')
class Contract(models.Model):
    player=models.ForeignKey(User, on_delete=models.CASCADE, related_name='contract_as_player')
    club=models.ForeignKey(User, on_delete=models.CASCADE, related_name='contract_as_club')
    wage=models.IntegerField()
    fees=models.IntegerField()
    bonus=models.CharField(max_length=200)
    contractAccepted=models.BooleanField(default=False)
    player_negotiating=models.BooleanField(default=False)
class NewFeeds(models.Model):
    feed=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics',null=True)
    video = models.FileField(upload_to='pics',
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='newfeeds_as_user')
    datetime = models.DateTimeField(null=True)
    likes_cout=models.IntegerField(default=0)
class likes(models.Model):
    feed=models.ForeignKey(NewFeeds,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes_as_user')
class following(models.Model):
    followed=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following_followed')
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following_following')
class Notification(models.Model):
    followed=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notification_followed')
    followingg=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notification_followingg')
    timestamp=models.DateTimeField(auto_now_add=True)