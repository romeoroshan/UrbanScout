from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class DateInput(forms.DateInput):
    input_type='date'






class LoginForm(forms.Form):
    email= forms.EmailField(
        widget= forms.TextInput(
            attrs={
                "class": "",
                "id":"email"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": ""
            }
        )
    )
    

#player


class PlayerSignUpForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "",
                "id":"pass"
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "",
                "id":"cpass"
                
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "",
                "id":"fn"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "",
                "id":"sn"
            }
        )
    )
    email=forms.EmailField(widget=forms.EmailInput(attrs={"id":"mail"}))
    player_dob=forms.DateField(widget=forms.DateInput(attrs={"id":"dateofbirth","type":"date"}))
    
    class Meta:
        model = User
        fields = ('img','first_name','last_name','email', 'password1', 'password2','player_dob')
        widgets={
            'player_dob':DateInput(),
        }

class ClubRegistraionForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "",
                "id":"pass"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "",
                "id":"cpass"
            }
        )
    )
    email=forms.EmailField(widget=forms.EmailInput(attrs={"id":"mail"}))
    
    
    class Meta:
        model = User
        fields = ('img','club_name','email', 'password1', 'password2','district','locality')