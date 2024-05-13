from django.urls import path
from . import views

app_name = 'farmer'

urlpatterns = [
    path('',views.farmer,name="farmer"),

    path('farmerprofile/',views.farmerprofile,name="farmerprofile"),
    path('editfarmerprofile/<int:id>/',views.editfarmerprofile,name="editfarmerprofile"),
    path('updatefarmerprofile/<int:id>/',views.updatefarmerprofile,name="updatefarmerprofile"),
    path('farmerprofilepic/',views.farmerprofilepic,name="farmerprofilepic"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('sales/',views.sales,name="sales"),
    path('productprice/',views.productprice,name="productprice"),
    path('productpriceadd/',views.productpriceadd,name="productpriceadd"),
    path('productpriceadddone/<str:product_name>/<str:product_type>/<str:quality>/<int:rate>/<int:quantity>/',views.productpriceadddone,name="productpriceadddone"),

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

    path('farmerbit/',views.farmerbit,name="farmerbit"),
    
    path('accept_bit/<int:dealerbit_id>/',views.accept_bit,name="accept_bit"),

    path('subscription/',views.subscription,name="subscription"),
    path('freeplan/',views.freeplan,name="freeplan"),
    path('basicplan/<int:amount>',views.basicplan,name="basicplan"),
    path('standardplan/<int:amount>',views.standardplan,name="standardplan"),
    path('premiumplan/<int:amount>',views.premiumplan,name="premiumplan"),
    path('success/',views.success,name="success"),

    path('farmeragreement/',views.farmeragreement,name="farmeragreement"),
    path('farmeragreementdone/',views.farmeragreementdone,name="farmeragreementdone"),
    
    path('buy/',views.buy,name="buy"),
    path('productlists/<str:producttype>/',views.productlists,name="productlists"),
    path('bit/<str:productname>/<str:producttype>/<str:img1>/<str:img2>/<str:img3>/<int:price>/<int:quantity>/',views.bit,name="bit"),

    path('renterslist/',views.renterslist,name="renterslist"),

    path('rent/',views.rent,name="rent"),

    path('getweather/',views.get_weather,name="get_weather"),

    # path('farm_view/',views.farm_view,name="farm_view"),
    # path('add_farmer/',views.add_farmer,name="add_farmer"),    
    # path('farm_stream/<int:pk>/',views.farm_stream,name="farm_stream"),    
    ]