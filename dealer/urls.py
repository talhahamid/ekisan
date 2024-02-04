from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dealers,name="dealers"),

    path('addbuy/',views.addbuy,name="addbuy"),  
    path('buy/',views.buy,name="buy"),      

    path('dealersprofile/',views.dealersprofile,name="dealersprofile"),

    path('delivery/',views.delivery,name="delivery"),
    # path('deliverymenadd/',views.deliverymenadd,name="deliverymenadd"),
    # path('deliverymenedit/',views.deliverymenedit,name="deliverymenedit"),

    path('farmerslist/',views.farmerslist,name="farmerslist"),
    path('farmersadd/',views.farmersadd,name="farmersadd"),
    path('farmersedit/',views.farmersedit,name="farmersedit"),

    path('productcategory/',views.productcategory,name="productcategory"),
    path('productcategorylist/',views.productcategorylist,name="productcategorylist"), 

    path('productlist/<str:fruit>',views.productlist,name="productlist"),

    path('transactions/',views.transactions,name="transactions"),

    path('buyvegetables/',views.buyvegetables,name="buyvegetables"),
    path('fruits/',views.fruits,name="fruits"),
    path('crops/',views.crops,name="crops"),

    path('bit/<str:user_name>/<str:product_name>/<str:product_type>/<str:quality>/<str:rate>/<str:quantity>/',views.bit,name="bit"),
    path('process_bit/', views.process_bit, name='process_bit'),

    path('mybits/', views.mybits, name='mybits'),

    path('get_notifications/', views.get_notifications, name='get_notifications'),

    path('subscription/',views.subscription,name="subscription"),
    path('freeplan/',views.freeplan,name="freeplan"),
    path('basicplan/<int:amount>',views.basicplan,name="basicplan"),
    path('standardplan/<int:amount>',views.standardplan,name="standardplan"),
    path('premiumplan/<int:amount>',views.premiumplan,name="premiumplan"),
    path('success/',views.success,name="success"),

    path('pay/<int:amount>/<str:name>/<str:quantity>',views.pay,name="pay")

]