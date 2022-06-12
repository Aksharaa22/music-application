from cgi import print_exception
from logging.config import valid_ident
import django
from django.contrib.auth.models import User
from store.models import movies2,Address, Cart, Category, Order, Product, History,MsProduct,MsProducttwo,MsCart,Mus,Book,Audio_store
from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistrationForm, AddressForm,AudioForm
from django.contrib import messages
from django.views import View
import decimal
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # for Class Based Views
from jewelryshop.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from decimal import Decimal
from django.http.response import JsonResponse


from django.http import HttpResponse

from django.db.models import Case, When

import urllib
import bs4 as bs
import re


import json

from django.http import HttpResponse
# Create your views here.

import razorpay
from django.views.decorators.csrf import csrf_exempt


#ms
def indexms(request):
    m = movies2.objects.all()
    
    return render(request,'indexms.html',{'m':m})





#homepage
def home(request):
    categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'store/index.html', context)


#song detail and related song
def detail(request, slug):
    
    product = get_object_or_404(Product, slug=slug)
    user = request.user 
    history= History(user=user, music_id=product.sku)
    history.save()
    related_products = Product.objects.exclude(id=product.id).filter(is_active=True, category=product.category)
    context = {
        'product': product,
        'related_products': related_products,

    }
    return render(request, 'store/detail.html', context)

#all categorys
def all_categories(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'store/categories.html', {'categories':categories})

#payment
def homerz(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000
        client = razorpay.Client(auth=("rzp_test_GJbO9Jo3XPJdVg", "PKLX429fwxkEwysZ0hV0bLuf"))
        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
    return render(request, "store/indexrz.html")

@csrf_exempt
def success(request):
    return render(request, "store/success.html")

#category of song inside
def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(is_active=True, category=category)
    categories = Category.objects.filter(is_active=True)
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/category_products.html', context)




    

#hisory of songs
def history(request):
    if request.method =="POST":
        user = request.user         
        music_id= request. POST[ 'music_id'] 
        history= History(user=user, music_id=music_id)
        history.save()
        return redirect(f"/history{music_id}")

    history = History.objects.filter(user=request.user).all()
    ids = []
    for i in history:
        ids.append(i.music_id)

    # preserved =Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)]) 
    song = Product.objects.filter(sku__in=ids)
    return render(request, 'store/history.html',{"history": song})


#upload of songs
def Audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST , request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = AudioForm()
    return render(request, 'store/audio.html', {'form':form})

#upload of songs-podcast list
def Audio_list(request):
    audio_list= Audio_store.objects.all()
    return render(request, 'store/audiolist.html', {'audio_list': audio_list})

# search
def search(request):
    query=request.GET.get("query")
    so= Product.objects.all()
    qs= so.filter(title__icontains=query)

    return render(request,'store/search.html',{"songs":qs})



#web scrape
def articles(request):
    # ******  source1   *******
    source = urllib.request.urlopen('https://pitchfork.com/news/').read()
    soup = bs.BeautifulSoup(source, 'lxml')
    text = []
    for paragraph in soup.find_all('p'):
        text.append(paragraph.text)
    tex = []
    for t in text:
        t = re.sub(r'\[[0-9]*\]', ' ', t)
        tex.append(t)
    # source 1 image scrapping
    list = []
    for item in soup.find_all('img'):
        list.append(item['src'])
    text.clear()
    # ******  source2  *******
    source2 = urllib.request.urlopen('https://www.outbrain.com/help/advertisers/music-blog/').read()
    soup2 = bs.BeautifulSoup(source2, 'lxml')
    text1 = []
    for paragraph in soup2.find_all('p'):
        text1.append(paragraph.text)
    tex1 = []
    for t in text1:
        t = re.sub(r'\[[0-9]*\]', ' ', t)
        tex1.append(t)
    text1.clear()

    # ******  source3  *******

    source3 = urllib.request.urlopen('http://www.bollymeaning.com/').read()
    soup3 = bs.BeautifulSoup(source3, 'lxml')
    text2 = []
    for paragraph in soup3.find_all('p'):
        text2.append(paragraph.text)

    tex2 = []
    for t in text2:
        t = re.sub(r'\[[0-9]*\]', ' ', t)
        tex2.append(t)

    text2.clear()

    return render(request, 'store/articles.html',{'text': tex, 'text2': tex1[:len(tex1) - 30], 'text3': tex2[2:len(tex2) - 20], 'list2': list[2]
                   })

@csrf_exempt
def paymentSuccess(request):
    if request.method == "POST":
        data = json.loads(request.body)

        order_id = data['order_id']
        amount = data['amount']

        username=request.user
        user=User.objects.get(username=username)
        userId=user.id

        # book_order = Bookings(order_id=order_id,amount=amount,username=username,lang="hindi")
        # book_order.save()

        # orderlist = book_order.order_list
       
        return JsonResponse({'status': "Booked Successfully", 'status_code': 200}, status=200)
    return redirect('/home/')





# Authentication Starts Here

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations! Registration Successful!")
            form.save()
        return render(request, 'account/register.html', {'form': form})
        

@login_required
def profile(request):
    addresses = Address.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user)
    return render(request, 'account/profile.html', {'addresses':addresses, 'orders':orders})


@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        form = AddressForm()
        return render(request, 'account/add_address.html', {'form': form})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            user=request.user
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            reg = Address(user=user, locality=locality, city=city, state=state)
            reg.save()
            messages.success(request, "Details Added Successfully.")
        return redirect('store:profile')


