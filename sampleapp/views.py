from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

# Create your views here
# def phello(request):
#     return HttpResponse("Hello World!")

def index(request):
    return render(request, 'index.html')

def loginpage2(request):
    return render(request,'loginpage2.html')

@csrf_exempt
def contact_mail(request):
    if request.method == 'POST':
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        message=request.POST.get('Message')
        print(name, email, message)
        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=message,
            from_email='noreply@example.com',
            recipient_list=['ananthuckofficial@gmail.com'],
        )
        
        return redirect('index')
    return render(request, 'Index.html')