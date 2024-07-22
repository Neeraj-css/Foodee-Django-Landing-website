from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Slide, Header,About_Us, Quote,Food_bg, Food_type,Category,Food_item,Event,Reservation
#from .forms import ReservationForm
def BASE(request):
   return render(request,'base.html')

def index(request):
   slides = Slide.objects.all()
   header = Header.objects.first()
   about = About_Us.objects.first()
   quote = Quote.objects.all()
   Fb = Food_bg.objects.first()
   food_type = Food_type.objects.all()
   categories = Category.objects.all()
   food_items = Food_item.objects.all()
   event= Event.objects.all()

   context = {'slides': slides,
              'header': header,
              'about': about,
              'quote': quote,
              'Fb': Fb,
              'food_type': food_type,
              'categories': categories,
              'food_items': food_items,
              'event': event
              }
   if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       occation = request.POST.get('occation')
       day = request.POST.get('day')
       month = request.POST.get('month')
       year = request.POST.get('year')
       time = request.POST.get('time')
       am_pm = request.POST.get('am_pm')
       message = request.POST.get('message')

       # Combine day, month, and year into a single date
       date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

       # Handle time formatting if needed
       time_formatted = f"{time.zfill(4)} {am_pm}"

       # Save to database
       reservation = Reservation(
           name=name,
           email=email,
           occation=occation,
           date=date,
           time=time_formatted,
           message=message
       )
       reservation.save()


   return render(request, 'index.html',context)