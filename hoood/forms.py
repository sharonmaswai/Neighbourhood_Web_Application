from django import forms
from .models import Profile, Concerns


class ConcernForm(forms.ModelForm):
    class Meta:
        model = Concerns
        fields = ('title','description',)
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','phone_number','bio','image','street_name') 
