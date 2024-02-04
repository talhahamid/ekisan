from django.contrib import admin
from django.urls import path
from . import views

app_name = 'farmer'

urlpatterns = [
    path('',views.farmer,name="farmer"),

    path('farmerprofile/',views.farmerprofile,name="farmerprofile"),

    path('calculations/',views.calculations,name="calculations"),
    path('calculationsadd/',views.calculationsadd,name="calculationsadd"),
    path('calculationsedit/',views.calculationsedit,name="calculationsedit"),

    path('dealerslist/',views.dealerslist,name="dealerslist"),
    path('dealersadd/',views.dealersadd,name="dealersadd"),
    path('dealersedit/',views.dealersedit,name="dealersedit"),

    path('renterslist/',views.renterslist,name="renterslist"),
    path('rentersadd/',views.rentersadd,name="rentersadd"),
    path('rentersedit/',views.rentersedit,name="rentersedit"),

    path('resourceslist/',views.resourceslist,name="resourceslist"),
    path('resourcesadd/',views.resourcesadd,name="resourcesadd"),
    path('resourcesedit/',views.resourcesedit,name="resourcesedit"),
    
    path('transactions/',views.transactions,name="transactions"),

    path('fertilizersform/',views.fertilizersform,name="fertilizersform"),

    path('oxdetails/',views.oxdetails,name="oxdetails"),

    path('patriform/',views.patriform,name="patriform"),

    path('pesticidesform/',views.pesticidesform,name="pesticidesform"),
    path('pesticideslist/',views.pesticideslist,name="pesticideslist"),

    path('productprice/',views.productprice,name="productprice"),
    path('productpriceadd/',views.productpriceadd,name="productpriceadd"),
    path('productpriceedit/',views.productpriceedit,name="productpriceedit"),

    path('sales/',views.sales,name="sales"),
    path('addsales/',views.addsales,name="addsales"),

    path('categorylist/',views.categorylist,name="categorylist"),
    path('salescategorylist/',views.salescategorylist,name="salescategorylist"),
    path('addsalescategory/',views.addsalescategory,name="addsalescategory"),

    path('seedsform/',views.seedsform,name="seedsform"),
    path('seedslist/',views.seedslist,name="seedslist"),

    path('vehiclesform/',views.vehiclesform,name="vehiclesform"),

    path('workersform/',views.workersform,name="workersform"),

    path('animalsform/',views.animalsform,name="animalsform"),

    
    path('vegitables/',views.vegitables,name="vegitables"),
    path('fruits/',views.fruits,name="fruits"),
    path('crops/',views.crops,name="crops"),

    path('farmerbit/',views.farmerbit,name="farmerbit"),
    
    path('accept_bit/<int:dealerbit_id>/',views.accept_bit,name="accept_bit"),

    path('subscription/',views.subscription,name="subscription"),
    path('freeplan/',views.freeplan,name="freeplan"),
    path('basicplan/<int:amount>',views.basicplan,name="basicplan"),
    path('standardplan/<int:amount>',views.standardplan,name="standardplan"),
    path('premiumplan/<int:amount>',views.premiumplan,name="premiumplan"),
    path('success/',views.success,name="success"),

    ]