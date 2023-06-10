from django.shortcuts import render,get_object_or_404
from .models import *
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages
import razorpay
client = razorpay.Client(auth=("Razor_pay_key", "secret_key"))

razorpay_order_id=''
razorpay_payment_id=''
razorpay_signature=''
# Create your views here.

def shop(request):
    products=Product.objects.filter(status="published")
    return render(request,'shop/productlist.html',{'products':products})
def product(request,**args):
    product=get_object_or_404(Product,**args)
    return render(request,'shop/product.html',{'product':product})


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

    

@login_required(login_url="/login")
def cart_detail(request):
    
    cart = Cart(request)
    cart=request.session.get('cart')
    sub_total=0
    discount=0
    tax=0
    request.session['subtotal']=sub_total
    request.session['tax']=tax
    request.session['discount']=discount
    for i in cart:

        a=cart[i]['price']
        b=cart[i]['quantity']
        total=int(a)*int(b)
        sub_total=total+sub_total
    if request.method=="GET":
        coupon=str(request.GET.get('coupon')).upper()
       
        if len(Offer.objects.filter(coupon=coupon)) > 0: 
          couponobj=Offer.objects.get(coupon__icontains=coupon)
          if couponobj.expired==False:
            discount=(int(couponobj.price_off)*sub_total)/100
         
            sub_total=sub_total-discount
            
            tax=(18*sub_total)/100
           
            subtotal=sub_total+tax
            
            
            request.session['subtotal']=subtotal
            request.session['tax']=tax
            request.session['discount']=discount
            return render(request, 'shop/cart.html',{'couponobj':couponobj})
          else:
              pass

   
    sub_total=sub_total-discount
    
    tax=(18*sub_total)/100

    subtotal=sub_total+tax
    
    request.session['subtotal']=subtotal
    request.session['tax']=tax
    request.session['discount']=discount
    
    return render(request, 'shop/cart.html')

    

    
def checkout(request):
    
    
    try:
        if request.method=="POST":

            uid=request.POST.get('id')
            uaddress=request.POST.get('address')
            uphone=request.POST.get('phone')
            ucity=request.POST.get('city')
            ustate=request.POST.get('state')
            uzip=request.POST.get('zip')
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
           
            address=get_object_or_404(Address,user=request.user,id=int(uid))
            if Address.objects.all().exists:
                request.user.first_name=fname
                request.user.last_name=lname
                request.user.save()
                address.address=uaddress
                address.phone=uphone
                address.city=ucity
                address.state=ustate
                address.zip=uzip
                address.save()

                return redirect('/shop/cart/cart-detail/')
    except:
        if request.method=="POST":
        
            total=(request.POST.get('subtotal'))
            total=int(total)+40
            address=Address.objects.filter(user=request.user)
            return render(request,'shop/checkout.html',{'subtotal':total*100,'addresses':address})
        else:
           return redirect('/shop/cart/cart-detail/')
    

def placeorder(request):
        
        if request.method=='POST':
            price=request.POST.get("price")
            addressid=request.POST.get("addressid")
         
            
    
            data = { "amount": int(price), "currency": "INR", "receipt": "order_rcptid_11" }
            payment = client.order.create(data=data)
 
            cart=request.session.get('cart')
   
            fullprice=int(price)/100
            for i in cart:
               product=cart[i]['name']
               price=cart[i]['price']
               quantity=cart[i]['quantity']
               address=get_object_or_404(Address,id=int(addressid))
               total=fullprice
              

               order_id=payment['id']
               user=request.user
               product_id=cart[i]['product_id']
               order=Order(product=product,price=price,quantity=quantity,address=address,total=total,order_id=order_id,user=user,product_id=product_id)
               order.save()

        return render(request,'shop/payment.html',{'payment':payment})

@csrf_exempt
def verify(request):
    if request.method=='POST':
        razorpay_order_id=request.POST.get('razorpay_order_id')
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
     
        try: 
            params_dict = {
                    'razorpay_order_id': razorpay_order_id,
                    'razorpay_payment_id': payment_id,
                    'razorpay_signature': signature
                }
            payment=client.utility.verify_payment_signature(params_dict)
            
            if payment==True:
                Order.objects.filter(order_id=razorpay_order_id).update(signature=signature,payment_id=payment_id,paid=True)
                
                return redirect(f'/shop/order/success/?id={razorpay_order_id}')
                
            
        except:
            return redirect(f'/shop/order/failure/?id={razorpay_order_id}')
def success(request):
    cart_clear(request)

    orderid=request.GET.get('id')
    messages.success(request, f"Your order ({orderid}) is successfully placed.")
    return render(request,'shop/success.html',{'orderid':orderid})
def failure(request):
    orderid=request.GET.get('id')
    messages.error(request, f"Oops there is some payment failure with your order ({orderid}).")
    return render(request,'shop/failure.html',{'orderid':orderid})

