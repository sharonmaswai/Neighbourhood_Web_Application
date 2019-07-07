from django import forms
from .models import Profile, Concerns


class ConcernForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','description',)
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','phone_number','bio','image','website') 
