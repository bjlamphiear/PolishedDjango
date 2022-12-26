from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']


       # Send Email
		send_mail(
			message_name, #subject
			message, #message
			message_email, # from email
       		['bjlamphiear@gmail.com','linzymae84@gmail.com'], #to email
 				)

		return render(request, 'contact.html', {'message_name':message_name})


	else:
		return render(request, 'contact.html', {})
def about(request):
	return render(request, 'about.html', {})
def pricing(request):
	return render(request, 'pricing.html', {})
def service(request):
	return render(request, 'service.html', {})

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']

		# Send Email
      	
		appointment = "Name: "+ your_name + "Phone: " + your_phone + "Email: "+ your_email + "Address: "+ your_address + "Date: " +  your_date + "Time"+  your_schedule + "Your Message: "+  your_message
		
		send_mail(
			'Polished Appointment Reqest', #subject
			appointment, #message
			your_email, # from email
      		['bjlamphiear@gmail.com','linzymae84@gmail.com'], #to email
 			)

		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_message': your_message})


	else:
		return render(request, 'home.html', {})
