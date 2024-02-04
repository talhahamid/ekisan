from django.shortcuts import render,redirect
from accounts.models import User,Subscription
from .models import Product
from dealer.models import Bit
from django.urls import reverse 
from django.http import JsonResponse,HttpResponse
import razorpay
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta

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

def farmerprofile(request):
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

def calculations(request):
        return render(request,'calculations_farmer.html')

def calculationsadd(request):
        return render(request,'calculationsadd_farmer.html')

def calculationsedit(request):
        return render(request,'calculationsedit_farmer.html')

def dealerslist(request):
        return render(request,'dealerslist_farmer.html')

def dealersadd(request):
        return render(request,'dealersadd_farmer.html')

def dealersedit(request):
        return render(request,'dealersedit_farmer.html')

def renterslist(request):
        return render(request,'renterslist_farmer.html')


def rentersadd(request):
        return render(request,'rentersadd_farmer.html')


def rentersedit(request):
        return render(request,'rentersedit_farmer.html')


def resourceslist(request):
        return render(request,'resourceslist_farmer.html')


def resourcesadd(request):
        return render(request,'addresources_farmer.html')


def resourcesedit(request):
        return render(request,'resourcesedit_farmer.html')


def fertilizersform(request):
        return render(request,'fertilizersform_farmer.html')

def oxdetails(request):
        return render(request,'oxdetails_farmer.html')

def patriform(request):
        return render(request,'patriform_farmer.html')


def pesticidesform(request):
        return render(request,'pesticidesform_farmer.html')


def pesticideslist(request):
        return render(request,'pesticideslist_farmer.html')


def productprice(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            products = Product.objects.filter(user_id=user_id)
            return render(request, 'Productsprice_farmer.html', {'products': products,'user_name':user_name})
        except User.DoesNotExist:
            return render(request, 'error.html', {'message': 'User not found'})


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
                
                if request.method == 'POST':
                        product_name = request.POST.get('product_name')
                        product_type = request.POST.get('product_type')
                        quality = request.POST.get('quality')
                        rate = request.POST.get('rate')
                        quantity = request.POST.get('quantity')
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
                product_name = request.POST.get('product_name')
                product_type = request.POST.get('product_type')
                quality = request.POST.get('quality')
                rate = request.POST.get('rate')
                quantity = request.POST.get('quantity')

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
                product_name = request.POST.get('product_name')
                product_type = request.POST.get('product_type')
                quality = request.POST.get('quality')
                rate = request.POST.get('rate')
                quantity = request.POST.get('quantity')

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
                product_name = request.POST.get('product_name')
                product_type = request.POST.get('product_type')
                quality = request.POST.get('quality')
                rate = request.POST.get('rate')
                quantity = request.POST.get('quantity')

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


def addsalescategory(request):
        return render(request,'addsalescategory_farmer.html')

def categorylist(request):
        return render(request,'categorylist_farmer.html')


def seedsform(request):
        return render(request,'seedsform_farmer.html')


def seedslist(request):
        return render(request,'seedslist_farmer.html')

def vehiclesform(request):
        return render(request,'vehiclesform_farmer.html')


def workersform(request):
        return render(request,'workersform_farmer.html')

def animalsform(request):
        return render(request,'animalsform_farmer.html')

def transactions(request):
        return render(request,'transactions_farmer.html')

def farmerbit(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            bit_data = Bit.objects.filter(farmer=user).values('id', 'product', 'bitter','farmer', 'product_type', 'quantity', 'rate', 'quality', 'bit_value', 'status')
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
                return render(request,'subscription_farmer.html')



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