from django.shortcuts import render,redirect
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	Contact.objects.create(
			name = request.POST['name'],
			email = request.POST['email'],
			subject = request.POST['subject'],
			message = request.POST['message'],
		)

	subject = 'Contact for Sunil'
	message = 'Hello, ' + request.POST['name'] + '\n\n' + 'Thanks for contacting us, We will contact you soon.'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [request.POST['email'],]
	send_mail( subject, message, email_from, recipient_list )

	subject1 = 'Contact from Website'
	message1 = 'Hello Sunil, ' + '\n\n' + request.POST['name'] + ' want to contact you.' + '\n\n' + 'Name : ' + request.POST['name'] + '\n' +'Email : ' + request.POST['email'] + '\n' + 'Subject : ' + request.POST['subject'] + '\n' + 'Message : ' + request.POST['message']
	recipient_list1 = ['sunilcprajapati2001@gmail.com',]
	send_mail( subject1, message1, email_from, recipient_list1 )

	return redirect('/')