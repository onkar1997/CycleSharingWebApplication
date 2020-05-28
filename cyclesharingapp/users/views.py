from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from bookride.models import Book
from contact.models import Contact
from payment.models import Pay
from datetime import datetime
from django.core.mail import send_mail
from cyclesharingapp import settings
import zerosms
import requests
import json
import cv2
from pyzbar import pyzbar
from tkinter import *
from imutils.video import VideoStream
import imutils


# Registeration

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                send_mail(
                    'UBike',
                    'Thanks for registering on UBike',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                user.save()
        else:
            messages.error(request, "Password dosen't match")
            return redirect('register')
        return redirect('login')
    else:
        return render(request, 'register.html')


# Login
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, username+" Logged In")
            return redirect("userDashboard")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")
    else:
        return render(request, 'login.html')


# Logout
def logout(request):
    auth.logout(request)
    return redirect("/")


# deleting user
def deleteUser(request, id):
    u = User.objects.get(id=id)
    u.delete()
    return redirect(registeredUser)


# Book page
def bookmyride(request):
    return render(request, 'book.html')


# book a ride
def booking(request):
    if request.method == 'POST':
        pickup_location = request.POST['pickup_location']
        drop_location = request.POST['drop_location']
        from_time = datetime.now()
        to_time = request.POST['to_time']
        fare = request.POST['fare']
        book_date = datetime.now()
        user_id = request.user.id
        b = Book(pickup_location=pickup_location, drop_location=drop_location,
                 from_time=from_time, to_time=to_time, fare=fare, book_date=book_date, user_id=user_id)

        if Book.objects.filter(user_id=user_id).exists():
            messages.error(request, 'Ride Already Booked')
            return redirect('booking')
        else:
            b.save()

            if (pickup_location == 'Spit College' and drop_location == 'Bhavans College' or pickup_location == 'Bhavans College' and drop_location == 'Spit College'):
                return render(request, 'BhavansToSpit.html')
            elif (pickup_location == 'Spit College' and drop_location == 'Bhavans Lake' or pickup_location == 'Bhavans Lake' and drop_location == 'Spit College'):
                return render(request, 'LakeToSpit.html')
            elif (pickup_location == 'Spit College' and drop_location == 'Bhavans Ground' or pickup_location == 'Bhavans Ground' and drop_location == 'Spit College'):
                return render(request, 'SpitToGround.html')
            elif (pickup_location == 'Bhavans College' and drop_location == 'Bhavans Ground' or pickup_location == 'Bhavans Ground' and drop_location == 'Bhavans College'):
                return render(request, 'GroundToBhavans.html')
            elif (pickup_location == 'Bhavans College' and drop_location == 'Bhavans Lake' or pickup_location == 'Bhavans Lake' and drop_location == 'Bhavans College'):
                return render(request, 'LakeToBhavans.html')
            elif (pickup_location == 'Bhavans Lake' and drop_location == 'Bhavans Ground' or pickup_location == 'Bhavans Ground' and drop_location == 'Bhavans Lake'):
                return render(request, 'LakeToGround.html')
    else:
        return render(request, 'book.html')


# delete a ride booked
def deleteRide(request, id):
    b = Book.objects.get(id=id)
    b.delete()
    return redirect(registeredRide)


# user dashboard
def userDashboard(request):
    try:
        bookrideInfo = Book.objects.all()
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    # return render(request, 'polls/detail.html', {'poll': p})
    return render(request, 'userDashboard.html', {'details': bookrideInfo})


# admin dashboard
def adminDashboard(request):
    return render(request, 'adminDashboard.html')


# admindashboard/registered user
def registeredUser(request):
    try:
        userInfo = User.objects.all()
    except Book.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'registeredUser.html', {'users': userInfo})
    # return render(request, 'registeredUser.html')


# admindashboard/registered rides
def registeredRide(request):
    try:
        bookrideInfo = Book.objects.all().order_by("-pk")
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'registeredRide.html', {'details': bookrideInfo})


def BhavansToSpit(request):
    return render(request, 'BhavansToSpit.html')


def LakeToSpit(request):
    return render(request, 'LakeToSpit.html')


def LibraryToSpit(request):
    return render(request, 'LibraryToSpit.html')


# contact
def contact(request):
    return render(request, 'contact.html')
    # return render(request, 'contact.html')


# contactUs
def contactUs(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.user.id
        phone = request.POST['phone']

        cont = Contact(
            first_name=first_name, last_name=last_name, email=email, phone=phone, message=message, user_id=user_id)
        cont.save()
        messages.info(
            request, "Thanks for Contacting Us! We'll get back to you soon. . .")

        URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request

        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
                'apikey': apiKey,
                'secret': secretKey,
                'usetype': useType,
                'phone': phoneNo,
                'message': textMessage,
                'senderid': senderId
            }
            return requests.post(reqUrl, req_params)

        # get response
        response = sendPostRequest(URL, '5MS0GYT0UVVIO57SV2ME5Y59E8T2B9X1', '8I2ZFK3VCEE348PP',
                                   'stage', phone, 'onkarpawar25@gmail.com', 'From UBike, Thanks for Contacting us, we will get back to you soon')

        return redirect('contact')

    else:
        return render(request, 'contact.html')

# received messages/feedbacks


def receivedFeedback(request):
    try:
        msg = Contact.objects.all()
    except Contact.DoesNotExist:
        raise Http404("Contacts does not exist")
    return render(request, 'receivedFeedback.html', {'msgs': msg})


# delete feedback / message
def deleteFeedback(request, id):
    c = Contact.objects.get(id=id)
    c.delete()
    return redirect(receivedFeedback)


def payment(request):
    return render(request, 'payment.html')


def donePayment(request):
    if request.method == 'POST':
        username = request.user.username
        cardNumber = request.POST['cardNumber']
        cardExpiry = request.POST['cardExpiry']
        cardCv = request.POST['cardCv']
        cardHolder = request.POST['cardHolder']
        totalAmount = "10"
        user_id = request.user.id

        p = Pay(
            username=username, cardNumber=cardNumber, cardExpiry=cardExpiry, cardCv=cardCv, cardHolder=cardHolder, totalAmount=totalAmount, user_id=user_id)
        p.save()
        messages.success(
            request, "Payment Successfully Done! Ride booked.")
        return (request, 'book.html')
    else:
        return render(request, 'payment.html')
