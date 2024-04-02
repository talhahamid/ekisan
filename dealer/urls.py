from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.dealers,name="dealers"),

    path('addbuy/',views.addbuy,name="addbuy"),  
    path('buy/',views.buy,name="buy"),

    path('sale/',views.sales,name="sales"),      

    path('dealersprofile/',views.dealersprofile,name="dealersprofile"),
    path('editdealerprofile/<int:id>/',views.editdealerprofile,name="editdealerprofile"),
    path('updatedealerprofile/<int:id>/',views.updatedealerprofile,name="updatedealerprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('dealerprofilepic/',views.dealerprofilepic,name="dealerprofilepic"),

    path('delivery/',views.delivery,name="delivery"),

    path('productcategory/',views.productcategory,name="productcategory"),
    path('productcategorylist/',views.productcategorylist,name="productcategorylist"), 

    path('productlist/<str:fruit>/',views.productlist,name="productlist"),
    path('productslist/<str:fruit>/',views.productslist,name="productslist"),

    path('transactions/',views.transactions,name="transactions"),

    path('vegitables/',views.vegitables,name="vegitables"),
    path('fruits/',views.fruits,name="fruits"),
    path('crops/',views.crops,name="crops"),
    path('herb/',views.herb,name="herb"),
    path('nuts/',views.nuts,name="nuts"),
    path('grains/',views.grains,name="grains"),
    path('legumes/',views.legumes,name="legumes"),
    path('tubers/',views.tubers,name="tubers"),
    path('berries/',views.berries,name="berries"),
    path('flowers/',views.flowers,name="flowers"),
    path('leafygreens/',views.leafygreens,name="leafygreens"),
    path('roots/',views.roots,name="roots"),
    path('spices/',views.spices,name="spices"),
    path('medicinalplants/',views.medicinalplants,name="medicinalplants"),
    path('mushrooms/',views.mushrooms,name="mushrooms"),
    path('pulses/',views.pulses,name="pulses"),
    path('oilseeds/',views.oilseeds,name="oilseeds"),
    path('covercrops/',views.covercrops,name="covercrops"),
    path('condiments/',views.condiments,name="condiments"),
    path('exoticplants/',views.exoticplants,name="exoticplants"),


    path('bit/<int:user_id>/<str:user_name>/<str:product_name>/<str:product_type>/<str:quality>/<str:rate>/<str:quantity>/',views.bit,name="bit"),
    path('process_bit/<int:id>/', views.process_bit, name='process_bit'),

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