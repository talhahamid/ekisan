from django.shortcuts import render,redirect
from accounts.models import User,Subscription,Profilepic
from seller.models import Products
from .models import Product,Agreement,Renter
from dealer.models import Bit
from django.urls import reverse 
from django.http import JsonResponse,HttpResponse
import razorpay
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import os
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

# Create your views here.

def farmer(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        dealers = User.objects.filter(role='Dealer')
        return render(request,'farmers_farmer.html',{'dealers':dealers,'user_name':user_name})

def vegitables(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'vegitables_farmer.html',{'user_name':user_name}) 

def fruits(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'fruits_farmer.html',{'user_name':user_name}) 

def crops(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'crops_farmer.html',{'user_name':user_name}) 

def herb(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'herb_farmer.html',{'user_name':user_name}) 


def nuts(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'nuts_farmer.html',{'user_name':user_name}) 

def grains(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'grains_farmer.html',{'user_name':user_name}) 


def legumes(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'legumes_farmer.html',{'user_name':user_name}) 


def tubers(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'tubers_farmer.html',{'user_name':user_name}) 


def berries(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'berries_farmer.html',{'user_name':user_name}) 


def flowers(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'flowers_farmer.html',{'user_name':user_name}) 


def leafygreens(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'leafygreens_farmer.html',{'user_name':user_name}) 


def roots(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'roots_farmer.html',{'user_name':user_name}) 



def spices(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'spices_farmer.html',{'user_name':user_name}) 



def medicinalplants(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'medicinalplants_farmer.html',{'user_name':user_name}) 



def mushrooms(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'mushrooms_farmer.html',{'user_name':user_name}) 



def pulses(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'pulses_farmer.html',{'user_name':user_name}) 




def oilseeds(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'oilseeds_farmer.html',{'user_name':user_name}) 


def covercrops(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'covercrops_farmer.html',{'user_name':user_name}) 



def condiments(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'condiments_farmer.html',{'user_name':user_name}) 



def exoticplants(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'exoticplants_farmer.html',{'user_name':user_name}) 




def farmerprofile(request):
        user_id = request.session.get('user_id')
        if user_id is not None:
                profile = User.objects.get(id=user_id)
                profilepic = None
                try:        
                        subscription=Subscription.objects.get(user=user_id)
                        plantype=subscription.planname
                        date=subscription.date
                        expiry_date=subscription.expiry_date
                        user_id = request.session.get('user_id')
                        user=User.objects.get(id=user_id)
                        profilepic=Profilepic.objects.get(user=user)
                        if plantype=='free':
                                if (subscription is not None):
                                        return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})
                        else:
                                expiry_date=date + timedelta(days=30)
                                if (subscription is not None):
                                        return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})    
                except ObjectDoesNotExist:
                       return render(request, 'farmerprofile_farmer.html', {'profile': profile,'profilepic':profilepic})
        else:
                return render(request, 'index.html')
        
def editfarmerprofile(request,id):
       farmer=User.objects.get(id=id)
       return render(request,'editfarmerprofile_farmer.html',{'farmer':farmer})       

def updatefarmerprofile(request,id):
       user=User.objects.get(id=id)
       if request.method=='POST':
              user.name=request.POST['name']
              user.address=request.POST['address']
              user.city=request.POST['city']
              user.state=request.POST['state']
              user.save()
              user_id = request.session.get('user_id')
              if user_id is not None:
                        profile = User.objects.get(id=user_id)
                        try:        
                                subscription=Subscription.objects.get(user=user_id)
                                plantype=subscription.planname
                                date=subscription.date
                                expiry_date=subscription.expiry_date
                                if plantype=='free':
                                        if (subscription is not None):
                                                return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription})
                                else:
                                        expiry_date=date + timedelta(days=30)
                                        if (subscription is not None):
                                                return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription})    
                        except ObjectDoesNotExist:
                         return render(request, 'farmerprofile_farmer.html', {'profile': profile})
              else:
                        return render(request, 'index.html')       
       return redirect(('farmerprofile')) 


