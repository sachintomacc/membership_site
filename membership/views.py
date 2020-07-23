from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
import stripe
# from .forms import MembershipDetailForm


def chargeCustomer(request):
    print('in charge')
    print(request.POST)
    customer = stripe.Customer.create(
        email=request.POST['email'], name=request.POST['name'], source=request.POST['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer, amount=500, currency='inr', description='donation')
    return redirect(reverse('thankyou'))



def stripee(request):
    return render(request, 'stripee.html')


def membership(request):
    initial = {
        'first_name': request.user.first_name,
        'email': request.user.email}
    # form = MembershipDetailForm(initial)
    context ={} #{'form': form}
    return render(request, 'membership.html', context)
