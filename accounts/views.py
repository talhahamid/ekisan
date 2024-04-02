from django.shortcuts import render,redirect
from .models import User
from farmer.models import Product,Message
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout as django_logout
from django.db.models import Count
from django.db.models import Sum
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Create your views here.
def home(request):
    farmers = User.objects.filter(role='Farmer').count()
    dealers = User.objects.filter(role='Dealer').count()
    products_info = Product.objects.values('product_name').annotate(total_quantity=Sum('quantity'), total_rate=Sum('rate'))
    total_messages = Message.objects.count()
    latest_messages = Message.objects.all()[max(total_messages - 3, 0):]
    return render(request, 'home_accounts.html',{'farmers':farmers,'dealers':dealers,'products_info':products_info,'latest_messages': latest_messages})


def forget(request):
    if request.method=="POST":
        email=request.POST['email']
        try:
            user=User.objects.get(email=email)        
        except User.DoesNotExist:

            return render(request, 'forget_accounts.html', {'error': 'User with this email does not exist.'})

        password=user.password
        name=user.name

        subject = 'We are from E-Kisan!'
        message = f'Dear {name} your password is {password} .'

        from_email = 'talhahamid.syed@gmail.com' 
        to_email = [email]

        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return redirect('employee')  
    return render(request, 'forget_accounts.html')


def index(request):
    if request.method == "POST":
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        user = User.objects.filter(mobile=mobile).first()
        if user is not None:
            if check_password(password, user.password):
                if user is not None:    
                    if user.role == 'Farmer':
                        # Add user to session and redirect
                        request.session['user_id'] = user.id
                        request.session['user_role'] = 'Farmer'
                        return redirect('/farmer/subscription/')
                    elif user.role == 'Dealer':
                        # Add user to session and redirect
                        request.session['user_id'] = user.id
                        request.session['user_role'] = 'Dealer'
                        return redirect('/dealer/subscription/')
                    elif user.role == 'Seller':
                        # Add user to session and redirect
                        request.session['user_id'] = user.id
                        request.session['user_role'] = 'Seller'
                        return redirect('/seller/')
                    elif user.role == 'Delivery Man':
                        # Add user to session and redirect
                        request.session['user_id'] = user.id
                        request.session['user_role'] = 'Delivery Man'
                        return redirect('/deliveryman/')
                    else:
                        return render(request, 'home_accounts.html')
                else:
                    return render(request, 'index_accounts.html')

    return render(request, 'index_accounts.html')    
                    
        


def password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
            password = user.password  # Assuming the password field in UserProfile model is named 'password'
            recipient_email = user.email
            send_mail(
                'Password Recovery',
                f'Your password is: {password}',
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                fail_silently=False,
            )
            return render(request,'password_accounts.html')
        except User.DoesNotExist:
            messages.error(request, 'No user account exists with the provided email.')
        return redirect('password')
    return render(request, 'password_accounts.html')

def otp(request):
    return render(request, 'otp_accounts.html')

def register(request):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        state=request.POST['state']
        city=request.POST['city']
        pincode=request.POST['pincode']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST['role']
        valid_roles = ['Farmer', 'Dealer','Delivery Man']  
        if role not in valid_roles:
            return render(request, 'register_accounts.html', {'error_message': 'Invalid role'})
        
        hashed_password = make_password(password)
        user = User(name=name,address=address,state=state,city=city,pincode=pincode,mobile=mobile,password=hashed_password ,email=email,role=role)
        user.save()
        return redirect('/index/')
    return render(request, 'register_accounts.html')




def logout(request):
    django_logout(request)
    request.session.flush()
    farmers = User.objects.filter(role='Farmer').count()
    dealers = User.objects.filter(role='Dealer').count()
    products_info = Product.objects.values('product_name').annotate(total_quantity=Sum('quantity'), total_rate=Sum('rate'))
    total_messages = Message.objects.count()
    latest_messages = Message.objects.all()[max(total_messages - 3, 0):]
    return render(request, 'home_accounts.html',{'farmers':farmers,'dealers':dealers,'products_info':products_info,'latest_messages': latest_messages})

