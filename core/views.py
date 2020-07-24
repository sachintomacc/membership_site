from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from django.conf import settings
from .forms import UserPreferencesForm
import stripe
from .models import UserPreferences


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
    response = render(request, 'dashboard.html')
    return response


@login_required
def user_preferences(request):
    form = UserPreferencesForm(request.POST or None)
    if form.is_valid():
        user_preference = UserPreferences.objects.get(user=request.user)
        user_preference.delete()

        instance = form.save(commit=False)
        instance.user = request.user
        instance.saved_user_prefereces = True
        instance.save()

        return redirect(reverse('thankyou'))

    context = {'form': form}
    return render(request, 'user_preferences.html', context)


def thankyou(request):
    return render(request, 'thankyou.html')
