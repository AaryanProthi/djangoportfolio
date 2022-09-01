from django.shortcuts import render, HttpResponse, redirect
from home.models import Message
from django.contrib import messages


# Create your views here.

def index(request):
    # return HttpResponse("Homepage")
    return render(request, 'index.html')

def achievements(request):
    return render(request, 'achievements.html')

def contact(request):
    
    return render(request, 'contact.html')

def message(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']
        # print(name, email, subject, message)
        message = Message(name = name, email = email, message = message)
        message.save()
        messages.success(request, "Thank You for reaching out! Message posted successfully")
        return redirect('message')
    return render(request, 'message.html')