from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

# ✅ Appointment Form
class AppointmentForm(forms.Form):
    your_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Name'
    }))
    your_phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Phone'
    }))
    your_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Email'
    }))
    your_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Address'
    }))
    your_schedule = forms.ChoiceField(choices=[
        ('9 AM to 10 AM', '9 AM to 10 AM'),
        ('11 AM to 12 PM', '11 AM to 12 PM'),
        ('2 PM to 4 PM', '2 PM to 4 PM'),
        ('8 PM to 10 PM', '8 PM to 10 PM'),
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    your_date = forms.ChoiceField(choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    your_message = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Your Message'
    }))
    captcha = ReCaptchaField(widget=ReCaptchaV3)

# ✅ Contact Form
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Your Message'
    }))
    captcha = ReCaptchaField(widget=ReCaptchaV3)