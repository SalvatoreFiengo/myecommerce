from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Userprofile
from accounts.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserForm
from helper.variables import background

def index(request):
    """return index.html file"""
    return redirect(reverse('products'))

@login_required
def logout(request):
    """log user out"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out", extra_tags="Login Status")
    return redirect(reverse("index"))

def login(request):
    """return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST["name"],
                                    password=request.POST["password"])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Hi {0}. You are successfully logged in".format(request.POST["name"]), extra_tags="Login Status")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form, "background_image":background["default"]})

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered", extra_tags="Registation Status")

                return redirect('edit_profile')
            else:
                messages.error(request, "Unable to register your account at this time", extra_tags="Registration Status")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        'registration_form': registration_form,
        "background_image":background["default"]})

@login_required
def user_profile(request):
    """Renders the user profile page"""
    user = User.objects.get(pk=request.user.id)
    return render(request, 'profile.html', {'user': user, 'profile': user.userprofile, "background_image":background["default"]})

@login_required
def edit_profile(request):
    """User can Edit Profile page"""
    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {"user_form": user_form,"profile_form": profile_form, "background_image":background["default"]})

def update_profile(request):
    """User can update its profile via Profile.html and related form"""
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'), extra_tags="Profile Updated")
            return redirect(reverse('index'))
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        "background_image":background["default"]
    })