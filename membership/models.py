from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class MembershipDetail(models.Model):
    membership_type = models.ForeignKey(
        'MembershipType', on_delete=models.CASCADE)
    title = models.ForeignKey(
        'Title', null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city_id = models.ForeignKey('City', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    telephone = models.IntegerField()
    date_joined = models.DateField(auto_now=False, auto_now_add=False)
    date_terminated = models.DateField(auto_now=False, auto_now_add=False)
    is_paid_up = models.BooleanField()
    notes = models.TextField()

    class Meta:
        verbose_name = 'MembershipDetail'
        verbose_name_plural = 'MembershipDetails'

    def __str__(self):
        return self.first_name


class MembershipType(models.Model):
    type_name = models.CharField(max_length=50)
    monthly_price = models.IntegerField()
    yearly_price_after_discount = models.IntegerField()

    class Meta:

        verbose_name = 'MembershipType'
        verbose_name_plural = 'MembershipTypes'

    def __str__(self):
        return self.type_name


class MemberPaymentHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment_id = models.IntegerField()

    class Meta:

        verbose_name = 'MemberPaymentHistory'
        verbose_name_plural = 'MemberPaymentHistories'

    def __str__(self):
        return self.user.username


class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.name
