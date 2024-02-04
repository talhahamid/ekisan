from django.shortcuts import redirect,render
from accounts.models import User
from datetime import datetime, timedelta
from accounts.models import User,Subscription

class AuthMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get('user_id')
        if user_id == None and 'accounts' in request.path:
            return render(request,'index_accounts.html')
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                role = user.role
                if user_id != None and role =='Dealer' and 'farmer' in request.path:
                     return render(request, 'accessdenied.html')
                current_date = datetime.now().date()
                subs=Subscription.objects.get(user_id=user_id)
                expiry_date=subs.expiry_date
                print(expiry_date)
                if expiry_date>current_date:
                    return render(request,'accessdenied.html')
            except User.DoesNotExist:
                pass   
        response = self.get_response(request)
        return response

