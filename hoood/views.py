from django.shortcuts import render, redirect
from .models import Profile, Concerns, Hood, Business
from .forms import ProfileForm, ConcernForm

# Create your views here.
def index(request):
    hoods = Hood.objects.all()
   
    return render(request, 'index.html',{'hoods':hoods})
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            #profile.user=current_user.id
            profile.save()

        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/profile-form.html', {"form":form})
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user.id)
    print(profile)
    
    
    return render(request,'profile/profile.html',{'profile':profile})
def post_concern(request):
    current_user = request.user
    if request.method == 'POST':
        form = ConcernForm(request.POST, request.FILES)
        if form.is_valid():
            concern = form.save(commit=False)
            #concern.user=current_user.id
            concern.save()

        return redirect('concerns')
    else:
        form = ConcernForm()
    return render(request, 'profile/concern-post.html', {"form":form})
def view_concern(request):
    current_user = request.user
    concerns = Concerns.objects.all()
    
    
    return render(request,'profile/concerns.html',{'concerns':concerns})    
def one_hood(request, hood_id):
    hoods=Hood.objects.filter(id=hood_id) 
    business= Business.objects.filter(id=hood_id)
    return render(request, 'single_hood.html',{'hoods':hoods,'business':business})   
def search_results(request):
    
    if 'search_project' in request.GET and request.GET['search_project']:
        search_term=request.GET.get('search_project')
        
        searched_hood=Hood.search_project(search_term)
        
    return render(request,'search.html',{'searched_hood':searched_hood})  