from django import forms
from .models import Profile, Concerns


class ConcernForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','description', 'link')
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','website') 
