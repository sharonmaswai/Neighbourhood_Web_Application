from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user.id
            profile.save()

        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile-form.html', {"form":form})
def profile(request):
    # current_user = request.user
    # profile = Profile.objects.filter(user=current_user.id)
    # print(profile)
    # project= Project.objects.all()
    
    return render(request,'profile.html')
def post_concern(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user.id
            profile.save()

        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile-form.html', {"form":form})
def view_concern(request):
    # current_user = request.user
    # profile = Profile.objects.filter(user=current_user.id)
    # print(profile)
    # project= Project.objects.all()
    
    return render(request,'concerns.html')    