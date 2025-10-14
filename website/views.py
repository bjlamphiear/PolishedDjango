from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, AppointmentForm  # ✅ Import both forms

# ✅ Static pages
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def service(request):
    return render(request, 'service.html')

# ✅ Contact form with validation
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                subject=cd['name'],
                message=cd['message'],
                from_email=cd['email'],
                recipient_list=['bjlamphiear@gmail.com', 'linzymae84@gmail.com'],
            )
            return render(request, 'contact.html', {
                'message_name': cd['name'],
                'form': ContactForm(),  # Reset form after success
                'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY,
            })
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY,
    })

# ✅ Appointment form with reCAPTCHA and review page
def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            appointment_details = (
                f"Name: {cd['your_name']}\n"
                f"Phone: {cd['your_phone']}\n"
                f"Email: {cd['your_email']}\n"
                f"Address: {cd['your_address']}\n"
                f"Date: {cd['your_date']}\n"
                f"Time: {cd['your_schedule']}\n"
                f"Message: {cd['your_message']}"
            )

            send_mail(
                subject='Polished Appointment Request',
                message=appointment_details,
                from_email=cd['your_email'],
                recipient_list=['bjlamphiear@gmail.com', 'linzymae84@gmail.com'],
            )

            return render(request, 'review.html', {
                'your_name': cd['your_name'],
                'your_phone': cd['your_phone'],
                'your_email': cd['your_email'],
                'your_address': cd['your_address'],
                'your_schedule': cd['your_schedule'],
                'your_date': cd['your_date'],
                'your_message': cd['your_message'],
            })
        else:
            return render(request, 'appointment.html', {
                'form': form,
                'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY,
            })
    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {
        'form': form,
        'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY,
    })