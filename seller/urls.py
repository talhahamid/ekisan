from django.urls import path
from . import views


urlpatterns = [
    path('',views.sellerprofile,name="sellerprofile"),
    path('editsellerprofile/<int:id>/',views.editsellerprofile,name="editsellerprofile"),
    path('updatesellerprofile/<int:id>/',views.updatesellerprofile,name="updatesellerprofile"),
    path('sellerprofilepic/',views.sellerprofilepic,name="sellerprofilepic"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('sellersales/',views.sellersales,name="sellersales"),
    path('productsadd/<str:producttype>/',views.productsadd,name="productsadd"),
    path('productsadded/<str:productname>/<str:producttype>/<int:price>/<int:quantity>/<str:img1>/<str:img2>/<str:img3>/',views.productsadded,name="productsadded"),
    path('selleragreement/',views.selleragreement,name="selleragreement"),
    path('productprice/',views.productprice,name="productprice"),
    path('sellerbit/',views.sellerbit,name="sellerbit"),

]