@login_required
def remove_address(request, id):
    a = get_object_or_404(Address, user=request.user, id=id)
    a.delete()
    messages.success(request, "Details removed.")
    return redirect('store:profile')

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)

    # Check whether the Product is alread in Cart or Not
    item_already_in_cart = Cart.objects.filter(product=product_id, user=user)
    if item_already_in_cart:
        cp = get_object_or_404(Cart, product=product_id, user=user)
        cp.quantity += 1
        cp.save()
    else:
        Cart(user=user, product=product).save()
    
    return redirect('store:cart')


@login_required
def cart(request):
    user = request.user
    cart_products = Cart.objects.filter(user=user)

    # Display Total on Cart Page
    amount = decimal.Decimal(0)
    shipping_amount = decimal.Decimal(10)
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in Cart.objects.all() if p.user==user]
    if cp:
        for p in cp:
            temp_amount = (p.quantity * p.product.price)
            amount += temp_amount

    # Customer Addresses
    addresses = Address.objects.filter(user=user)

    context = {
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount,
        'addresses': addresses,
    }
    return render(request, 'store/cart.html', context)


@login_required
def remove_cart(request, cart_id):
    if request.method == 'GET':
        c = get_object_or_404(Cart, id=cart_id)
        c.delete()
        messages.success(request, "Song removed from Favourite.")
    return redirect('store:cart')


@login_required
def plus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        cp.quantity += 1
        cp.save()
    return redirect('store:cart')


@login_required
def minus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        # Remove the Product if the quantity is already 1
        if cp.quantity == 1:
            cp.delete()
        else:
            cp.quantity -= 1
            cp.save()
    return redirect('store:cart')


@login_required
def checkout(request):
    user = request.user
    address_id = request.GET.get('address')
    
    address = get_object_or_404(Address, id=address_id)
    # Get all the products of User in Cart
    cart = Cart.objects.filter(user=user)
    for c in cart:
        # Saving all the products from Cart to Order
        Order(user=user, address=address, product=c.product, quantity=c.quantity).save()
        # And Deleting from Cart
        c.delete()
    return redirect('store:orders')


@login_required
def orders(request):
    all_orders = Order.objects.filter(user=request.user).order_by('-ordered_date')
    return render(request, 'store/orders.html', {'orders': all_orders})





def shop(request):
    return render(request, 'store/shop.html')





def test(request):
    return render(request, 'store/test.html')



def mcategories(request):
    return render(request, "store/mcategories.html")



def mcategory_products(request):
    
    products = MsProduct.objects.filter(is_active=True)
    
    context = {
       
        'products': products,
       
    }
    return render(request, 'store/mcategory_products.html',context)

def mcategorytwo_products(request):
    
    productstwo = MsProducttwo.objects.filter(is_active=True)
    
    context = {
       
        'productstwo': productstwo,
       
    }
    return render(request, 'store/mcategorytwo_products.html',context)


def mdetailone(request):
    product = get_object_or_404(MsProduct)
   
    context = {
        'product': product,
        
    }
    return render(request, 'store/mdetailone.html', context)







@login_required
def madd(request):
    user = request.user
    mproduct_id = request.GET.get('mprod_id')
    product = get_object_or_404(MsProduct, id=mproduct_id)

    # Check whether the Product is alread in Cart or Not
    item_already_in_cart = MsCart.objects.filter(product=mproduct_id, user=user)
    if item_already_in_cart:
        cp = get_object_or_404(MsCart, product=mproduct_id, user=user)
        cp.quantity += 1
        cp.save()
    else:
        MsCart(user=user, product=product).save()
    
    return redirect('store:mscart')

@login_required
def mscart(request):
    user = request.user
    mcart_products = MsCart.objects.filter(user=user)

    # Display Total on Cart Page
    amount = decimal.Decimal(0)
    shipping_amount = decimal.Decimal(10)
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in MsCart.objects.all() if p.user==user]
    if cp:
        for p in cp:
            temp_amount = (p.quantity * p.product.price)
            amount += temp_amount

   

    context = {
        'mcart_products': mcart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount,
        
    }
    return render(request, 'store/mscart.html', context)




client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def razorpaycheck(request):
    tot_cost = val()
    order_amount = 50000
    order_currency = 'INR'
    payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture=3009))
    payment_id = payment_order['id']
    context = {
        'amount': {{tot_cost}}, 'api_key':rzp_test_6n6SQcbSrcOw97, 'order_id':payment_order_id
    }
    return redirect('store:success')



#book
@login_required
def find(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        bus_list = Mus.objects.filter(source=source_r, dest=dest_r, date=date_r)
        if bus_list:
            return render(request, 'store/list.html', locals())
        else:
            context["error"] = "Sorry no shows availiable"
            return render(request, 'store/find.html', context)
    else:
        return render(request, 'store/find.html')

@login_required
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        seats_r = int(request.POST.get('no_seats'))
        bus = Mus.objects.get(id=id_r)
        if bus:
            if bus.rem > int(seats_r):
                name_r = bus.bus_name
                tot_cost = int(seats_r) * bus.price
                source_r = bus.source
                dest_r = bus.dest
                nos_r = Decimal(bus.nos)
                price_r = bus.price
                date_r = bus.date
                time_r = bus.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = bus.rem - seats_r
                Mus.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, bus_name=name_r,tot_cost=tot_cost,
                                           source=source_r, busid=id_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                global val
                def val():
                    return tot_cost
                # book.save()
                return render(request, 'store/bookings.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'store/find.html', context)

    else:
        return render(request, 'store/find.html')

@login_required
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            bus = Mus.objects.get(id=book.busid)
            rem_r = bus.rem + book.nos
            Mus.objects.filter(id=book.busid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect('store:seebookings')
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that music"
            return render(request, 'store/error.html', context)
    else:
        return render(request, 'store/find.html')

        
@login_required
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'store/booklist.html', locals())
    else:
        context["error"] = "Sorry no shows booked"
        return render(request, 'store/find.html', context)