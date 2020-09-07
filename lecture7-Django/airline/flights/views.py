from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight,Passenger
#导入Flight类以便于渲染

# Create your views here.
def index(request):
    #return HttpResponse("Flights")
    # 类似于jiajia
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request,flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")
    context = {
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passenger": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html", context)

def book(request,flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request,"flights/error.html", {"message":"No selection."})    
    except Flight.DoesNotExist:
        return render(request,"flights/error.html", {"message":"No flight."})    
    except Passenger.DoesNotExist:
        return render(request,"flights/error.html", {"message":"No passenger."})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight",args=(flight_id,)))