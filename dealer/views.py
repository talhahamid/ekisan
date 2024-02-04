from django.shortcuts import render,redirect
from accounts.models import User,Subscription
from farmer.models import Product,Tracking
from django.shortcuts import render, get_list_or_404
from dealer.models import Bit
from django.http import JsonResponse,HttpResponse
from farmer.models import Message
import razorpay
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
# Create your views here.


def buy(request):
    user_id = request.session.get('user_id')

    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name

        # Check user's subscription
        user_subscription = Subscription.objects.filter(user=user).first()
        if user_subscription:
                has_added_product = Bit.objects.filter(bitter=user_name).exists()
                
                if has_added_product:
                        return render(request, 'cantBuy_dealer.html', {'user_name': user_name, 'error_message': 'You can buy only one product with a free subscription.'})
                
                current_date = datetime.now().date()
                expiry_date = user_subscription.date + timedelta(days=3)
                if current_date > expiry_date:
                        Product.objects.filter(user=user).delete()
                        return render(request, 'subscription_dealer.html')

                return render(request,'buy_dealer.html',{'user_name':user_name})
        
        elif user_subscription.planname == 'basic':
                # For basic subscription, dealer can buy only 4 products and they expire after 30 days
                
                product_count = Bit.objects.filter(bitter=user_name).count()
                if product_count >= 4:
                        return render(request, 'cantBuy_dealer.html', {'user_name': user_name, 'error_message': 'You can buy only 4 products with a basic subscription.'})
                
                current_date = datetime.now().date()
                expiry_date = user_subscription.date + timedelta(days=30)
                if current_date > expiry_date:
                        Product.objects.filter(user=user).delete()
                        return render(request, 'subscription_dealer.html')

                return render(request,'buy_dealer.html',{'user_name':user_name})

        elif user_subscription.planname == 'standard':
                
                product_count = Bit.objects.filter(bitter=user_name).count()
                if product_count >= 10:
                        return render(request, 'cantBuy_dealer.html', {'user_name': user_name, 'error_message': 'You can buy only 10 products with a basic subscription.'})
                
                current_date = datetime.now().date()
                expiry_date = user_subscription.date + timedelta(days=30)
                if current_date > expiry_date:
                        Product.objects.filter(user=user).delete()
                        return render(request, 'subscription_dealer.html')

                return render(request,'buy_dealer.html',{'user_name':user_name})

        elif user_subscription.planname == 'premium':
                
                current_date = datetime.now().date()
                expiry_date = user_subscription.date + timedelta(days=30)
                if current_date > expiry_date:
                        Product.objects.filter(user=user).delete()
                        return render(request, 'subscription_dealer.html')

                return render(request,'buy_dealer.html',{'user_name':user_name})

                 
    # Handle the case where user_id is None
    user_id = request.session.get('user_id')
    if user_id is not None:
        profile = User.objects.get(id=user_id)
        try:        
                subscription=Subscription.objects.get(user=user_id)
                plantype=subscription.planname
                date=subscription.date
                if plantype=='free':
                    expiry_date=date + timedelta(days=3)
                    if (subscription is not None):
                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'expiry_date':expiry_date})
                else:
                    expiry_date=date + timedelta(days=30)
                    if (subscription is not None):
                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'expiry_date':expiry_date})    
        except ObjectDoesNotExist:
                return render(request, 'dealerprofile_dealer.html', {'profile': profile})



