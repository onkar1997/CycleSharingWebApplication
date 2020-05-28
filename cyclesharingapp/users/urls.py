from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('bookmyride', views.bookmyride, name='bookmyride'),
    path('booking', views.booking, name='booking'),
    path('userDashboard', views.userDashboard, name='userDashboard'),
    path('adminDashboard', views.adminDashboard, name='adminDashboard'),
    path('registeredUser', views.registeredUser, name='registeredUser'),
    path('registeredRide', views.registeredRide, name='registeredRide'),
    path('BhavansToSpit', views.BhavansToSpit, name='BhavansToSpit'),
    path('LakeToSpit', views.LakeToSpit, name='LakeToSpit'),
    path('LibraryToSpit', views.LibraryToSpit, name='LibraryToSpit'),
    path('deleteUser/<int:id>', views.deleteUser, name='deleteUser'),
    path('deleteRide/<int:id>', views.deleteRide, name='deleteRide'),
    path('contact', views.contact, name='contact'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('receivedFeedback', views.receivedFeedback, name='receivedFeedback'),
    path('deleteFeedback/<int:id>', views.deleteFeedback, name='deleteFeedback'),
    path('payment', views.payment, name='payment'),
    path('donePayment', views.donePayment, name='donePayment'),

]
