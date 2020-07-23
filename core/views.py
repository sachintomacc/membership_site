from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from django.conf import settings
from .forms import UserPreferencesForm
import stripe
from .models import UserPreferences

# stripe.api_key = "sk_test_51H4o50DLCEyNZL8YOpFgmi8jI0sWDslQ9GRkPZ12SqkglAkJiidioJGvV0MV0vEYNLVF7Mqd9qbvEhOEDyDslxzg00L3V56wUF"




# def test_cookie(request):
#     if not request.COOKIES.get('logged_in_user'):

#         response.set_cookie('user_logged_in',request.user.username,max_age=30)
#         return response
#     else:
#         response = HttpResponse('your fav team is {}'.format(request.COOKIES['team']))
#         return response

# set_cookie(key, value='', max_age=None, expires=None, path='/', domain=None, secure=None, httponly=False, samesite=None) :











@login_required
def home(request):

    user_preferences,created = UserPreferences.objects.get_or_create(user=request.user)
    if user_preferences.saved_user_prefereces:
        response = redirect('dashboard')
    else:
        response = redirect('user_preferences')
 
    return response


@login_required
def dashboard(request):
    response = render(request,'dashboard.html')
    # response.set_cookie('logged_in_user',request.user.username,max_age=10)
    return response





@login_required
def user_preferences(request):
    form = UserPreferencesForm(request.POST or None)
    if form.is_valid():
        preferences = UserPreferences.objects.get(user=request.user)
        preferences.option_1 = form.cleaned_data.get('option_1')
        preferences.option_2 = form.cleaned_data.get('option_2')
        preferences.option_3 = form.cleaned_data.get('option_3')
        preferences.user = request.user
        preferences.saved_user_prefereces = True
        preferences.save()
        return redirect(reverse('thankyou'))

    context = {'form': form}
    return render(request, 'user_preferences.html', context)


def thankyou(request):
    return render(request, 'thankyou.html')