def addbuy(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    return render(request, 'addbuy_dealer.html',{'user_name':user_name})

def buyvegetables(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    return render(request,'buyvegetables_dealer.html',{'user_name':user_name}) 

def fruits(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    return render(request,'fruits_dealer.html',{'user_name':user_name}) 

def crops(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name    
    return render(request,'crops_dealer.html',{'user_name':user_name}) 

def dealers(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    farmers = User.objects.filter(role='Farmer')
    return render(request, 'dealers_dealer.html', {'farmers': farmers,'user_name':user_name})

def dealersprofile(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        profile = User.objects.get(id=user_id)
        try:        
                subscription=Subscription.objects.get(user=user_id)
                plantype=subscription.planname
                if plantype=='free':
                    if (subscription is not None):
                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription})
                else:
                    if (subscription is not None):
                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription})    
        except ObjectDoesNotExist:
                return render(request, 'dealerprofile_dealer.html', {'profile': profile})
    else:
        return render(request, 'index.html')

def delivery(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        profile = User.objects.get(id=user_id)
        user_name=profile.name
    if user_id:    
        bits = Bit.objects.filter(bitter=user_name)
        if bits.exists():
            first_bit = bits.first()
            farmer = first_bit.farmer
        else:
            farmer = None
        farmer= User.objects.get(name=farmer)
        user_id=farmer.id
        product=Product.objects.get(user_id=user_id)
        quantity=product.quantity
        bit = Bit.objects.get(bitter=user_name)
        name=bit.product
        amount=bit.bit_value
        amount=int(amount)
        client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
        payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
        charge=float(amount)*0.05
        quantity_numeric =  quantity
        yourAmount=amount
        amount=amount*quantity_numeric
        charge=charge*quantity_numeric
        user_id=request.session.get('user_id')
        user=User.objects.get(id=user_id)
        address=user.address
        user_name = user.name
        paymentAmount=int(yourAmount)*int(quantity_numeric)
        delivery_charge=float(yourAmount)*0.10*float(quantity_numeric)
        total=float(paymentAmount)+float(charge)+float(delivery_charge)
        pay=total*100
        return render(request,'delivery_dealer.html',{'total':total,'pay':pay,'amount':amount,'quantity':quantity,'yourAmount':yourAmount,'paymentAmount':paymentAmount,'delivery_charge':delivery_charge,'charge':charge,'name':name,'address':address,'user_name':user_name})
    return render(request, 'delivery_dealer.html')


def deliverymenadd(request):
    return render(request, 'deliverymenadd_dealer.html')

def deliverymenedit(request):
    return render(request, 'deliverymenedit_dealer.html')

def farmerslist(request):
    return render(request, 'farmerslist_dealer.html')

def farmersadd(request):
    return render(request, 'farmersadd_dealer.html')    
    
def farmersedit(request):
    return render(request, 'farmersedit_dealer.html') 

def productcategory(request):
    return render(request, 'productcategory_dealer.html')

def productcategorylist(request):
    return render(request, 'productcategorylist_dealer.html')
   
def productlist(request,fruit):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    fruit_data = get_list_or_404(Product, product_name=fruit)
    return render(request, 'productlist_dealer.html', {'fruit_data': fruit_data, 'fruit': fruit,'user_name':user_name})

def transactions(request):
    return render(request, 'transactionsdealer_dealer.html')    

def bit(request, user_name, product_name, product_type, quality, rate, quantity):
     context = {
        'user_name': user_name,
        'product_name': product_name,
        'product_type': product_type,
        'quality': quality,
        'rate': rate,
        'quantity': quantity,
    }
     return render(request,'bit_dealer.html',context)

def process_bit(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
        bitter_address=user.address
    if request.method == 'POST':
        farmer = request.POST.get('farmer')
        product = request.POST.get('product')
        product_type = request.POST.get('product_type')
        quality = request.POST.get('quality')
        rate = request.POST.get('rate')
        quantity = request.POST.get('quantity')
        bit_value = request.POST.get('bit')
        status = False
        farmer=User.objects.get(name=farmer)
        farmer_address=farmer.address
        Bit.objects.create(
            farmer=farmer,
            product=product,
            product_type=product_type,
            quality=quality,
            rate=rate,
            quantity=quantity,
            bit_value=bit_value,
            bitter=user_name,
            status=status,
            bitter_address=bitter_address,
            farmer_address=farmer_address
        )

    return render(request,'buy_dealer.html')


def mybits(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            bit_data = Bit.objects.filter(bitter=user).values('product','farmer', 'product_type', 'quantity', 'rate', 'quality', 'bit_value')
            print('het',bit_data)
            bit = {}
            for entry in bit_data:
                product_name = entry['product']
                if product_name not in bit or product_name in bit:
                        bit[product_name] = []
                        bit[product_name].append(entry)
            
            notifications = Message.objects.filter(user=user)

            context = {
                        'bit': bit,
                        'bit_data':bit_data,
                        'user_name':user_name,
                        'notifications':notifications
                }
            return render(request,'mybits_dealer.html',context)
        except Bit.DoesNotExist:
                return render(request, 'error.html', {'message': 'Bit not found'})
        

def get_notifications(request):
    user_id = request.session.get('user_id')
    user=User.objects.get(id=user_id)
    if user_id:
        user_notifications = Message.objects.filter(user=user.name).values('notification','product')
        notifications = [{'notification': notification['notification'], 'product': notification['product']} for notification in user_notifications]
        bit_value=Bit.objects.get(bitter=user.name)
        quantity=(bit_value.quantity)
        return JsonResponse({'notifications': notifications, 'bit_value': bit_value.bit_value,'quantity':quantity})
    return JsonResponse({'notifications': [], 'bit_value': None})


def pay(request,amount,name,quantity):
    charge=amount*0.05
    quantity_numeric = float(''.join(filter(str.isdigit, quantity)))
    yourAmount=amount
    amount=amount*quantity_numeric
    charge=charge*quantity_numeric
    client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
    payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    address=user.address
    user_name = user.name
    paymentAmount=amount*quantity_numeric
    delivery_charge=yourAmount*0.10*quantity_numeric
    total=amount+charge+delivery_charge
    pay=total*100
    return render(request,'pay_dealer.html',{'total':total,'pay':pay,'amount':amount,'quantity':quantity,'yourAmount':yourAmount,'paymentAmount':paymentAmount,'delivery_charge':delivery_charge,'charge':charge,'name':name,'address':address,'user_name':user_name})


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
                                        return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'expiry_date':expiry_date})
                                
        except ObjectDoesNotExist:
                return render(request,'subscription_dealer.html')



def freeplan(request):          
        user=request.session.get('user_id')
        planname='free'
        amount=0
        date=datetime.now().date()
        existing_subscription = Subscription.objects.filter(user_id=user, planname=planname).first()

        if not existing_subscription:
                new_subscription = Subscription(planname=planname, user_id=user, amount=amount, date=date)
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
                                return render(request,'subscription_dealer.html')
                        if (subscription is not None):
                                return render(request, 'dealerprofile_dealer.html', {'profile': profile,'subscription':subscription,'expiry_date':expiry_date})
                except ObjectDoesNotExist:
                       return render(request, 'subscription_dealer.html')



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
        return render(request,'standardplan_dealer.html',{'payment':payment})         

def premiumplan(request,amount):        
        print((amount))
        client = razorpay.Client(auth=('rzp_test_bX75Gd98qBwkpY', 'dqDmwLhAXqBPTz1okdtBUHMJ'))
        payment = client.order.create({'amount':(amount)*100,'currency':"INR",'payment_capture':'1'})
        print(payment)
        order_id=payment['id']
        order_status=payment['status']
        #if order_status=='created':
        return render(request,'premiumplan_dealer.html',{'payment':payment})


def success(request):
    id=request.GET.get(id)
    subs=Subscription.objects.get(razor_pay_order_id=id)
    subs.is_paid=True
    subs.save()
    return HttpResponse('Payment Success')