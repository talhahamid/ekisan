from django.shortcuts import render,redirect
from accounts.models import User,Subscription,Profilepic
from seller.models import Products
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.contrib import messages
import os
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password


# Create your views here.


def sellerprofile(request):
        user_id = request.session.get('user_id')
        if user_id is not None:
                profile = User.objects.get(id=user_id)
                profilepic = None
                return render(request, 'sellerprofile_seller.html', {'profile': profile,'profilepic':profilepic})    
        else:
            return render(request, 'sellerprofile_seller.html')
        
def editsellerprofile(request,id):
       seller=User.objects.get(id=id)
       return render(request,'editsellerprofile_seller.html',{'seller':seller})       

def updatesellerprofile(request,id):
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
                        return render(request, 'sellerprofile_seller.html', {'profile': profile})
              else:
                        return render(request, 'index.html')       
       return redirect(('sellerprofile')) 


def sellerprofilepic(request):
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
                                return render(request, 'sellerprofile_seller.html', {'profile': profile,'profilepic':profilepic})
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
                        return render(request, 'sellerprofile_seller.html', {'profile': profile,'profilepic':profilepic})
                else:
                        return render(request, 'index.html')                     

        except:                        
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
                        return render(request, 'sellerprofile_seller.html', {'profile': profile,'profilepic':profilepic})
                else:
                        return render(request, 'index.html')        
        return render(request,'sellerprofile_seller.html')


def changepassword(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        password_from_db = user.password
        if new_password == confirm_new_password:
             if check_password(current_password, user.password):
                hashed_password = make_password(new_password)
                user.password = hashed_password
                user.save()
                messages = 'Password successfully changed.'
             else:
                messages = 'New password and confirm password do not match.'
        else:
            messages = 'Current password is incorrect.'
        return render(request, 'sellerprofile_seller.html', {'profile': user, 'error_messages': messages})
    return render(request, 'sellerprofile_seller.html')


def sellersales(request):
       return render(request,'sales_seller.html')

def selleragreement(request):
       if request.method=="POST":
              product_name=request.POST['product_name']
              product_type=request.POST['product_type']
              price=request.POST['price']
              quantity=request.POST['quantity']
              img1=request.FILES['img1']
              img2=request.FILES['img2']
              img3=request.FILES['img3']
              context={
                  'product_name':product_name,
                  'product_type':product_type,
                  'price':price,
                  'quantity':quantity,
                  'img1':img1,
                  'img2':img2,
                  'img3':img3,              
              }
       return render(request,'agreement_seller.html',context)

def productsadd(request,producttype):
       return render(request,'productsadd_seller.html',{'producttype':producttype})

def productsadded(request,productname,producttype,price,quantity,img1,img2,img3):
        products=Products(productname=productname,producttype=producttype,price=price,quantity=quantity,img1=img1,img2=img2,img3=img3)
        products.save()
        file_paths = [] 
        for img in [img1, img2, img3]:
                file_name = img.name 
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                file_paths.append(file_path)  
                with open(file_path, 'wb') as destination:
                        for chunk in img.chunks():
                                destination.write(chunk)                      
        return render(request,'productsadd_seller.html')
        
def productprice(request):
        user_id = request.session.get('user_id')
        if user_id:
                user = User.objects.get(pk=user_id)
                user_name = user.name   
        user=User.objects.get(id=user_id)    
        products=Products.objects.filter(user=user)    
        return render(request, 'productprice_seller.html', {'products': products,'user_name':user_name})



def sellerbit(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        user_name = user.name
    if user_id:
        #try:
        #     user = User.objects.get(id=user_id)
        #     bit_data = SellerBit.objects.filter(farmer_id=user).values('id', 'product', 'bitter','farmer', 'product_type', 'quantity', 'rate', 'quality', 'bit_value', 'status')
        #     print('hey',bit_data)
        #     bit = {}
        #     for entry in bit_data:
        #         product_name = entry['product']
        #         if product_name not in bit or product_name in bit:
        #                 bit[product_name] = []
        #                 bit[product_name].append(entry)
        #     context = {
        #                 'bit': bit,
        #                 'bit_data':bit_data,
        #                 'user_name':user_name
        #         }
            return render(request,'sellerbit_seller.html')#,context)
        # except SellerBit.DoesNotExist:
            return render(request, 'error.html', {'message': 'Bit not found'})

