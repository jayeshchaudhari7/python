from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Restaurant, MenuItem, Cart, Order, Review

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def restaurant_detail(request, id):
    restaurant = Restaurant.objects.get(id=id)
    menu = MenuItem.objects.filter(restaurant=restaurant)
    reviews = Review.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'menu': menu,
        'reviews': reviews,
    })

@login_required
def submit_review(request, restaurant_id):
    if request.method == "POST":
        review_text = request.POST.get("review")
        rating = int(request.POST.get("rating"))
        restaurant = Restaurant.objects.get(id=restaurant_id)
        Review.objects.create(
            user=request.user,
            restaurant=restaurant,
            review=review_text,
            rating=rating
        )
    return redirect('restaurant_detail', id=restaurant_id)

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def cart(request):
    items = Cart.objects.filter(user=request.user)
    total = sum(i.item.price * i.quantity for i in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

@login_required
def add_to_cart(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    Cart.objects.create(user=request.user, item=item)
    return redirect('cart')

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(i.item.price * i.quantity for i in cart_items)
    order = Order.objects.create(user=request.user, total=total)
    for item in cart_items:
        order.items.add(item.item)
    cart_items.delete()
    return redirect('orders')

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})
