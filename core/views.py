from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from django.conf import settings
from .forms import UserPreferencesForm
import stripe
from .models import UserPreferences,Preference
from membership.models import MembershipDetail
from django.core.exceptions import ObjectDoesNotExist


@login_required
def home(request):

    user_preferences, created = UserPreferences.objects.get_or_create(
        user=request.user)
    user_preferences.user = request.user
    user_preferences.save()
    if user_preferences.saved_user_prefereces:
        response = redirect('dashboard')
    else:
        response = redirect('user_preferences')

    return response


@login_required
def dashboard(request):
    try:
        membership = MembershipDetail.objects.get(user=request.user)
        membership_type_name = membership.membership_type.type_name
    except:
        membership_type_name = None
    context = {'membership_type_name':membership_type_name}
    return render(request, 'dashboard.html',context)


@login_required
def user_preferences(request):
    form = UserPreferencesForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user  = request.user
        print('>>>>>>>>>>>>>>>>>>>>>>>',instance)
        print('>>>>>>>>>>>>>>>>>>>>>>>',instance.id)
        print('>>>>>>>>>>>>>>>>>>>>>>>',instance.user)
        user_preference = UserPreferences.objects.get(user=request.user)
        user_preference.saved_user_prefereces = True
        user_preference.save()

        for preference in instance.preferences:
            user_preference.preferences.add(Preference.objects.get(id=preference.id))



        # user_preference.save_m2m()

        # user_preference.delete()

        # instance = form.save(commit=False)
        # print('==',instance.preferences.all())
        # instance.user = request.user
        # instance.saved_user_prefereces = True
        # instance.save()

        return redirect(reverse('thankyou'))

    context = {'form': form, 'username':request.user.username}
    return render(request, 'user_preferences.html', context)


def thankyou(request):
    return render(request, 'thankyou.html')
