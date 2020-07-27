from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
import stripe
from .forms import MembershipDetailForm,DonationForm
from django.conf import settings
from .models import *
import datetime
from django.contrib.auth.models import Group

stripe.api_key = settings.STRIPE_KEY


def create_donation(request):
    print('POST==', request.POST)
    stripe.Charge.create(
        amount=2000,
        source=request.POST['stripeToken'],
        currency="inr",
        description="My First Test Charge (created for API docs)",
    )
    return redirect(reverse('thankyou'))


def chargeCustomer(request):
    print('======chargeCustomer============')
    print(request.POST)
    customer = stripe.Customer.create(
        email=request.POST['email'], name=request.POST['name'], source=request.POST['stripeToken'])

    user_membership_detail = MembershipDetail.objects.get(user=request.user)
    user_membership_detail.stripe_customer_id = customer.id
    user_membership_type = user_membership_detail.membership_type
    if user_membership_detail.membership_term == 'M':
        price_id = user_membership_type.stripe_monthly_price_id
        amount = user_membership_type.monthly_price
        description = user_membership_type.type_name + ' Monthly Plan Payment'

    else:
        price_id = user_membership_type.stripe_yearly_price_id
        amount = user_membership_type.yearly_price_after_discount
        description = user_membership_type.type_name + ' Yearly Plan Payment'

    stripe.Subscription.create(
        customer=customer.id,
        items=[
            {"price": price_id},
        ],
    )
    user_membership_detail.is_paid_up = True
    user_membership_detail.date_joined = datetime.date.today()
    user_membership_detail.save()

    user_payment_history = MemberPaymentHistory()
    user_payment_history.user = request.user
    user_payment_history.amount = amount
    user_payment_history.description = description
    user_payment_history.save()
    
    group = Group.objects.get(name=user_membership_type.membership_group) 
    group.user_set.add(request.user)

    return redirect(reverse('thankyou'))


# def create_subscription(request,customer,price):
#     import stripe
# stripe.api_key = "sk_test_51H4o50DLCEyNZL8YOpFgmi8jI0sWDslQ9GRkPZ12SqkglAkJiidioJGvV0MV0vEYNLVF7Mqd9qbvEhOEDyDslxzg00L3V56wUF"

# stripe.Subscription.create(
#   customer="cus_HiqdXrJnNK61rk",
#   items=[
#     {"price": "price_1H9O8fDLCEyNZL8Y3wigPeIF"},
#   ],
# )


# def create_product(requ)


# def create_membership


#     import stripe
# stripe.api_key = "sk_test_51H4o50DLCEyNZL8YOpFgmi8jI0sWDslQ9GRkPZ12SqkglAkJiidioJGvV0MV0vEYNLVF7Mqd9qbvEhOEDyDslxzg00L3V56wUF"

# stripe.Subscription.create(
#   customer="cus_Hiq6dx4oGJKpRT",
#   items=[
#     {"price": "price_1H9O8fDLCEyNZL8Y3wigPeIF"},
#   ],
# )


# import stripe
# stripe.api_key = "sk_test_51H4o50DLCEyNZL8YOpFgmi8jI0sWDslQ9GRkPZ12SqkglAkJiidioJGvV0MV0vEYNLVF7Mqd9qbvEhOEDyDslxzg00L3V56wUF"

# stripe.Customer.retrieve("cus_Hiq9Jcoa0fYaz9")


# import stripe
# stripe.api_key = "sk_test_51H4o50DLCEyNZL8YOpFgmi8jI0sWDslQ9GRkPZ12SqkglAkJiidioJGvV0MV0vEYNLVF7Mqd9qbvEhOEDyDslxzg00L3V56wUF"

# stripe.Price.create(
#   unit_amount=100000,
#   currency="inr",
#   recurring={"interval": "year"},
#   product="prod_HipoYTBL8x0S0w",
# )


# import stripe
# stripe.api_key = "sk_test_51H4o50DLCEyNZL8YOpFgmi8jI0sWDslQ9GRkPZ12SqkglAkJiidioJGvV0MV0vEYNLVF7Mqd9qbvEhOEDyDslxzg00L3V56wUF"

# stripe.Product.create(name="Gold Special")


def stripee(request):
    return render(request, 'stripee.html')


def stripee_two(request):
    return render(request, 'stripee_two.html')


def membership(request):

    if request.method == 'POST':
        form = MembershipDetailForm(request.POST)
        if form.is_valid():
            print('valid')
            instance = form.save(commit=False)
            instance.user = request.user
            instance.first_name = request.user.first_name
            instance.last_name = request.user.last_name
            instance.save()
            request.payment_type = 'membership'
            # if not request.GET._mutable:
            #     request.GET._mutable = True
            # request.GET['payment_type'] = 'membership'
            # print('GET=========',request.GET)
            return redirect('stripee')
        else:
            print('invalid')
            # instance = form.save()
            context = {'form': form}
            return render(request, 'membership.html', context)

    # initial = {
    #     'first_name': request.user.first_name,
    #     'email': request.user.email}
    # first_name = request.user.first_name
    # last_name = request.user.last_name
    # form = JournalForm(initial={'tank': 123})
    # print('first = ',request.user.first_name)
    # print('last = ',request.user.last_name)
    if not request.GET._mutable:
        request.GET._mutable = True
    request.GET['payment_type'] = 'membership'
    request.GET['age'] = 26
    print('GET=========', request.GET)
    form_intial_values = {
        'first_name': request.user.first_name, 'last_name': request.user.last_name}
    form = MembershipDetailForm(initial=form_intial_values)
    context = {'form': form}
    return render(request, 'membership.html', context)


def donation(request):
    if request.method == 'POST':
        print('7')
        form = DonationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print('valid donation')
            return redirect('stripee_two')
    print('11')
    form = DonationForm()
    context = {'form': form}

    return render(request, 'donation.html', context)
