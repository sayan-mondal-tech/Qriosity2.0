from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from .import models
import datetime
from .forms import UserDetails
#from django.contrib.auth.models import User

# Create your views here.

current_leaderboard = None


def logout(request):
    return render(request, 'user/logout.html')


@login_required(login_url='/login', redirect_field_name=None)
def dashboard(request):
    if request.user:
        if request.user.is_authenticated:
            player = models.Player.objects.get(user=request.user)
            print("In dashboard - Name - {}  User - {}".format(player.name, player.user))
            return render(request, 'user/dashboard.html', {'user': player})
        else:
            return redirect('home:home')
    else:
        return redirect('home:home')


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        profile = user
        try:
            player = models.Player.objects.get(user=profile)
        except:
            player = models.Player(user=profile)
            player.last_submit = datetime.datetime.now()
            player.name = response.get('name')
            player.image = response.get('picture')
            player.email = response.get('email')
            player.save()
    elif backend.name == 'facebook':
        profile = user
        try:
            player = models.Player.objects.get(user=profile)
        except:
            player = models.Player(user=profile)
            player.name = response.get(
                'first_name')+" "+response.get('last_name')
            player.email = response.get('email')
            player.image = "http://graph.facebook.com/%s/picture?type=large" \
                % response["id"]
            player.last_submit = datetime.datetime.now()
            player.save()


@login_required(login_url='/login', redirect_field_name=None)
def leaderboard(request):
    global current_leaderboard
    current_leaderboard = models.Player.objects.order_by(
        '-score', '-last_submit')
    return render(request, 'user/leaderboard.html', {'leaderboard': current_leaderboard})


def privacy_policy_fb(request):
    return render(request, "user/privacypolicy.html")


# @login_required(login_url='logout/')
def UserData(request):
    my_form = UserDetails()
    context = {
        "form": my_form
    }
    return render(request, "user/details.html", context)


def Formdata(request):
    if request.method == "POST":
        my_form = UserDetails(request.POST)
        if my_form.is_valid():
            # my form is valid
            form_data = my_form.cleaned_data
            # print(form_data['college'])
            p1 = models.Player.objects.get(user=request.user)
            r = models.PlayerDetails(
                user_name=p1, college=form_data['college'], year=form_data['year'], contact=form_data['contact'],
                full_name=form_data['full_name'])
            r.save()
            # models.PlayerDetails.objects.create(**my_form.cleaned_data

        else:
            z = my_form.errors
            print(z)
    p1 = models.Player.objects.get(user=request.user)

    try:
        r = models.PlayerDetails.objects.get(user_name=p1)
        return render(request, 'user/form_status.html', {"details": r})
    except models.PlayerDetails.DoesNotExist:
        render(request, "user/details.html")

    my_form = UserDetails()
    context = {
        "form": my_form
    }
    return render(request, "user/details.html", context)
