from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm, AppointmentForm

# Recipients for all form submissions
NOTIFICATION_RECIPIENTS = ['bjlamphiear@gmail.com', 'linzymae84@gmail.com']


def _strip_header(value):
    """Strip CR/LF from any user-supplied value used in email headers
    to prevent email-header injection."""
    if value is None:
        return ''
    return str(value).replace('\r', ' ').replace('\n', ' ').strip()


# Static pages
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pricing(request):
    return render(request, 'pricing.html')


def service(request):
    return render(request, 'service.html')


# Contact form
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            visitor_name = _strip_header(cd['name'])
            visitor_email = _strip_header(cd['email'])

            email = EmailMessage(
                subject=f"New contact form message from {visitor_name}",
                body=f"From: {visitor_name} <{visitor_email}>\n\n{cd['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=NOTIFICATION_RECIPIENTS,
                reply_to=[visitor_email],
            )
            email.send(fail_silently=False)

            return render(request, 'contact.html', {
                'message_name': cd['name'],
                'form': ContactForm(),
                'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY,
            })
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'RECAPTCHA_PUBLIC_KEY': settings.RECAPTCHA_PUBLIC_KEY,
    })


# Appointment form
def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            visitor_name = _strip_header(cd['your_name'])
            visitor_email = _strip_header(cd['your_email'])

            appointment_details = (
                f"Name: {visitor_name}\n"
                f"Phone: {cd['your_phone']}\n"
                f"Email: {visitor_email}\n"
                f"Address: {cd['your_address']}\n"
                f"Day: {cd['your_date']}\n"
                f"Time: {cd['your_schedule']}\n"
                f"Message: {cd['your_message']}"
            )

            email = EmailMessage(
                subject=f"Polished appointment request from {visitor_name}",
                body=appointment_details,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=NOTIFICATION_RECIPIENTS,
                reply_to=[visitor_email],
            )
            email.send(fail_silently=False)

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