def farmerprofilepic(request):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        try:
                profile=Profilepic.objects.get(user=user)
                if profile:
                        profile.profilepic=request.FILES['profilepic']
                        profile.save()
                        file_name = profile.profilepic.name
                        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                        with open(file_path, 'wb') as destination:
                                for chunk in profile.profilepic.chunks():
                                        destination.write(chunk)  
                        user_id = request.session.get('user_id')
                        if user_id is not None:
                                profile = User.objects.get(id=user_id)
                                try:        
                                        subscription=Subscription.objects.get(user=user_id)
                                        plantype=subscription.planname
                                        date=subscription.date
                                        expiry_date=subscription.expiry_date
                                        profilepic=Profilepic.objects.get(user=user)
                                        if plantype=='free':
                                                if (subscription is not None):
                                                        return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})
                                        else:
                                                expiry_date=date + timedelta(days=30)
                                                if (subscription is not None):
                                                        return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})    
                                except ObjectDoesNotExist:
                                        return render(request, 'farmerprofile_farmer.html', {'profile': profile,'profilepic':profilepic})
                        else:
                                return render(request, 'index.html') 
                else:
                        profilepic=request.FILES['profilepic']
                profile=Profilepic(profilepic=profilepic,user=user)
                profile.save() 
                file_name = profile.profilepic.name
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                with open(file_path, 'wb') as destination:
                        for chunk in profile.profilepic.chunks():
                                destination.write(chunk)  
                user_id = request.session.get('user_id')
                if user_id is not None:
                        profile = User.objects.get(id=user_id)
                        try:        
                                subscription=Subscription.objects.get(user=user_id)
                                plantype=subscription.planname
                                date=subscription.date
                                expiry_date=subscription.expiry_date
                                if plantype=='free':
                                        if (subscription is not None):
                                                return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})
                                else:
                                        expiry_date=date + timedelta(days=30)
                                        if (subscription is not None):
                                                return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})    
                        except ObjectDoesNotExist:
                         return render(request, 'farmerprofile_farmer.html', {'profile': profile,'profilepic':profilepic})
                else:
                        return render(request, 'index.html')                     

        except:                        
                print('hey')
                profilepic=request.FILES['profilepic']
                profile=Profilepic(profilepic=profilepic,user=user)
                profile.save() 
                file_name = profile.profilepic.name
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                with open(file_path, 'wb') as destination:
                        for chunk in profile.profilepic.chunks():
                                destination.write(chunk)  
                user_id = request.session.get('user_id')
                if user_id is not None:
                        profile = User.objects.get(id=user_id)
                        try:        
                                subscription=Subscription.objects.get(user=user_id)
                                plantype=subscription.planname
                                date=subscription.date
                                expiry_date=subscription.expiry_date
                                if plantype=='free':
                                        if (subscription is not None):
                                                return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})
                                else:
                                        expiry_date=date + timedelta(days=30)
                                        if (subscription is not None):
                                                return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'profilepic':profilepic})    
                        except ObjectDoesNotExist:
                         return render(request, 'farmerprofile_farmer.html', {'profile': profile,'profilepic':profilepic})
                else:
                        return render(request, 'index.html')        
        return render(request,'farmerprofile_farmer.html')


