from django.shortcuts import render
from accounts.models import User
from farmer.models import Bit
from django.conf import settings
import requests
import googlemaps   
# Create your views here.
def deliveryman(request):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    username=user.name
    return render(request,'deliveryman.html',{'username':username})

def profile(request):
    user_id=request.session.get('user_id')
    profile=User.objects.get(id=user_id)
    return render(request,'deliveryman_profile.html',{'profile':profile})

def myproduct(request):
    try:
        user_id=request.session.get('user_id')
        user=User.objects.get(id=user_id)
        username=user.name
        city=user.city
        bits=Bit.objects.filter(status='True')        
        return render(request,'deliveryman_myproduct.html',{'username':username,'bits':bits}) 
    except User.DoesNotExist:
        pass
        return render(request,'deliveryman_myproduct.html',{'username':username})




def productsdelivered(request):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    username=user.name
    return render(request,'deliveryman_productsdelivered.html',{'username':username})

def location(request,farmer_address,bitter_address):
    print('wow',farmer_address,bitter_address)
    
    if farmer_address !=  None:
        from_address_string = str(farmer_address)
        gmaps=googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY )
        result=gmaps.geocode(from_address_string)[0]
        geometry=result.get('geometry',{})
        location1=geometry.get('location',{})
        lat=location1.get('lat',None)
        lng=location1.get('lng',None)
        print('hey',lat,lng)
        
        to_address_string = str(bitter_address)
        gmaps=googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY )
        result1=gmaps.geocode(to_address_string)[0]
        geometry1=result1.get('geometry',{})
        location2=geometry1.get('location',{})
        lat1=location2.get('lat',None)
        lng1=location2.get('lng',None)
        print('hey',lat1,lng1)    

        calculate=gmaps.distance_matrix(
                from_address_string,
                to_address_string   
        )
        print(calculate)

        duration_seconds = calculate['rows'][0]['elements'][0]['duration']['value']
        duration_minutes = duration_seconds/60

        distance_meters = calculate['rows'][0]['elements'][0]['duration']['value']
        distance_kilometers = distance_meters/1000

        if 'distance_in_traffic' in calculate['rows'][0]['elements'][0]:
            duration_in_traffic_seconds = calculate['rows'][0]['elements'][0]['distance_in_traffic']['value'] 
            duration_in_traffic_minutes = duration_in_traffic_seconds/60
        else:
            duration_in_traffic_minutes = None


        print(duration_minutes)
        print(distance_kilometers)   
        print(duration_in_traffic_minutes)   

    else:
        result=""    
    
    return render(request,'deliveryman_location.html',{'lat':lat,'lng':lng,'lat1':lat1,'lng1':lng1})