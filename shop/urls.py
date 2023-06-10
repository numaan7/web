from django.urls import path,include
from . import views
urlpatterns = [
  path('',views.shop,name='shop'),
  path('<slug:url>/',views.product,name='product'),
   path('product/<int:id>/',views.product,name='product'),
   path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('checkout/checkout_details/',views.checkout,name='checkout'),
    path('placeorder/done/',views.placeorder,name="placeorder"),
    path('order/status/',views.verify,name="verify"),
    path('order/success/',views.success),
    path('order/failure/',views.failure),



]