def changepassword(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        
        # Retrieve the hashed password from the database
        password_from_db = user.password
        
        if new_password == confirm_new_password:
                # Verify the current password
             if check_password(current_password, user.password):
                # Hash the new password before saving it
                hashed_password = make_password(new_password)
                user.password = hashed_password
                user.save()
                messages = 'Password successfully changed.'
                        
                
                # Handle subscription logic
                try:
                    subscription = Subscription.objects.get(user=user)
                    plantype = subscription.planname
                    date = subscription.date
                    expiry_date = subscription.expiry_date
                    
                    if plantype == 'free':
                        expiry_date = date + timedelta(days=30)
                    
                    return render(request, 'farmerprofile_farmer.html', {'profile': user, 'subscription': subscription, 'messages': messages})
                except ObjectDoesNotExist:
                    return render(request, 'farmerprofile_farmer.html', {'profile': user, 'messages': messages})
             else:
                messages = 'New password and confirm password do not match.'
        else:
            messages = 'Current password is incorrect.'
        return render(request, 'farmerprofile_farmer.html', {'profile': user, 'error_messages': messages})
    return render(request, 'farmerprofile_farmer.html')


def productprice(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name   
        user=User.objects.get(id=user_id)    
        products=Product.objects.filter(user=user)    
        return render(request, 'Productsprice_farmer.html', {'products': products,'user_name':user_name})
          


def productpriceadd(request):
    user_id = request.session.get('user_id')
    fruit_name = request.GET.get('fruit', '')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
        user_subscription = Subscription.objects.filter(user=user, planname='free').first()
        if user_subscription:
                has_added_product = Product.objects.filter(user=user).exists()                
                if has_added_product:
                        return render(request, 'cantaddProducts_farmer.html', {'fruit_name': fruit_name, 'user_name': user_name, 'error_message': 'You can add only one product with a free subscription.'})                
                current_date = datetime.now().date()
                expiry_date = user_subscription.date + timedelta(days=3)
                if current_date > expiry_date:
                        Product.objects.filter(user=user).delete()
                        return render(request, 'subscription_farmer.html')
        basic_subscription = Subscription.objects.filter(user=user, planname='basic').first()
        if basic_subscription:
            # Check if subscription has expired
            current_date = datetime.now().date()
            expiry_date = basic_subscription.date + timedelta(days=30)  # Assuming 1 month validity
            if current_date > expiry_date:
                # Subscription has expired, delete user's products
                Product.objects.filter(user=user).delete()
                return render(request, 'subscription_farmer.html', {'user_name': user_name})
            # User has an active subscription, check the number of products
            product_count = Product.objects.filter(user=user).count()
            if product_count >= 4:
                return render(request, 'cantaddProducts_farmer.html', {'fruit_name': fruit_name, 'user_name': user_name, 'error_message': 'You can add up to 4 products with a basic subscription.'})
        standard_subscription = Subscription.objects.filter(user=user, planname='standard').first()
        if standard_subscription:
            # Check if subscription has expired
            current_date = datetime.now().date()
            expiry_date = standard_subscription.date + timedelta(days=30)  # Assuming 1 month validity
            if current_date > expiry_date:
                # Subscription has expired, delete user's products
                Product.objects.filter(user=user).delete()
                return render(request, 'subscription_farmer.html', {'user_name': user_name})
            # User has an active subscription, check the number of products
            product_count = Product.objects.filter(user=user).count()
            if product_count >= 10:
                return render(request, 'cantaddProducts_farmer.html', {'fruit_name': fruit_name, 'user_name': user_name, 'error_message': 'You can add up to 4 products with a basic subscription.'})
        premium_subscription = Subscription.objects.filter(user=user, planname='premium').first()
        if premium_subscription:
            # Check if subscription has expired
            current_date = datetime.now().date()
            expiry_date = premium_subscription.date + timedelta(days=30)  # Assuming 1 month validity

            if current_date > expiry_date:
                # Subscription has expired, delete user's products
                Product.objects.filter(user=user).delete()
                return render(request, 'subscription_farmer.html', {'user_name': user_name})
        if user_id:
                user = User.objects.get(id=user_id)
                products = Product.objects.filter(user=user)
                return render(request, 'Productspriceadd_farmer.html', {'fruit_name': fruit_name,'products': products, 'user_name': user_name})





def productpriceadddone(request,product_name,product_type,quality,rate,quantity):
    user_id = request.session.get('user_id')
    fruit_name = request.GET.get('fruit', '')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
        user_subscription = Subscription.objects.filter(user=user, planname='free').first()
        if user_subscription:
                has_added_product = Product.objects.filter(user=user).exists()
                
                if has_added_product:
                        return render(request, 'cantaddProducts_farmer.html', {'fruit_name': fruit_name, 'user_name': user_name, 'error_message': 'You can add only one product with a free subscription.'})
                
                current_date = datetime.now().date()
                expiry_date = user_subscription.date + timedelta(days=3)
                if current_date > expiry_date:
                        Product.objects.filter(user=user).delete()
                        return render(request, 'subscription_farmer.html')
                
                if request.method == 'POST':
                        user_id = request.session.get('user_id')
                        if user_id:
                                user = User.objects.get(id=user_id)
                                product = Product.objects.create(user=user, product_name=product_name, product_type=product_type, quality=quality, rate=rate, quantity=quantity)
                                products = Product.objects.filter(user=user)
                                return render(request, 'Productsprice_farmer.html', {'products': products, 'user_name': user_name})
                        


        basic_subscription = Subscription.objects.filter(user=user, planname='basic').first()

        if basic_subscription:
            # Check if subscription has expired
            current_date = datetime.now().date()
            expiry_date = basic_subscription.date + timedelta(days=30)  # Assuming 1 month validity

            if current_date > expiry_date:
                # Subscription has expired, delete user's products
                Product.objects.filter(user=user).delete()
                return render(request, 'subscription_farmer.html', {'user_name': user_name})

            # User has an active subscription, check the number of products
            product_count = Product.objects.filter(user=user).count()

            if product_count >= 4:
                return render(request, 'cantaddProducts_farmer.html', {'fruit_name': fruit_name, 'user_name': user_name, 'error_message': 'You can add up to 4 products with a basic subscription.'})

            if request.method == 'POST':
                # Create the product
                product = Product.objects.create(user=user, product_name=product_name, product_type=product_type, quality=quality, rate=rate, quantity=quantity)

                # Redirect to 'Productsprice_farmer' after adding a product
                products = Product.objects.filter(user=user)
                return render(request, 'Productsprice_farmer.html', {'products': products, 'user_name': user_name})

        standard_subscription = Subscription.objects.filter(user=user, planname='standard').first()

        if standard_subscription:
            # Check if subscription has expired
            current_date = datetime.now().date()
            expiry_date = standard_subscription.date + timedelta(days=30)  # Assuming 1 month validity

            if current_date > expiry_date:
                # Subscription has expired, delete user's products
                Product.objects.filter(user=user).delete()
                return render(request, 'subscription_farmer.html', {'user_name': user_name})

            # User has an active subscription, check the number of products
            product_count = Product.objects.filter(user=user).count()

            if product_count >= 10:
                return render(request, 'cantaddProducts_farmer.html', {'fruit_name': fruit_name, 'user_name': user_name, 'error_message': 'You can add up to 4 products with a basic subscription.'})

            if request.method == 'POST':
                # Create the product
                product = Product.objects.create(user=user, product_name=product_name, product_type=product_type, quality=quality, rate=rate, quantity=quantity)

                # Redirect to 'Productsprice_farmer' after adding a product
                products = Product.objects.filter(user=user)
                return render(request, 'Productsprice_farmer.html', {'products': products, 'user_name': user_name})

        premium_subscription = Subscription.objects.filter(user=user, planname='premium').first()

        if premium_subscription:
            # Check if subscription has expired
            current_date = datetime.now().date()
            expiry_date = premium_subscription.date + timedelta(days=30)  # Assuming 1 month validity

            if current_date > expiry_date:
                # Subscription has expired, delete user's products
                Product.objects.filter(user=user).delete()
                return render(request, 'subscription_farmer.html', {'user_name': user_name})

        
            if request.method == 'POST':
                # Create the product
                product = Product.objects.create(user=user, product_name=product_name, product_type=product_type, quality=quality, rate=rate, quantity=quantity)

                # Redirect to 'Productsprice_farmer' after adding a product
                products = Product.objects.filter(user=user)
                return render(request, 'Productsprice_farmer.html', {'products': products, 'user_name': user_name})


        if user_id:
                user = User.objects.get(id=user_id)
                products = Product.objects.filter(user=user)
                return render(request, 'Productspriceadd_farmer.html', {'fruit_name': fruit_name,'products': products, 'user_name': user_name})



def productpriceedit(request):
        return render(request,'Productspriceedit_farmer.html')


def sales(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'sales_farmer.html',{'user_name':user_name})

def addsales(request):
        return render(request,'addsales_farmer.html')


def salescategorylist(request):
        return render(request,'salescategorylist_farmer.html')


def farmerbit(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            bit_data = Bit.objects.filter(farmer_id=user).values('id', 'product', 'bitter','farmer', 'product_type', 'quantity', 'rate', 'quality', 'bit_value', 'status')
            print('hey',bit_data)
            bit = {}
            for entry in bit_data:
                product_name = entry['product']
                if product_name not in bit or product_name in bit:
                        bit[product_name] = []
                        bit[product_name].append(entry)
            context = {
                        'bit': bit,
                        'bit_data':bit_data,
                        'user_name':user_name
                }
            return render(request,'farmerbit_farmer.html',context)
        except Bit.DoesNotExist:
            return render(request, 'error.html', {'message': 'Bit not found'})
        

def accept_bit(request, dealerbit_id):
    if request.method == 'POST':
        try:
                dealer_bit = Bit.objects.get(pk=dealerbit_id)
                farmer_bit = dealer_bit.status
                product_bit= dealer_bit.product
                dealer_bit.status = True
                dealer_bit.save()
                other_bits = Bit.objects.filter(status=farmer_bit,product=product_bit).exclude(pk=dealerbit_id)
                other_bits.delete()

                user_id = request.session.get('user_id')
                if user_id:
                        user = User.objects.get(pk=user_id)
                        user_name = user.name
                if user_id:
                        try:
                                user = User.objects.get(id=user_id)
                                bit_data = Bit.objects.filter(bitter=user).values('id', 'product', 'bitter','farmer', 'product_type', 'quantity', 'rate', 'quality', 'bit_value', 'status')
                                print(bit_data)
                                bit = {}
                                for entry in bit_data:
                                        product_name = entry['product']
                                        if product_name not in bit or product_name in bit:
                                                bit[product_name] = []
                                                bit[product_name].append(entry)
                                context = {
                                                'bit': bit,
                                                'bit_data':bit_data,
                                                'user_name':user_name
                                        }
                                return render(request,'farmerbit_farmer.html',context)
                        except Bit.DoesNotExist:
                                return render(request, 'error.html', {'message': 'Bit not found'})  
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def subscription(request):
        try:
                user=request.session.get('user_id')
                sub=Subscription.objects.get(user=user)
                print(sub)
                if(sub.user):
                        user_id = request.session.get('user_id')
                        if user_id is not None:
                                profile = User.objects.get(id=user_id)
                                subscription=Subscription.objects.get(user=user_id)
                                date=subscription.date
                                expiry_date=date + timedelta(days=3)
                                if (subscription is not None):
                                        return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'expiry_date':expiry_date})
                                
        except ObjectDoesNotExist:
                user_id=request.session.get('user_id')
                user=User.objects.get(id=user_id)
                name=user.name
                return render(request,'subscription_farmer.html',{'name':name})



def freeplan(request):          
        user=request.session.get('user_id')
        planname='free'
        amount=0
        date=datetime.now().date()
        existing_subscription = Subscription.objects.filter(user_id=user, planname=planname).first()

        if not existing_subscription:
                current_date = datetime.now().date()
                expiry_date = current_date + timedelta(days=3)  
                new_subscription = Subscription(planname=planname, user_id=user, amount=amount, date=date,expiry_date=expiry_date)
                new_subscription.save()
        else:
                pass
        if user is not None:
                profile = User.objects.get(id=user)
                try:        
                        subscription=Subscription.objects.get(user=user)
                        date=subscription.date
                        expiry_date=date + timedelta(days=3)
                        if expiry_date < datetime.now().date():
                                return render(request,'subscription_farmer.html')
                        if (subscription is not None):
                                return render(request, 'farmerprofile_farmer.html', {'profile': profile,'subscription':subscription,'expiry_date':expiry_date})
                except ObjectDoesNotExist:
                       return render(request, 'subscription_farmer.html')



def basicplan(request,amount):        
        print((amount))
        client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
        payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
        print(payment)
        order_id=payment['id']
        order_status=payment['status']
        #if order_status=='created':
        return render(request,'basicplan_farmer.html',{'payment':payment})

def standardplan(request,amount):        
        print((amount))
        client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
        payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
        print(payment)
        order_id=payment['id']
        order_status=payment['status']
        #if order_status=='created':
        return render(request,'standardplan_farmer.html',{'payment':payment})         

def premiumplan(request,amount):        
        print((amount))
        client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
        payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
        print(payment)
        order_id=payment['id']
        order_status=payment['status']
        #if order_status=='created':
        return render(request,'premiumplan_farmer.html',{'payment':payment})


def success(request):
    id=request.GET.get(id)
    subs=Subscription.objects.get(razor_pay_order_id=id)
    subs.is_paid=True
    subs.save()
    return HttpResponse('Payment Success')


def farmeragreement(request):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        if request.method=="POST":
                product_name=request.POST['product_name']
                product_type=request.POST['product_type']
                rate=request.POST['rate']
                quantity=request.POST['quantity']
                quality=request.POST['quality']
                context = {
                        'product_name': product_name,
                        'product_type': product_type,
                        'rate': rate,
                        'quantity': quantity,
                        'quality': quality,
                        'user_name':user_name,
                            }
                return render(request,'agreement_farmer.html',context)
        return render(request,'agreement_farmer.html',{'user_name':user_name})


def farmeragreementdone(request):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        if request.method=="POST":
                agree=Agreement(user=user,agree=True) 
                agree.save()       
                return render(request,'sales_farmer.html',{'user_name':user_name})        
        return render(request,'agreement_farmer.html',{'user_name':user_name})




# from django.shortcuts import render, HttpResponseRedirect
# from django.shortcuts import render, HttpResponse
# from farmer.models import Farm
# import json

# def add_farmer(request):
#         if request.method == "POST":
#                 user_id=request.session.get('user_id')
#                 user=User.objects.get(id=user_id)
                
#                 latitude = request.POST.get('latitude')
#                 longitude = request.POST.get('longitude')
#                 description = request.POST.get('description')
#                 video_url = request.POST.get('video_url')
#                 farm=Farm(user=user,latitude=latitude,longitude=longitude,description=description,video_url=video_url)
#                 farm.save()
#                 return render(request, 'myfarm.html')
#         return render(request, 'create_farm.html')



# def farm_view(request):
#     """
#     Handles requests to view a farm's details and potentially display the farm's live stream.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         HttpResponse: The response to be sent to the client.
#     """

#     user_id = request.session.get('user_id')
#     farm = Farm.objects.filter(name=user_id).first()

#     if not farm:
#         print(farm)
#         return HttpResponse('Farm not found', status=404)

#     # **Simulate retrieving stream URL from an external service (replace with actual logic)**
#     stream_url = "https://www.example.com/live-stream/farm-{farm_id}".format(farm_id=farm.id)

#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         return HttpResponse(json.dumps({'stream_url': stream_url}), content_type='application/json')

#     # **Replace dummy latitude and longitude with actual values or remove them if not used**
#     farm.latitude = -25.7956  # Dummy latitude (replace with actual value if needed)
#     farm.longitude = 28.2189  # Dummy longitude (replace with actual value if needed)

#     return render(request, 'myfarm.html', {'farm': farm})


# from django.http import HttpResponse
# import requests  # Assuming you're using requests for API calls (replace with appropriate library)

# # # Replace with your actual API endpoint URL and authentication details
# # API_ENDPOINT_URL = "https://your-api-endpoint.com/farm/{farm_id}/stream_url"
# # API_KEY = "your_api_key"  # Replace with your actual API key

# def farm_stream(request, pk):
#     farm = Farm.objects.filter(id=pk, owner=request.user).first()  # Fetch farm owned by the user
#     if not farm:
#         return HttpResponse('Farm not found or not owned by you', status=404)

#     # Retrieve stream URL from external service using API
#     try:
#         response = requests.get(API_ENDPOINT_URL.format(farm_id=farm.id), headers={'Authorization': f'Bearer {API_KEY}'})
#         response.raise_for_status()  # Raise an exception for non-200 status codes
#         stream_url = response.json()['stream_url']
#     except requests.exceptions.RequestException as e:
#         print(f"Error retrieving stream URL: {e}")
#         return HttpResponse('Failed to retrieve stream URL', status=500)

#     return HttpResponse(json.dumps({'stream_url': stream_url}), content_type='application/json')


def buy(request):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        return render(request,'buy_farmer.html',{'user_name':user_name})

def productlists(request,producttype):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        products=Products.objects.filter(producttype=producttype)        
        return render(request,'productslist_farmer.html',{'user_name':user_name,'products':products})

def bit(request,productname,img1,img2,img3,producttype,price,quantity):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        context={
                'productname':productname,
                'img1':img1,
                'img2':img2,
                'img3':img3,
                'producttype':producttype,
                'price':price,
                'quantity':quantity,
                'user_name':user_name
        }
        return render(request,'bit_farmer.html',context)

def renterslist(request):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        renters=Renter.objects.exclude(user=user)        
        return render(request,'rentlist_farmer.html',{'user_name':user_name,'renters':renters})

def rent(request):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name
        if request.method=="POST":
               city=request.POST['city']
               location=request.POST['location']
               rent=request.POST['rent'] 
               duration=request.POST['duration']
               img1=request.POST['img1']
               img2=request.POST['img2']
               img3=request.POST['img3'] 
               rent=Renter(user=user,city=city,img1=img1,img2=img2,img3=img3,location=location,rent=rent,duration=duration)
               rent.save()
               file_paths = [] 
               for img in [img1, img2, img3]:
                        file_name = img.name 
                        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                        file_paths.append(file_path)  
                        with open(file_path, 'wb') as destination:
                                for chunk in img.chunks():
                                        destination.write(chunk)       
        return render(request,'rent_farmer.html',{'user_name':user_name})

