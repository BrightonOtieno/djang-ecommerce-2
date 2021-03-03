from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



PAYMENT_CHOICES = (
    ('S','Stripe'),
    ('P','Paypal')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    # TODO:make the country field False
    shipping_country = CountryField(blank_label='(Select Country)').formfield(
        required = False,
        widget=CountrySelectWidget(attrs={
        "class":"custom-select d-block w-100",
        "id":'country'}))
    shipping_zip = forms.CharField(required=False)
    # the shipping address filled is same as billing address so it will clone shipping (now this is billing address)
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
    set_default_shipping = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
    use_default_shipping = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
    # BILLING
    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(Select Country)').formfield(
        required = False,
        widget=CountrySelectWidget(attrs={
        "class":"custom-select d-block w-100",
        "id":'country'}))

    billing_zip = forms.CharField(required=False)
    set_default_billing = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
    use_default_billing = forms.BooleanField(widget=forms.CheckboxInput(),required=False)
    # PAYMENT
    payment_option = forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_CHOICES)


class CouponForm (forms.Form):
    code = forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Promo Code',
        'aria-label':"Recipient\s username",
        'aria-describedby':'basic-addon2'

    }))


# REFUND FORM
class RefundForm(forms.Form):
    ref_code = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows':4
    }))
    email = forms.EmailField()